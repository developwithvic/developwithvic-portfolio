from flask import Blueprint, render_template, request
import os
import markdown
import frontmatter


main = Blueprint(
    "main",
    __name__
)


@main.route("/")
def home():

    return render_template(
        "index.html"
    )



@main.route("/about")
def about():

    return render_template(
        "about.html"
    )



@main.route("/blog")
def blog():

    search_query = request.args.get(
        "search",
        ""
    ).lower()


    posts = []

    blog_folder = "content/blog"


    for filename in os.listdir(blog_folder):

        if filename.endswith(".md"):

            filepath = os.path.join(
                blog_folder,
                filename
            )


            post = frontmatter.load(
                filepath
            )


            title = post.metadata.get(
                "title"
            )


            category = post.metadata.get(
                "category"
            )


            content = post.content


            # Search filter

            if search_query:

                if (
                    search_query not in title.lower()
                    and
                    search_query not in content.lower()
                    and
                    search_query not in category.lower()
                ):

                    continue



            posts.append({

                "title": title,

                "date": post.metadata.get(
                    "date"
                ),

                "category": category,

                "slug": filename.replace(
                    ".md",
                    ""
                ),

                "content": markdown.markdown(
                    content
                )

            })


    return render_template(
        "blog/index.html",
        posts=posts
    )


@main.route("/blog/<post_name>")
def blog_post(post_name):

    filepath = os.path.join(
        "content/blog",
        post_name + ".md"
    )


    if os.path.exists(filepath):

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()


        html_content = markdown.markdown(
            content
        )


        return render_template(
            "blog/post.html",
            content=html_content
        )


    return "Post not found", 404