from pathlib import Path

from flask import Blueprint, render_template_string

# explorer_html = ExplorerGraphiQL().html(None)

examples_blueprint = Blueprint(
    'graphql-examples', __name__, url_prefix='/graphql-examples')


@examples_blueprint.route("")
def graphql_examples():
    base_path = Path("testing/graphql_queries")
    snippets = {}

    for category in ("queries", "mutations"):
        for file in (base_path / category).glob("*.graphql"):
            key = f"{category}/{file.name}"
            snippets[key] = file.read_text()

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>GraphQL Examples</title>
        <style>
            body { font-family: sans-serif; padding: 2em; background: #f4f4f4; }
            .card { background: #fff; margin-bottom: 2em; padding: 1em; border: 1px solid #ccc; border-radius: 8px; }
            pre { background: #eee; padding: 1em; overflow-x: auto; }
            button.copy { margin-top: 0.5em; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>GraphQL Example Queries & Mutations</h1>
        {% for name, content in snippets.items() %}
        <div class="card">
            <h3>{{ name }}</h3>
            <pre><code id="snippet-{{ loop.index }}">{{ content }}</code></pre>
            <button class="copy" onclick="copyToClipboard('snippet-{{ loop.index }}')">Copy</button>
        </div>
        {% endfor %}
        <script>
            function copyToClipboard(id) {
                const text = document.getElementById(id).innerText;
                navigator.clipboard.writeText(text).then(() => {
                    alert('Copied!');
                }, () => {
                    alert('Failed to copy');
                });
            }
        </script>
    </body>
    </html>
    """, snippets=snippets)
