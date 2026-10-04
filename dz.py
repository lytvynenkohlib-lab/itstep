import time
import unittest


def measure_execution_time(func, *args, **kwargs):
  start_time = time.perf_counter()
  result = func(*args, **kwargs)
  end_time = time.perf_counter()
  execution_time = end_time - start_time
  return result, execution_time




def sample_function_sleep(seconds):
  time.sleep(seconds)
  return "done"


def sample_function_add(a, b):
  return a + b


class TestMeasureExecutionTime(unittest.TestCase):

  def test_execution_time_duration(self):
    delay = 0.1
    result, exec_time = measure_execution_time(
        sample_function_sleep, seconds=delay
    )
    self.assertEqual(result, "done")
    self.assertGreaterEqual(exec_time, delay)
    self.assertLess(
        exec_time, delay + 0.05
    )

  def test_function_arguments_and_return(self):
    result, exec_time = measure_execution_time(sample_function_add, 5, 10)
    self.assertEqual(result, 15)
    self.assertGreater(exec_time, 0)


if __name__ == "__main__":
  unittest.main()