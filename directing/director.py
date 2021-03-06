

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        gems = cast.get_first_actor("gems")
        rocks = cast.get_first_actor("rocks")
        velocity = self._keyboard_service.get_direction()
        auto_velocity = self._keyboard_service.get_auto_direction()
        robot.set_velocity(velocity)

        gems.set_velocity(auto_velocity)
        rocks.set_velocity(auto_velocity)





    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        gems = cast.get_actors("gems")
        rocks = cast.get_actors("rocks")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        for gem in gems :
            gem.move_down(max_x, max_y)
            gem.set_text("*")
            if robot.get_position().equals(gem.get_position()): # Add  or is_epired:
                cast.remove_actor("gems", gem)


        for rock in rocks:
            rock.move_down(max_x, max_y)
            rock.set_text("0")
            if robot.get_position().equals(rock.get_position()):
                cast.remove_actor("rocks", rock)
            
        # Remove any expired rocks and create new ones in their place, loop through and
        # remove them from Cast. 
        # 
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()