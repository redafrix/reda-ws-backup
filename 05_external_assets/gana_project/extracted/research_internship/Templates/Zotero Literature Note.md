---
citekey: {{citekey}}
status: unread
source: zotero
tags:
  - literature-note
---

# {{title}}

## Citation
{{bibliography}}

## Metadata
- Citekey: `{{citekey}}`
- Type: {{itemType}}
- Authors: {% if authors %}{{authors}}{% elif creators and creators.length > 0 %}{% for creator in creators %}{% if creator.name %}{{creator.name}}{% else %}{{creator.firstName}} {{creator.lastName}}{% endif %}{% if not loop.last %}, {% endif %}{% endfor %}{% endif %}
- Year: {% if date %}{{date | format("YYYY")}}{% endif %}
- Zotero: [Open item]({{desktopURI}})
{% if DOI %}- DOI: {{DOI}}
{% endif %}{% if pdfZoteroLink %}- PDF: {{pdfZoteroLink}}
{% endif %}{% if hashTags %}- Tags: {{hashTags}}
{% endif %}

{% if abstractNote %}
## Abstract
{{abstractNote}}
{% endif %}

{% persist "summary" %}
## Summary
- Research question:
- Core claim:
- Method:
- Key findings:
- Relevance to my work:
{% endpersist %}

{% persist "review" %}
## Literature Review Notes
- Strengths:
- Weaknesses:
- Useful quotes or claims:
- Follow-up questions:
{% endpersist %}

{% if markdownNotes %}
{% persist "zotero-notes" %}
## Zotero Notes
{{markdownNotes}}
{% endpersist %}
{% endif %}

{% persist "annotations" %}
{% set newAnnotations = annotations | filterby("date", "dateafter", lastImportDate) %}
{% if newAnnotations.length > 0 %}
## Imported Annotations
### {{importDate | format("YYYY-MM-DD HH:mm")}}
{% for annotation in newAnnotations %}
#### Page {{annotation.pageLabel or annotation.page}}
{% if annotation.annotatedText %}
> {{annotation.annotatedText}}
{% endif %}
{% if annotation.imageRelativePath %}
![[{{annotation.imageRelativePath}}]]
{% endif %}
{% if annotation.comment %}
Comment: {{annotation.comment}}
{% endif %}
Type: {{annotation.type}}{% if annotation.colorCategory %} | Color: {{annotation.colorCategory}}{% endif %} | [Open in Zotero]({{annotation.attachment.desktopURI.replace("select", "open-pdf")}}?page={{annotation.pageLabel}}&annotation={{annotation.id}})

{% endfor %}
{% endif %}
{% endpersist %}
