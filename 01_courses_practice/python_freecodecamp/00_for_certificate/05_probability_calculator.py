import random


class Hat:
    def __init__(self, **balls: dict[str:int]) -> None:
        self.contents: list = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls: int) -> list:
        if num_balls > len(self.contents):
            drawn_balls: list[str] = self.contents[:]
            self.contents: list = []
            return drawn_balls
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat: Hat, expected_balls: dict[str:int], num_balls_drawn: int, num_experiments: int) -> float:
    successful_experiments: int = 0

    for _ in range(num_experiments):
        hat_copy: Hat = Hat(**{ball: hat.contents.count(ball) for ball in set(hat.contents)})
        drawn_balls: list = hat_copy.draw(num_balls_drawn)

        drawn_count: dict[str:int] = {}

        for ball in drawn_balls:
            if ball in drawn_count:
                drawn_count[ball] += 1
            else:
                drawn_count[ball] = 1

        success: bool = True

        for ball, count in expected_balls.items():
            if drawn_count.get(ball, 0) < count:
                success = False
                break

        if success:
            successful_experiments += 1

    return successful_experiments / num_experiments


hat: Hat = Hat(black=6, red=4, green=3)
probability: float = experiment(hat=hat,
                                expected_balls={"red": 2, "green": 1},
                                num_balls_drawn=5,
                                num_experiments=2000)
print(probability)
