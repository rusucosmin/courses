<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
    <head>
      <link rel="stylesheet" type="text/css" href="display_style.css"/>
    </head>
    <body>
      <table class="main-section" border="1">
        <tr class="header-row">
          <th>Type</th>
          <th>Name</th>
          <th>Author</th>
          <th>Year</th>
        </tr>
        <xsl:for-each select="entries/entry">
          <tr class="data-row">
            <td class="type-data">
              <xsl:value-of select="type"/>
            </td>
            <td class="name-data">
              <xsl:choose>
                <xsl:when test="type='web link'">
                  <a rel="alternate" href="{name}"><xsl:value-of select="name"/></a>
                </xsl:when>
                <xsl:when test="type='image'">
                  imagine:
                  <img src="{name}"/><xsl:value-of select="name"/>
                </xsl:when>
                <xsl:otherwise>
                  <xsl:value-of select="name"/>
                </xsl:otherwise>
              </xsl:choose>
            </td>
            <td class="author-data">
              <xsl:value-of select="author"/>
            </td>
            <td class="year-data">
              <xsl:value-of select="year"/>
            </td>
          </tr>
        </xsl:for-each>
      </table>
    </body>
  </html>
</xsl:template>
</xsl:stylesheet>
