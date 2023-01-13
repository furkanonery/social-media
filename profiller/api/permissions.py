from rest_framework import permissions


class kendiProfiliYaDaReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user

class durumSahibiYaDaReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        print(obj,request.user)
        
        return obj.user_profil == request.user.Profil

# class fotoSahibiYaDaReadOnly(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):

#         if request.method in permissions.SAFE_METHODS:
#             return True

#         print(obj,request.user)
        
#         return obj.user_profil == request.user.Profil
