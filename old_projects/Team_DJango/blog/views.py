
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Post
import random
import string
import json
from django.utils import timezone
import datetime

def generate_captcha_text(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

class CaptchaView(View):
    def get(self, request, *args, **kwargs):
        last_captcha_time_str = request.session.get('last_captcha_success')

        if last_captcha_time_str:
            try:
                last_captcha_dt = datetime.datetime.fromisoformat(last_captcha_time_str)
                
                if timezone.is_aware(last_captcha_dt):
                    now = timezone.now()
                else:
                    now = datetime.datetime.now()

                time_difference = now - last_captcha_dt
                
                if time_difference.total_seconds() < 1800:
                    print("Пользователь перенаправлен, так как прошло менее 30 минут.")
                    return HttpResponseRedirect(reverse('firstpage'))
            except ValueError:
                print("Ошибка: Неверный формат временной метки 'last_captcha_success' в сессии.")
                pass
            except Exception as e:
                print(f"Неожиданная ошибка при проверке времени CAPTCHA: {e}")
                pass

        captcha_text = generate_captcha_text()
        request.session['captcha_text'] = captcha_text
        return render(request, 'index.html', {'captcha_text': captcha_text})

    def post(self, request, *args, **kwargs):
        user_input = request.POST.get('user_input', '').strip()
        session_captcha = request.session.get('captcha_text', '').strip()

        if user_input.lower() == session_captcha.lower():
            if 'captcha_text' in request.session:
                del request.session['captcha_text']
            
            request.session['last_captcha_success'] = timezone.now().isoformat()
            request.session.modified = True
            
            return HttpResponseRedirect(reverse('firstpage'))
        else:
            captcha_text = generate_captcha_text()
            request.session['captcha_text'] = captcha_text
            return render(request, 'index.html', {'error_message': 'Неверный код CAPTCHA. Попробуйте снова.', 'captcha_text': captcha_text})

class FirstPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'firstpage.html')

class BlogListView(ListView):
    model = Post
    template_name = 'blog/main.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class AddPostApiView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            title = data.get('title')
            category = data.get('category')
            image = data.get('image')
            content = data.get('content')

            if not all([title, category, content]):
                return JsonResponse({'success': False, 'message': 'Missing required fields.'}, status=400)

            post = Post.objects.create(
                title=title,
                category=category,
                image=image,
                content=content,
            )
            return JsonResponse({'success': True, 'message': 'Post added successfully!', 'post_id': post.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
