# syntax=docker/dockerfile:1
FROM postgres:16
EXPOSE 5432
COPY prisma /prisma
COPY docker/initdb/ /docker-entrypoint-initdb.d/
RUN chmod -R 0755 /docker-entrypoint-initdb.d
