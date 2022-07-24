FROM postgres:13-alpine
# USER 0:0
COPY startup.sh .
RUN chmod +x ./startup.sh

ENTRYPOINT ["./startup.sh"]