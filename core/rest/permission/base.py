from rest_framework.permissions import BasePermission



class IsOwnerOrAdminOrReadOnly(BasePermission):
    message = "You have not access this api.Access Denied!"

    def has_permission(self, request, view):
        if request.method in ['GET', 'POST', 'DELETE','PATCH', 'PUT']:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):

        if request.method == 'POST':
            if request.user.role == 'Admin':
                return True
            if request.user.role == 'Manager':
                return True
            return False
        
        if request.method == 'PATCH':
            if request.user.role == 'Admin':
                return True
            if request.user.role == 'Manager':
                return True
            return False
        
        if request.method == 'PUT':
            if request.user.role == 'Admin':
                return True
            if request.user.role == 'Manager':
                return True
            return False
        
        if request.method == 'DELETE':
            if request.user.role == 'Admin':
                return True
            if request.user.role == 'Manager':
                return False
            return False
    
        if request.method == 'GET':
            if request.user.role == 'Admin':
                return True
            if request.user.role == 'Manager':
                return True
            return False
             
        return False




