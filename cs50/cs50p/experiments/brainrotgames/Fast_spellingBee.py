# trying out the import functions and learning to apply them to this simple game loll
# im still slow at finding the choices and applying them for
import random
import time

# brainrot i could think of:
# some words
words = [
    "darren espanto", "rizzler", "gyatt", "fanum tax", "aura farm",
    "clipper", "lookxmaxx", "coughing baby", "gooner", "brainrot"
]

# using a list of tuples to map time thresholds to point values
def get_points(elapsed):
    thresholds = [(1.5, 3), (2.0, 2), (3.5, 1)]
    for limit, score in thresholds:
        if elapsed <= limit:
            return score
    # award 0 points if elapsed exceeds all thresholds
    return 0


def main():
    remaining = words.copy()
    score = 0

    while remaining:
        current = random.choice(remaining).lower()
        print(f"\nSpell this word: {current.upper()}")

        # using time.time() to measure how long the player takes to answer
        start = time.time()
        answer = input("Your answer: ").strip().lower()
        elapsed = time.time() - start

        if answer == current:
            points = get_points(elapsed)
            score += points
            remaining.remove(current)
            print(f"Correct! +{points} pts ({elapsed:.1f}s)")
        else:
            score -= 2
            print(f"Wrong! -2 pts ({elapsed:.1f}s)")

        print(f"Score: {score} | Words left: {len(remaining)}")

    print(f"\nGame over! Final score: {score}/{len(words) * 3}")


if __name__ == "__main__":
    main()

