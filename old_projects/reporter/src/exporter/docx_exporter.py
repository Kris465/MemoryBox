# src/exporter/docx_exporter.py
import os
import re
from typing import Dict, List, Optional
from loguru import logger
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


class DocxExporter:
    def __init__(self):
        """Инициализация экспортера в DOCX"""
        self.template_path = "templates\\reference.docx"
        logger.info("DocxExporter инициализирован")

    def _clean_lecture_title(self, title: str) -> str:
        """Очистка названия лекции от лишних префиксов"""
        prefixes_to_remove = [
            r'^конспект лекции:\s*',
            r'^лекция\s*\d*[\.:]*\s*',
            r'^конспект:\s*',
            r'^тема\s*\d*[\.:]*\s*',
        ]
        
        cleaned_title = title.strip()
        
        for prefix in prefixes_to_remove:
            cleaned_title = re.sub(prefix, '', cleaned_title, flags=re.IGNORECASE)
        
        cleaned_title = re.sub(r'^[-\–\—]\s*', '', cleaned_title)
        cleaned_title = re.sub(r'\*\*|\*|`', '', cleaned_title)
        cleaned_title = re.sub(r'\s+', ' ', cleaned_title).strip()
        
        return cleaned_title

    def _extract_meaningful_title(self, summary_path: str) -> str:
        """Извлечение осмысленного названия лекции"""
        try:
            with open(summary_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.split('\n')
            meaningful_titles = []
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                    
                if line.startswith('# '):
                    title = self._clean_lecture_title(line[2:])
                    if title and len(title) > 10:
                        meaningful_titles.append(title)
                
                elif line.startswith('## '):
                    title = self._clean_lecture_title(line[3:])
                    if title and len(title) > 15:
                        meaningful_titles.append(title)
            
            if meaningful_titles:
                return meaningful_titles[0]
            else:
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('#') and len(line) > 20:
                        clean_line = self._clean_lecture_title(line)
                        return clean_line[:80]
            
            return "Материал лекции"
            
        except Exception as e:
            logger.warning(f"Не удалось извлечь название лекции: {e}")
            return "Материал лекции"

    def _get_course_title(self, week_summaries: List[Dict]) -> str:
        """Определение названия курса из конспектов"""
        if week_summaries:
            topic = self._extract_meaningful_title(week_summaries[0]['summary_path'])
            return topic
        return "Конспект лекций"

    def _create_clean_table_of_contents(self, doc: Document, week_number: int, summaries: List[Dict]):
        """Создание чистого и простого оглавления"""
        try:
            # Добавляем заголовок СОДЕРЖАНИЕ
            toc_title = doc.add_paragraph("СОДЕРЖАНИЕ")
            toc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            toc_title.runs[0].bold = True
            toc_title.runs[0].font.size = Pt(16)
            toc_title.runs[0].font.color.rgb = None
            
            doc.add_paragraph()
            
            # Добавляем информацию о неделе
            week_info = doc.add_paragraph(f"Неделя {week_number}")
            week_info.runs[0].bold = True
            week_info.runs[0].font.size = Pt(14)
            week_info.runs[0].font.color.rgb = None
            
            doc.add_paragraph()
            
            # Просто перечисляем лекции без подразделов
            for i, summary in enumerate(summaries, 1):
                lecture_title = self._extract_meaningful_title(summary['summary_path'])
                clean_title = self._clean_lecture_title(lecture_title)
                
                toc_item = doc.add_paragraph(f"{i}. {clean_title}")
                toc_item.paragraph_format.left_indent = Pt(0)
                toc_item.paragraph_format.first_line_indent = Pt(0)
                
                for run in toc_item.runs:
                    run.font.color.rgb = None
                    run.font.size = Pt(12)
            
            doc.add_page_break()
            
            logger.info(f"Создано оглавление с {len(summaries)} лекциями")
            
        except Exception as e:
            logger.warning(f"Не удалось добавить оглавление: {e}")

    def _create_different_first_page(self, doc: Document):
        """Создание разных настроек для первой страницы (без номера)"""
        try:
            section = doc.sections[0]
            section.different_first_page_header_footer = True
            
            first_page_footer = section.first_page_footer
            for paragraph in first_page_footer.paragraphs:
                p = paragraph._element
                p.getparent().remove(p)
            
            first_page_footer_paragraph = first_page_footer.add_paragraph()
            first_page_footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
        except Exception as e:
            logger.warning(f"Не удалось настроить разные страницы: {e}")

    def _add_page_numbers(self, doc: Document):
        """Добавление нумерации страниц (начиная со второй страницы)"""
        try:
            section = doc.sections[0]
            footer = section.footer
            
            for paragraph in footer.paragraphs:
                p = paragraph._element
                p.getparent().remove(p)
            
            footer_paragraph = footer.add_paragraph()
            footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            run = footer_paragraph.add_run()
            fld_char = OxmlElement('w:fldChar')
            fld_char.set(qn('w:fldCharType'), 'begin')
            
            instr_text = OxmlElement('w:instrText')
            instr_text.set(qn('xml:space'), 'preserve')
            instr_text.text = 'PAGE'
            
            fld_char2 = OxmlElement('w:fldChar')
            fld_char2.set(qn('w:fldCharType'), 'end')
            
            run._r.append(fld_char)
            run._r.append(instr_text)
            run._r.append(fld_char2)
            
            run.font.name = 'Times New Roman'
            run.font.size = Pt(12)
            run.font.color.rgb = None
            
        except Exception as e:
            logger.warning(f"Не удалось добавить нумерацию страниц: {e}")

    def _setup_heading_styles(self, doc: Document):
        """Настройка стилей заголовков с черным цветом"""
        try:
            if 'Heading 1' not in doc.styles:
                heading1 = doc.styles.add_style('Heading 1', 1)
            else:
                heading1 = doc.styles['Heading 1']
            
            heading1.font.name = 'Times New Roman'
            heading1.font.size = Pt(16)
            heading1.font.bold = True
            heading1.font.color.rgb = None
            
            if 'Heading 2' not in doc.styles:
                heading2 = doc.styles.add_style('Heading 2', 1)
            else:
                heading2 = doc.styles['Heading 2']
            
            heading2.font.name = 'Times New Roman'
            heading2.font.size = Pt(14)
            heading2.font.bold = True
            heading2.font.color.rgb = None
            
            if 'Heading 3' not in doc.styles:
                heading3 = doc.styles.add_style('Heading 3', 1)
            else:
                heading3 = doc.styles['Heading 3']
            
            heading3.font.name = 'Times New Roman'
            heading3.font.size = Pt(14)
            heading3.font.italic = True
            heading3.font.color.rgb = None
            
        except Exception as e:
            logger.warning(f"Не удалось настроить стили заголовков: {e}")

    def _clean_markdown_line(self, line: str) -> str:
        """Тщательная очистка строки от Markdown артефактов"""
        line = line.strip()
        
        if line in ['---', '***', '___']:
            return ''
        
        line = re.sub(r'^>\s*', '', line)
        line = re.sub(r'#+\s*', '', line)
        line = re.sub(r'\*\*([^*]+)\*\*', r'\1', line)
        line = re.sub(r'\*([^*]+)\*', r'\1', line)
        line = re.sub(r'`([^`]+)`', r'\1', line)
        line = re.sub(r'~~([^~]+)~~', r'\1', line)
        
        line = re.sub(r'^[-*+]\s+', '', line)
        line = re.sub(r'^\d+\.\s+', '', line)
        
        line = re.sub(r'<br\s*/?>', '\n', line)
        line = re.sub(r'<[^>]+>', '', line)
        
        return line.strip()

    def _is_table_separator(self, line: str) -> bool:
        """Проверяет, является ли строка разделителем таблицы"""
        line = line.strip()
        if not line.startswith('|'):
            return False
        
        clean_line = line.replace('|', '').replace('-', '').replace(':', '').replace(' ', '')
        return len(clean_line) == 0

    def _should_skip_line(self, line: str, lecture_title: str) -> bool:
        """Определяет, нужно ли пропустить строку (дублирующую заголовок)"""
        if not line.strip():
            return False
            
        clean_line = self._clean_markdown_line(line)
        
        if (line.startswith('# ') or line.startswith('## ')) and clean_line:
            clean_lecture_title = self._clean_lecture_title(lecture_title)
            
            words_line = set(clean_line.lower().split())
            words_title = set(clean_lecture_title.lower().split())
            
            if words_line and words_title:
                common_words = words_line.intersection(words_title)
                similarity = len(common_words) / max(len(words_line), len(words_title))
                
                if similarity > 0.7:
                    return True
        
        return False

    def _is_list_item(self, text: str) -> bool:
        """Проверяет, является ли текст элементом списка"""
        patterns = [
            r'^[•\-*+]\s+',
            r'^[а-яa-z]\.\s+',
            r'^\d+\.\s+',
        ]
        
        for pattern in patterns:
            if re.match(pattern, text, re.IGNORECASE):
                return True
        return False

    def _add_lecture_content(self, doc: Document, summary_path: str, lecture_num: int):
        """Добавление контента лекции с правильным оформлением"""
        try:
            with open(summary_path, 'r', encoding='utf-8') as f:
                content = f.read()

            lecture_meaningful_title = self._extract_meaningful_title(summary_path)
            
            # Добавляем заголовок лекции
            lecture_title = doc.add_paragraph(f"Лекция {lecture_num}. {lecture_meaningful_title}", style='Heading 1')
            lecture_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
            lecture_title.paragraph_format.space_after = Pt(18)

            lines = content.split('\n')
            in_table = False
            table_rows = []
            current_paragraph = None
            content_started = False
            in_list = False

            for i, line in enumerate(lines):
                line = line.strip()
                if not line:
                    if current_paragraph:
                        current_paragraph = None
                    in_list = False
                    continue

                # Пропускаем разделители
                if line in ['---', '***', '___']:
                    if current_paragraph:
                        current_paragraph = None
                    in_list = False
                    continue

                # Пропускаем строки, начинающиеся с одиночного >
                if line.startswith('> ') and len(line) > 2 and not line.startswith('> «'):
                    line = line[2:].strip()

                if not content_started and self._should_skip_line(line, lecture_meaningful_title):
                    continue
                
                if not content_started and line.strip():
                    content_started = True

                # Обработка таблиц
                if line.startswith('|') and '|' in line:
                    if self._is_table_separator(line):
                        continue
                    
                    if not in_table:
                        in_table = True
                        table_rows = []
                    
                    cells = [self._clean_markdown_line(cell) for cell in line.split('|') if cell.strip()]
                    if cells:
                        table_rows.append(cells)
                    continue
                elif in_table and table_rows:
                    self._create_proper_table(doc, table_rows)
                    in_table = False
                    table_rows = []
                    current_paragraph = None
                    in_list = False
                    continue

                # Обработка заголовков
                if line.startswith('# '):
                    in_list = False
                    if current_paragraph:
                        current_paragraph = None
                    
                    title = self._clean_markdown_line(line)
                    if title and not self._should_skip_line(line, lecture_meaningful_title):
                        heading = doc.add_paragraph(title, style='Heading 1')
                        heading.paragraph_format.space_before = Pt(12)
                        heading.paragraph_format.space_after = Pt(6)
                        heading.paragraph_format.first_line_indent = Pt(0)
                    continue

                elif line.startswith('## '):
                    in_list = False
                    if current_paragraph:
                        current_paragraph = None
                    
                    title = self._clean_markdown_line(line)
                    if title:
                        subheading = doc.add_paragraph(title, style='Heading 2')
                        subheading.paragraph_format.space_before = Pt(9)
                        subheading.paragraph_format.space_after = Pt(3)
                        subheading.paragraph_format.first_line_indent = Pt(0)
                    continue

                elif line.startswith('### '):
                    in_list = False
                    if current_paragraph:
                        current_paragraph = None
                    
                    title = self._clean_markdown_line(line)
                    if title:
                        subsubheading = doc.add_paragraph(title, style='Heading 3')
                        subsubheading.paragraph_format.space_before = Pt(6)
                        subsubheading.paragraph_format.space_after = Pt(3)
                        subsubheading.paragraph_format.first_line_indent = Pt(0)
                    continue

                # Обработка списков - только первый уровень
                if self._is_list_item(line):
                    in_list = True
                    if current_paragraph:
                        current_paragraph = None
                    
                    text = self._clean_markdown_line(line)
                    if text:
                        # Для списков используем минимальный отступ
                        list_para = doc.add_paragraph()
                        list_para.paragraph_format.left_indent = Pt(25)  # Минимальный отступ
                        list_para.paragraph_format.first_line_indent = Pt(0)
                        
                        # Определяем маркер в зависимости от типа списка
                        if re.match(r'^[•\-*+]', line):
                            marker = '• '
                        elif re.match(r'^[а-яa-z]\.', line.lower()):
                            marker = ''
                        elif re.match(r'^\d+\.', line):
                            marker = ''
                        else:
                            marker = '• '
                        
                        run = list_para.add_run(marker + text)
                        run.font.size = Pt(14)
                        run.font.color.rgb = None
                        list_para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                    continue

                # Обработка цитат
                elif line.startswith('> '):
                    in_list = False
                    if current_paragraph:
                        current_paragraph = None
                    
                    text = self._clean_markdown_line(line)
                    if text:
                        quote_para = doc.add_paragraph(text)
                        quote_para.paragraph_format.left_indent = Pt(25)
                        quote_para.paragraph_format.first_line_indent = Pt(0)
                        quote_para.paragraph_format.space_before = Pt(3)
                        quote_para.paragraph_format.space_after = Pt(3)
                        quote_para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                        for run in quote_para.runs:
                            run.font.color.rgb = None
                    continue

                # Обычный текст
                else:
                    clean_line = self._clean_markdown_line(line)
                    if clean_line:
                        # Если мы внутри списка, продолжаем текущий параграф
                        if in_list and current_paragraph:
                            current_paragraph.add_run(' ' + clean_line)
                        else:
                            if current_paragraph:
                                current_paragraph.add_run(' ' + clean_line)
                            else:
                                current_paragraph = doc.add_paragraph(clean_line)
                                current_paragraph.paragraph_format.first_line_indent = Pt(0)
                                current_paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                                for run in current_paragraph.runs:
                                    run.font.color.rgb = None
                            in_list = False

            if in_table and table_rows:
                self._create_proper_table(doc, table_rows)

        except Exception as e:
            logger.error(f"Ошибка добавления контента лекции: {e}")
            raise

    def _create_proper_table(self, doc: Document, rows: List[List[str]]):
        """Создание правильно оформленной таблицы"""
        try:
            if len(rows) < 1:
                return
            
            num_cols = len(rows[0])
            table = doc.add_table(rows=len(rows), cols=num_cols)
            table.style = 'Table Grid'
            table.autofit = False
            
            for i, row in enumerate(rows):
                for j, cell_text in enumerate(row):
                    if j < num_cols:
                        cell = table.cell(i, j)
                        cell.text = cell_text
                        
                        for paragraph in cell.paragraphs:
                            paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                            paragraph.paragraph_format.first_line_indent = Pt(0)
                            for run in paragraph.runs:
                                run.font.name = 'Times New Roman'
                                run.font.size = Pt(12)
                                run.font.color.rgb = None
                        
                        cell.vertical_alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            if num_cols == 2:
                table.columns[0].width = Inches(1.5)
                table.columns[1].width = Inches(4.5)
            elif num_cols == 3:
                table.columns[0].width = Inches(1.5)
                table.columns[1].width = Inches(2.0)
                table.columns[2].width = Inches(2.5)
            else:
                col_width = Inches(6.0 / num_cols)
                for col in table.columns:
                    col.width = col_width
            
            if len(rows) > 0:
                for j in range(num_cols):
                    cell = table.cell(0, j)
                    for paragraph in cell.paragraphs:
                        for run in paragraph.runs:
                            run.bold = True
                            run.font.color.rgb = None
            
            doc.add_paragraph()
            
        except Exception as e:
            logger.warning(f"Не удалось создать таблицу: {e}")

    def _setup_gost_styles(self, doc: Document):
        """Настройка стилей по ГОСТу (без красных строк)"""
        try:
            style = doc.styles['Normal']
            style.font.name = 'Times New Roman'
            style.font.size = Pt(14)
            style.font.color.rgb = None
            
            paragraph_format = style.paragraph_format
            paragraph_format.line_spacing = 1.5
            paragraph_format.space_before = Pt(0)
            paragraph_format.space_after = Pt(0)
            paragraph_format.first_line_indent = Pt(0)
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            
        except Exception as e:
            logger.warning(f"Не удалось настроить стили: {e}")

    def create_week_report(self, week_number: int, summaries: List[Dict], output_path: str) -> str:
        """Создание отчета для недели"""
        try:
            if not os.path.exists(self.template_path):
                raise FileNotFoundError(f"Шаблон {self.template_path} не найден")
                
            doc = Document(self.template_path)
            logger.info("Используется шаблон reference.docx")

            course_title = self._get_course_title(summaries)
            logger.info(f"Тема: {course_title}")
            
            for paragraph in doc.paragraphs:
                if '{{TITLE}}' in paragraph.text:
                    paragraph.text = paragraph.text.replace('{{TITLE}}', course_title)
                    for run in paragraph.runs:
                        run.font.color.rgb = None
                    break

            # Настраиваем стили
            self._setup_gost_styles(doc)
            self._setup_heading_styles(doc)
            
            # Настраиваем разные страницы
            self._create_different_first_page(doc)
            self._add_page_numbers(doc)
            
            # Добавляем простое оглавление
            self._create_clean_table_of_contents(doc, week_number, summaries)

            # Добавляем контент лекций
            for i, summary in enumerate(summaries, 1):
                if i > 1:
                    doc.add_page_break()
                
                self._add_lecture_content(doc, summary['summary_path'], i)

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            doc.save(output_path)
            logger.success(f"Отчет недели {week_number} сохранен: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Ошибка создания отчета: {e}")
            raise

    def export_course_reports(self, summaries_dir: str = "./data/summaries",
                             output_dir: str = "./data/reports",
                             weeks_to_process: Optional[List[int]] = None) -> Dict:
        """Создание отчетов для всего курса"""
        if not os.path.exists(summaries_dir):
            raise FileNotFoundError(f"Папка не найдена: {summaries_dir}")

        logger.info(f"Создание отчетов для: {summaries_dir}")

        week_dirs = []
        for item in os.listdir(summaries_dir):
            item_path = os.path.join(summaries_dir, item)
            if os.path.isdir(item_path) and item.startswith("week_"):
                week_dirs.append(item_path)

        week_dirs.sort(key=lambda x: int(x.split("_")[-1]))

        if weeks_to_process:
            week_dirs = [wd for wd in week_dirs if int(wd.split("_")[-1]) in weeks_to_process]

        course_results = {}
        for week_dir in week_dirs:
            week_num = int(week_dir.split("_")[-1])
            logger.info(f"Создание отчета для недели {week_num}")

            try:
                week_summaries = []
                for file in os.listdir(week_dir):
                    if file.endswith('_summary.txt') or file.endswith('_summary.md'):
                        summary_path = os.path.join(week_dir, file)
                        week_summaries.append({
                            'summary_path': summary_path,
                            'video_name': file.replace('_summary.txt', '').replace('_summary.md', '')
                        })

                if not week_summaries:
                    logger.warning(f"Нет конспектов для недели {week_num}")
                    continue

                logger.info(f"Найдено конспектов: {len(week_summaries)}")

                output_path = os.path.join(output_dir, f"week_{week_num}_report.docx")
                report_path = self.create_week_report(week_num, week_summaries, output_path)
                
                course_results[week_num] = {
                    'report_path': report_path,
                    'summaries_count': len(week_summaries)
                }

            except Exception as e:
                logger.error(f"Ошибка для недели {week_num}: {e}")
                course_results[week_num] = None

        total_reports = sum(1 for result in course_results.values() if result)
        logger.success(f"Создано отчетов: {total_reports}")
        return course_results