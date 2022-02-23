class Director:


    def __init__ (self, keyboard_service, video_service):
        self._keyboard_service = keyboard_service
        self._video_service = video_service


    def start_game(self, cast):

        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()