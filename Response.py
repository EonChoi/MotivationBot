def handle_response(message) -> str:
    p_message= message.lower()
    if p_message == 'hello':
        return 'hey there!'
    if p_message == 'motivate me':
        return 'remember the bitterness you faced throughout your life, that should do it.'
