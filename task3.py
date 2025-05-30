# When a user enters a lesson page, we save the time of entry. When a user exits a lesson (or closes a tab, browser – in general, somehow breaks the connection with the server),
# we record the time of exiting the lesson. The time of each user's presence in the lesson is stored in the form of intervals. A dictionary containing three lists with timestamps
# (time in seconds) is passed to the function: lesson – the beginning and end of the lesson student – ​​intervals of student presence tutor – intervals of teacher presence The intervals
# are arranged as follows – it is always a list of an even number of elements. Even indices (starting with 0) indicate the time of entry to the lesson, and odd indices indicate the time
# of exit from the lesson. We need to write a function appearance that receives a dictionary with intervals as input and returns the total time of student and teacher presence in the lesson (in seconds).

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']

    # Convert flat lists into pairs (entry, exit)
    def entry_exit_pairs(presence_intervals):
        entry_exit_pairs = []

        for i in range(0, len(presence_intervals), 2):
            entry_time = presence_intervals[i]
            exit_time = presence_intervals[i + 1]

            # Calculate the effective presence time within the lesson bounds
            effective_start = max(entry_time, lesson_start)
            effective_end = min(exit_time, lesson_end)
            if effective_start < effective_end:  # Only count if there's a valid interval
                entry_exit_pairs.append((effective_start, effective_end))

        return entry_exit_pairs

    pupil_pairs = entry_exit_pairs(intervals['pupil'])
    tutor_pairs = entry_exit_pairs(intervals['tutor'])

    # Contains all seconds during which the pupil was in the lesson
    pupil_seconds = set()
    for start, end in pupil_pairs:
        pupil_seconds.update(range(start, end))

    # Contains all seconds during which the tutor was in the lesson
    tutor_seconds = set()
    for start, end in tutor_pairs:
        tutor_seconds.update(range(start, end))

    # Gives the set of seconds where both were present
    return len(pupil_seconds & tutor_seconds)


tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
