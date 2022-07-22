import re
from rest_framework.permissions import BasePermission

class IsCandidateUser(BasePermission):

    def has_permission(self, request, view):
        
        user = request.user

        return 