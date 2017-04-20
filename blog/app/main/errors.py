# coding=utf-8

from flask import render_template, jsonify, request
from . import main


@main.app_errorhandler(403)
def forbidden(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        return jsonify(status=403, message='Forbidden')
    return render_template('main/403.html'), 403


@main.app_errorhandler(404)
def page_not_found(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        return jsonify(stasus=404, message='Not Found')
    return render_template('main/404.html'), 404


@main.app_errorhandler(500)
def server_internal_error(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        return jsonify(status=500, message=u'接口错误')
    return render_template('main/500.html'), 500
