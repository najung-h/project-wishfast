from .base import *
import environ
import os

# environ 초기화
env = environ.Env()

DEBUG = True # temp #  개발 끝나면 False로 변경 예정

# .env 파일 로드
environ.Env.read_env(os.path.join(BASE_DIR, ".env.prod"))

# .env 파일에서 도메인 목록을 읽어옴
ALLOWED_HOSTS = [h.strip() for h in env("DJANGO_ALLOWED_HOSTS").split(",")]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ["DB_USER"],
        "PASSWORD": os.environ["DB_PASSWORD"],
        "HOST": os.environ["DB_HOST"],
        "PORT": os.getenv("DB_PORT", "3306"),
        "OPTIONS": {"charset": "utf8mb4"},
        "CONN_MAX_AGE": int(os.getenv("DB_CONN_MAX_AGE", "60")),
    }
}

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)


# Django 로깅: 콘솔 + 파일(7일 보관)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "[{asctime}] {levelname} {name}:{lineno} | {message}", "style": "{"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "verbose"},
        "file_rotating": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": str(LOG_DIR / "django.log"),
            "when": "D",
            "interval": 1,
            "backupCount": 7,
            "encoding": "utf-8",
            "formatter": "verbose",
        },
    },
    "root": {"handlers": ["console", "file_rotating"], "level": "INFO"},
    "loggers": {
        "django": {"handlers": ["console", "file_rotating"], "level": "WARNING", "propagate": False},
        "django.request": {"handlers": ["console", "file_rotating"], "level": "ERROR", "propagate": False},
    },
}


# HTTPS를 위한 보안 설정 활성화
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https") # 프록시 환경에서 HTTPS를 인식


# 신뢰된 오리진 목록 
CSRF_TRUSTED_ORIGINS = [
    "https://runornot.site",
    "https://www.runornot.site",   # www 쓰면 함께
]

# 세션/CSRF 쿠키를 HTTPS 연결에서만 전송 
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


# 실제 클라이언트가 HTTPS로 전송했음을 장고에게 알려주는 힌트 
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # 프록시가 이 헤더를 넣어줄 때