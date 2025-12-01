# Алгосы
Факториал, Фибоначчи, 6 сортировок, Стэк и Очередь

[Практика](https://github.com/boltozviak/leetcode)♥

## Поставить
```zsh
#скопировать репозиторий
git clone <repository-url>`
cd lab3_algo_pack

#поставить зависимости
uv sync

#отчёт с бенчмарками
python3 -m src.main

#запустить тесты
uv run pytest tests/ -v
```

## Мат Функции
- [Факториал](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/funcs/fact.py)
  - `fact_iter(n)` - вычисление факториала итеративно(через цикл)
  - `fact_recursive(n)` - вычисление факториала рекурсивно

- [Фибоначчи](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/funcs/fibo.py)
начальные значения: 0 и 1
  - `fibo_iter(n)` - n-е число Фибоначчи итеративно(через цикл)
  - `fibo_recursive(n)` - n-е число Фибоначчи рекурсивно

## Сортировки
- [bubble](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/sortings/bubble.py) - пузырьковая сортировка O(n²)
  - `bubble_sort(arr)` - простая, стабильная, для малых массивов

- [quick](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/sortings/quick.py) -
  - `quick_sort(arr)` - с оптимизациями: медиана из трёх для выбора опорного элемента, insertion sort для малых массивов

- [radix](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/sortings/radix.py)
  - `radix_sort(arr, base)` - поразрядная сортировка, работает с отрицательными числами, настраиваемая база
  - `count_for_radix()` - стабильная сортировка подсчётом для одного разряда

- [bucket](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/sortings/bucket.py)
  - `bucket_sort(arr, buckets)` - блочная сортировка для равномерно распределённых данных (int/float)
  - `recursive_bucket()` - рекурсивное разбиение на блоки

- [counting](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/sortings/counting.py)
  - `counting_sort(arr)` - стабильная сортировка подсчётом, только для целых чисел

- [heap](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/sortings/heap.py)
  - `heap_sort(arr)` - пирамидальная сортировка на месте, нестабильная
  - `heapify()` - восстановление свойства кучи

## Структуры данных
- [Stack](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/structures/stack.py) - стек на односвязном списке
  - `push(value)` - добавить элемент O(1)
  - `pop()` - извлечь верхний элемент O(1)
  - `peek()` - посмотреть верхний элемент O(1)
  - `min()` - найти минимум O(1) (хранится в каждом узле)
  - `is_empty()` - проверка на пустоту

- [Queue](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/structures/queue.py) - очередь на односвязном списке
  - `enqueue(value)` - добавить в конец O(1)
  - `dequeue()` - извлечь из начала O(1)
  - `front()` - посмотреть первый элемент O(1)
  - `is_empty()` - проверка на пустоту

## Утилиты
- [Benchmarks](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/utils/benchmarks.py)
  - `timeit_once(func, *args)` - однократный замер времени выполнения
  - `benchmark_sorts(arrays, algos)` - сравнение сортировок на разных типах данных

- [Test-generators](https://github.com/boltozviak/lab3_algo_pack/blob/main/src/utils/test_generator.py) - генерация тестовых данных
  - `rand_int_array(n, lo, hi, distinct, seed)` - случайный массив целых чисел
  - `nearly_sorted(n, swaps, seed)` - почти отсортированный массив
  - `many_duplicates(n, k_unique, seed)` - массив с множеством дубликатов
  - `reverse_sorted(n)` - отсортированный в обратном порядке
  - `rand_float_array(n, lo, hi, seed)` - случайный массив вещественных чисел
