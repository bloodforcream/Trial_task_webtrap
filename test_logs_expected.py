logs_expected = {
    'test_api_route': [
        'INFO - GET - /api - {}', 'INFO - Starting process1',
        'INFO - Doing complicated calculations for process1',
        'INFO - Completed process1',
        'INFO - Starting process2',
        'INFO - Doing complicated calculations for process2',
        'INFO - Completed process2', 'INFO - Starting process3',
        'INFO - Doing complicated calculations for process3',
        'INFO - Completed process3\n'
    ],

    'test_api_route_post': [
        'INFO - POST - /api - {}',
        'ERROR - POST method not allowed\n'
    ],

    'test_api_route_invalid_1_parameter': [
        "INFO - GET - /api - {'invalid': '1'}",
        'ERROR - Got "invalid = 1" parameter\n'
    ],

    'test_api_route_invalid_path': [
        'INFO - GET - /notapipath - {}',
        'ERROR - Invalid path\n'
    ],

    'test_api_route_notawaiting_1_parameter': [
        "INFO - GET - /api - {'notawaiting': '1'}",
        'INFO - Starting process1',
        'INFO - Doing complicated calculations for process1',
        'INFO - Completed process1', 'INFO - Starting process2',
        'ERROR - Got "notawaiting=1" parameter', 'INFO - Closing process2\n'
    ],

    'test_process1': [
        'INFO - Starting process1',
        'INFO - Doing complicated calculations for process1',
        'INFO - Completed process1'
    ],

    'test_process2': [
        'INFO - Starting process2',
        'INFO - Doing complicated calculations for process2',
        'INFO - Completed process2'
    ],

    'test_process2_not_awaiting_1': [
        'INFO - Starting process2',
        'ERROR - Got "notawaiting=1" parameter',
        'INFO - Closing process2\n'
    ],

    'test_process3': [
        'INFO - Starting process3',
        'INFO - Doing complicated calculations for process3',
        'INFO - Completed process3\n'
    ]
}
