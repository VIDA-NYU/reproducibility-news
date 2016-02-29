<?xml version="1.0"?>
<rss version="2.0">
  <channel>
    <title>Reproducibility News Feed</title>
    <link>http://reproduciblescience.org/</link>
    <description>A feed that shows recent news about scientific reproducibility efforts.</description>
{% for item in items %}
    <item>
      <title>{{ item.title }}</title>
      <link>{{ item.link }}</link>
      <pubDate>{{ item.date }}</pubDate>
      <description>
        {{ item.description }}
      </description>
{% for tag in item.tags %}
      <category>{{ tag }}</category>
{% endfor %}
    </item>
{% endfor %}
  </channel>
</rss>
