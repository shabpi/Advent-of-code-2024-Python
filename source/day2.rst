

DAY 2 
==========================


the input in `Day 2  <https://adventofcode.com/2024/day/2>`_ is a bunch of lines of numbers, called reports, the objective was to count how many reports are safe.
We need to check for every sequence if it is safe, for that we use the ``is_safe()`` function:


.. py:function:: day2.is_safe
    Returns a bool, declaring the safety of the sequence.
    
   :param sequence: a sequence of numbers
   :type kind: list[int]
   :return: if it's safe or not.
   :rtype: bool

For it to be safe it has to be only Decreasing or Increasing,
Additionally the difference between two consecutive numbers has to be atleast 1 and at most 3.

take a look at the code! 

.. code-block:: python

    length = len(sequence)
    if (length == 1): 
        return True
    if (int(sequence[0]) <= int(sequence[1])): ## Increasing case
        for i in range(0,length-1 ):
            if (int(sequence[i]) >= int(sequence[i+1]) or int(sequence[i+1]) - int(sequence[i]) > 3 ):
                return False
    else:
        for i in range(0,length -1): ## Decreasing case
            if (int(sequence[i]) <= int(sequence[i+1]) or int(sequence[i]) - int(sequence[i+1]) > 3 ):
                return False
    return True
    