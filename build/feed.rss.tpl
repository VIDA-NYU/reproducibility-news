<?xml version="1.0"?>
<rss version="2.0">
  <channel>
    <title>Reproducibility News Feed</title>
    <link>http://reproduciblescience.org/</link>
{% for item in items %}
    <item>
      <title>{{ item.title }}</title>
      <link>{{ item.link }}</link>
      <pubDate>{{ item.date }}</pubDate>
      <description>
        {{ item.description }}
      </description>
    </item>
{% endfor %}
  </channel>
</rss>
