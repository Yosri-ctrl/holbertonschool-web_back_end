#!/usr/bin/env python3
"""class SessionAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
from uuid import uuid4
 

class SessionAuth(Auth):
    """class SessionAuth that inherits from Auth
    for creating a new authentication mechanism
    """
    user_id_by_session_id = {}
    def create_session(self, user_id: str = None) -> str:
        """
        """
        if user_id is None or type(user_id) is not str:
            return None
        id = str(uuid4())
        self.user_id_by_session_id[id] = user_id
        return id
    
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)
