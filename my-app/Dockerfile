FROM nginx:alpine
COPY . /usr/share/nginx/html
COPY README.md /README.md
COPY show-readme.sh /show-readme.sh
RUN sed -i 's/\r$//' /show-readme.sh && chmod +x /show-readme.sh
ENTRYPOINT ["/show-readme.sh"]
CMD ["nginx", "-g", "daemon off;"]
EXPOSE 80