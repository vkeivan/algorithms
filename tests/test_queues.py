from queues.queue import ArrayQueue, LinkedListQueue
from queues.max_sliding_window import max_sliding_window
from queues.reconstruct_queue import reconstruct_queue

import unittest

class TestQueue(unittest.TestCase):
    """
        Test suite for the Queue data structures.
    """

    def test_ArrayQueue(self):
        queue = ArrayQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # test __iter__()
        it = iter(queue)
        self.assertEqual(1, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(3, next(it))
        self.assertRaises(StopIteration, next, it)

        # test __len__()
        self.assertEqual(3, len(queue))

        # test is_empty()
        self.assertFalse(queue.is_empty())

        # test peek()
        self.assertEqual(1, queue.peek())

        # test dequeue()
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())

        self.assertTrue(queue.is_empty())

    def test_LinkedListQueue(self):
        queue = LinkedListQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # test __iter__()
        it = iter(queue)
        self.assertEqual(1, next(it))
        self.assertEqual(2, next(it))
        self.assertEqual(3, next(it))
        self.assertRaises(StopIteration, next, it)

        # test __len__()
        self.assertEqual(3, len(queue))

        # test is_empty()
        self.assertFalse(queue.is_empty())

        # test peek()
        self.assertEqual(1, queue.peek())

        # test dequeue()
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        self.assertEqual(3, queue.dequeue())

        self.assertTrue(queue.is_empty())

class TestSuite(unittest.TestCase):

    def test_max_sliding_window(self):

        array = [1, 3, -1, -3, 5, 3, 6, 7]
        self.assertEqual(max_sliding_window(array, k=5), [5, 5, 6, 7])
        self.assertEqual(max_sliding_window(array, k=3), [3, 3, 5, 5, 6, 7])
        self.assertEqual(max_sliding_window(array, k=7), [6, 7])

        array = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
        self.assertEqual(max_sliding_window(array, k=4), [10, 10, 10, 15, 15, 90, 90])
        self.assertEqual(max_sliding_window(array, k=7), [15, 15, 90, 90])
        self.assertEqual(max_sliding_window(array, k=2), [8, 10, 10, 9, 9, 15, 15, 90, 90])

    def test_reconstruct_queue(self):
        self.assertEqual([[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]],
                         reconstruct_queue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))

if __name__ == "__main__":

    unittest.main()
