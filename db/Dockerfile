FROM postgres:16
COPY init.sql /docker-entrypoint-initdb.d/init.sql
COPY README.md /README.md
COPY show-readme.sh /show-readme.sh
RUN sed -i 's/\r$//' /show-readme.sh && chmod +x /show-readme.sh
ENTRYPOINT ["/show-readme.sh"]
CMD ["postgres"]
EXPOSE 5432