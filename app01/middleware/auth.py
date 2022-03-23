from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 排除那些不需要登录就能访问的页面
        if request.path_info in ["/login/", "/image/code/"]:
            return
        info_dict = request.session.get("info")
        if info_dict:
            return
        return redirect('/login/')
