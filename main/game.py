import pygame
from enum import Enum


# ============================================================
# CONFIGURATION
# ============================================================

# Pygame runs at this FPS.
# This is NOT the snake movement speed.
FPS = 60

# Number of milliseconds between two snake movements
# at difficulty level 1.
BASE_MOVE_INTERVAL = 200

# Speed multiplier for each difficulty.
SPEED_MULTIPLIERS = {
    1: 1.00,
    2: 1.25,
    3: 1.50,
    4: 1.75,
}

# Points obtained when eating a fruit.
FRUIT_POINTS = {
    1: 4,
    2: 5,
    3: 6,
    4: 7,
}


# ============================================================
# GAME STATUS
# ============================================================

class GameStatus(Enum):
    """
    Represents the current state of a game.
    """

    WAITING = "waiting"
    RUNNING = "running"
    GAME_OVER = "game_over"


# ============================================================
# DIRECTIONS
# ============================================================

class Direction(Enum):
    """
    Possible directions of the snake.
    """

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


# ============================================================
# GAME
# ============================================================

class Game:
    """
    Main game controller.

    Responsibilities:
        - Store the configuration of the current game.
        - Manage the game state.
        - Process player input.
        - Control the movement timing.
        - Coordinate Snake, Map and Fruit.
        - Handle collisions.
        - Handle scoring.
        - Detect game over.
        - Reset the game.
        - Render the game using Pygame.

    The detailed implementation of Snake, Map and Fruit is
    handled by their respective modules.
    """

    def __init__(self, difficulty, map_id):
        """
        Create a new game.

        Parameters:
            difficulty (int):
                Difficulty level from 1 to 4.

            map_id (int):
                Selected map from 1 to 4.
        """

        # ----------------------------------------------------
        # Validate configuration
        # ----------------------------------------------------

        if difficulty not in SPEED_MULTIPLIERS:
            raise ValueError("Difficulty must be between 1 and 4.")

        if map_id not in (1, 2, 3, 4):
            raise ValueError("Map ID must be between 1 and 4.")

        # ----------------------------------------------------
        # Configuration
        # ----------------------------------------------------

        self.difficulty = difficulty
        self.map_id = map_id

        self.speed_multiplier = SPEED_MULTIPLIERS[difficulty]
        self.fruit_points = FRUIT_POINTS[difficulty]

        self.move_interval = (
            BASE_MOVE_INTERVAL / self.speed_multiplier
        )

        # ----------------------------------------------------
        # Dynamic state
        # ----------------------------------------------------

        self.direction = None
        self.score = 0
        self.status = GameStatus.WAITING

        # ----------------------------------------------------
        # Timing
        # ----------------------------------------------------

        self.move_timer = 0

        # ----------------------------------------------------
        # Pygame
        # ----------------------------------------------------

        self.clock = pygame.time.Clock()

        # These will be initialized by initialize_game().
        self.snake = None
        self.map = None
        self.fruit = None

        self.initialize_game()

    # ========================================================
    # INITIALIZATION
    # ========================================================

    def initialize_game(self):
        """
        Initialize all objects required for a new game.

        This method assumes that the Snake, Map and Fruit
        classes will be supplied by the other modules.
        """

        # ----------------------------------------------------
        # Map
        # ----------------------------------------------------

        # TODO:
        # Replace this with the actual Map implementation.
        #
        # Example:
        #
        # self.map = Map(self.map_id)

        self.map = None

        # ----------------------------------------------------
        # Snake
        # ----------------------------------------------------

        # TODO:
        # Replace this with the actual Snake implementation.
        #
        # Example:
        #
        # start_position = self.map.get_center()
        # self.snake = Snake(start_position)

        self.snake = None

        # ----------------------------------------------------
        # Fruit
        # ----------------------------------------------------

        # TODO:
        # Replace this with the actual Fruit implementation.
        #
        # Example:
        #
        # self.fruit = Fruit()
        # self.spawn_fruit()

        self.fruit = None

        # ----------------------------------------------------
        # Game state
        # ----------------------------------------------------

        self.direction = None
        self.score = 0
        self.status = GameStatus.WAITING
        self.move_timer = 0

    # ========================================================
    # EVENT HANDLING
    # ========================================================

    def handle_event(self, event):
        """
        Process one Pygame event.

        The Game receives Pygame input and converts it into
        game-level actions.
        """

        if event.type == pygame.QUIT:
            return "quit"

        if event.type == pygame.KEYDOWN:

            # ----------------------------------------------
            # Direction controls
            # ----------------------------------------------

            if event.key == pygame.K_UP:
                self.change_direction(Direction.UP)

            elif event.key == pygame.K_DOWN:
                self.change_direction(Direction.DOWN)

            elif event.key == pygame.K_LEFT:
                self.change_direction(Direction.LEFT)

            elif event.key == pygame.K_RIGHT:
                self.change_direction(Direction.RIGHT)

            # ----------------------------------------------
            # Restart after game over
            # ----------------------------------------------

            elif (
                event.key == pygame.K_r
                and self.status == GameStatus.GAME_OVER
            ):
                self.reset()

            # ----------------------------------------------
            # Return to menu
            # ----------------------------------------------

            elif (
                event.key == pygame.K_ESCAPE
                and self.status == GameStatus.GAME_OVER
            ):
                return "menu"

        return None

    # ========================================================
    # DIRECTION
    # ========================================================

    def change_direction(self, new_direction):
        """
        Try to change the direction of the snake.

        A direction change is rejected if it would cause
        an immediate 180-degree turn.

        The first valid direction also changes the state
        from WAITING to RUNNING.
        """

        # No direction has been selected yet.
        if self.direction is None:

            self.direction = new_direction

            if self.status == GameStatus.WAITING:
                self.status = GameStatus.RUNNING

            return True

        # ----------------------------------------------------
        # Prevent immediate 180-degree turns
        # ----------------------------------------------------

        current_dx, current_dy = self.direction.value
        new_dx, new_dy = new_direction.value

        if (
            current_dx + new_dx == 0
            and current_dy + new_dy == 0
        ):
            return False

        self.direction = new_direction

        return True

    # ========================================================
    # UPDATE
    # ========================================================

    def update(self, delta_time):
        """
        Update the game.

        delta_time:
            Time elapsed since the previous frame in
            milliseconds.
        """

        if self.status != GameStatus.RUNNING:
            return

        self.move_timer += delta_time

        if self.move_timer >= self.move_interval:

            # Reset timer.
            #
            # Using modulo prevents us from losing time when
            # a frame takes slightly longer than expected.
            self.move_timer %= self.move_interval

            self.move_snake()

    # ========================================================
    # MOVE SNAKE
    # ========================================================

    def move_snake(self):
        """
        Perform one complete snake movement.

        The order is:

            1. Calculate next position
            2. Apply map rules
            3. Check collisions
            4. Move snake
            5. Check fruit
            6. Update score / growth
            7. Generate new fruit
        """

        if self.snake is None:
            return

        if self.direction is None:
            return

        # ----------------------------------------------------
        # 1. Current head
        # ----------------------------------------------------

        current_head = self.snake.get_head()

        dx, dy = self.direction.value

        next_position = (
            current_head[0] + dx,
            current_head[1] + dy
        )

        # ----------------------------------------------------
        # 2. Apply map rules
        # ----------------------------------------------------

        next_position = self.apply_map_rules(next_position)

        # If the map rules already resulted in a collision,
        # the game is over.
        if next_position is None:
            self.game_over()
            return

        # ----------------------------------------------------
        # 3. Collision detection
        # ----------------------------------------------------

        if self.check_collision(next_position):
            self.game_over()
            return

        # ----------------------------------------------------
        # 4. Check whether fruit is eaten
        # ----------------------------------------------------

        eating_fruit = self.is_fruit_at(next_position)

        # ----------------------------------------------------
        # 5. Move snake
        # ----------------------------------------------------

        self.snake.move(next_position, grow=eating_fruit)

        # ----------------------------------------------------
        # 6. Fruit
        # ----------------------------------------------------

        if eating_fruit:

            self.score += self.fruit_points

            self.spawn_fruit()

    # ========================================================
    # MAP RULES
    # ========================================================

    def apply_map_rules(self, position):
        """
        Apply the rules of the selected map.

        For a free-passage map, the position wraps around
        the edges.

        For a bordered map, leaving the map returns None.

        For maps with obstacles, obstacles are handled as
        collisions.
        """

        # TODO:
        # Replace this section with the actual Map API.

        if self.map is None:
            return position

        x, y = position

        width = self.map.get_width()
        height = self.map.get_height()

        # ----------------------------------------------------
        # Position outside map
        # ----------------------------------------------------

        if x < 0 or x >= width or y < 0 or y >= height:

            if self.map.wraps_edges():

                x %= width
                y %= height

                return x, y

            else:
                return None

        # ----------------------------------------------------
        # Position inside map
        # ----------------------------------------------------

        if self.map.is_obstacle(position):
            return None

        return position

    # ========================================================
    # COLLISIONS
    # ========================================================

    def check_collision(self, position):
        """
        Check whether the next position causes a collision.

        Checks:
            - Snake's own body
            - Map obstacles

        The map boundary is handled by apply_map_rules().
        """

        # ----------------------------------------------------
        # Map collision
        # ----------------------------------------------------

        if self.map is not None:

            if self.map.is_obstacle(position):
                return True

        # ----------------------------------------------------
        # Snake collision
        # ----------------------------------------------------

        body = self.snake.get_body()

        # The tail is normally going to disappear during
        # this movement.
        #
        # Therefore, moving onto the current tail is allowed
        # when the snake is not eating a fruit.
        #
        # However, if the fruit is on the next position,
        # the tail remains and the complete body must be
        # considered.

        eating_fruit = self.is_fruit_at(position)

        if eating_fruit:
            collision_body = body
        else:
            collision_body = body[:-1]

        if position in collision_body:
            return True

        return False

    # ========================================================
    # FRUIT
    # ========================================================

    def is_fruit_at(self, position):
        """
        Check whether the fruit is located at position.
        """

        if self.fruit is None:
            return False

        return self.fruit.get_position() == position

    def spawn_fruit(self):
        """
        Generate a new fruit on a valid position.

        The fruit must not be:
            - on the snake
            - on an obstacle
            - outside the map
        """

        if self.fruit is None:
            return

        if self.map is None:
            return

        snake_body = self.snake.get_body()

        # Ask the Fruit module to find a valid position.
        #
        # The exact implementation can be changed once the
        # Fruit branch is integrated.

        self.fruit.spawn(
            map=self.map,
            occupied_positions=snake_body
        )

    # ========================================================
    # GAME OVER
    # ========================================================

    def game_over(self):
        """
        End the current game.
        """

        if self.status == GameStatus.GAME_OVER:
            return

        self.status = GameStatus.GAME_OVER

        # The score is intentionally not deleted.
        # The scoreboard module can retrieve it using
        # get_score().

    # ========================================================
    # RESET
    # ========================================================

    def reset(self):
        """
        Reset the current game using the same configuration.

        Difficulty and map remain unchanged.
        """

        self.initialize_game()

    # ========================================================
    # GETTERS
    # ========================================================

    def get_score(self):
        """
        Return the current score.
        """

        return self.score

    def get_status(self):
        """
        Return the current game status.
        """

        return self.status

    def get_direction(self):
        """
        Return the current direction.
        """

        return self.direction

    def is_running(self):
        """
        Return True if the game is currently running.
        """

        return self.status == GameStatus.RUNNING

    def is_game_over(self):
        """
        Return True if the game has ended.
        """

        return self.status == GameStatus.GAME_OVER

    # ========================================================
    # DRAW
    # ========================================================

    def draw(self, screen):
        """
        Draw the current game state.

        Snake, Map and Fruit are responsible for drawing
        themselves.
        """

        if self.map is not None:
            self.map.draw(screen)

        if self.fruit is not None:
            self.fruit.draw(screen)

        if self.snake is not None:
            self.snake.draw(screen)

        # The score can later be handled by the
        # menu-scoreboard module.
        #
        # For now, Game only exposes the score through
        # get_score().

    # ========================================================
    # MAIN GAME LOOP
    # ========================================================

    def run(self, screen):
        """
        Run the Pygame loop for this game.

        Returns:
            "quit"  -> application should close
            "menu"  -> return to main menu
        """

        running = True

        while running:

            # ------------------------------------------------
            # Calculate elapsed time
            # ------------------------------------------------

            delta_time = self.clock.tick(FPS)

            # ------------------------------------------------
            # Events
            # ------------------------------------------------

            for event in pygame.event.get():

                result = self.handle_event(event)

                if result == "quit":
                    return "quit"

                if result == "menu":
                    return "menu"

            # ------------------------------------------------
            # Update
            # ------------------------------------------------

            self.update(delta_time)

            # ------------------------------------------------
            # Draw
            # ------------------------------------------------

            self.draw(screen)

            pygame.display.flip()

        return "quit"