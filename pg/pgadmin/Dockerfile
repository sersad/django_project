FROM dpage/pgadmin4:latest
USER root
COPY startup.sh .
RUN chmod +x ./startup.sh
#USER pgadmin
ENTRYPOINT ["./startup.sh"]