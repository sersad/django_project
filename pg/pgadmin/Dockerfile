FROM dpage/pgadmin4
USER root
COPY startup.sh .
RUN chmod +x ./startup.sh
#USER pgadmin
ENTRYPOINT ["./startup.sh"]