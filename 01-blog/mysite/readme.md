## Chapter 3: Extending your blog


### Adding a search engine with Solr and Haystack

Solr is a popular open-source search platform that offers full-text search, term boosting, hit highlighting, faceted search and dynamic clustering


Haystack is a django application that works as an abstaction layer for multiple search engines.


Each Solr core is a Lucene instance along with a Solr configuration, a data schema and other erquired configuration to use it.


1. Created a Solr Docker instance
2. Created a new core instance using `docker exec -it --user=solr blog_solr bin/solr create_core -c blog`
3. Installed django-haystack and pysolr.
4. Added haystack in INSTALLED_APPS
5. pym build_solr_schema > schema.xml
6. docker cp schema.xml blog_solr:/opt/solr/server/solr/blog/conf/schema.xml
7. pym rebuild_index
8. pym update_index --age=<num_hours to update less objects. you can setup a cron to keep the solr index updated.



#### Custom: Elasticsearch over Solr

docker run -d --name elas -v "$PWD/esdata":/usr/share/elasticsearch/data -p 9200:9200 elasticsearch

we need to use elasticsearch 1.7 apparently the latest version of elasticsearch doesn't work well with django haystack


