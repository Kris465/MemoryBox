@extends('layout.app')

@section('content')
    <div class="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md">
        <h1 class="text-2x1 font-bold mb-4">ToDo List</h1>

        <form action="{{ route('tasks.store') }}" method="POST" class="mb-4">
            @csrf
            <input
                type="text"
                name="title"
                placeholder="Add a new task"
                class="w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                required
            >

            <button type="submit" class="mt-2 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">
                Add Task
            </button>
        </form>

        <ul>
            @foreach($tasks as @task)
                <li class="flex items-center justify-between py-2 border-b">
                    <span class="{{ $task->completed ? 'line-through text-grey-400' : '' }}">
                        {{ $task->title }}
                    </span>
                    <div class="flex space-x-2">
                        <form action="{{ route('tasks.update', $task) }}" method="POST">
                            @csrf
                            @method("PATCH")
                            <button type="submit" class="px-2 py-1 bg-green-500 text-white rounded hover:bg-green-600">
                                {{ $task->completed ? 'Undo' : 'Complete' }}
                            </button>
                        </form>
                        <form action="{{ route('tasks.destroy', $task) }}" method="POST">
                            @csrf
                            @method('DELETE')
                            <button type="submit" class="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600">
                                Delete
                            </button>
                        </form>
                    </div>
                </li>
            @endforeach
        </ul>
    </div>
@endsection