# AST Group website

[Live website](https://larslindemann1989.github.io/ast-lab/) · [Edit About the group](https://github.com/LarsLindemann1989/ast-lab/edit/main/content/about.md) · [Edit research areas](https://github.com/LarsLindemann1989/ast-lab/tree/main/content/research)

The Algorithmic Systems Theory Group at ETH Zürich. This is the GitHub Pages version of the selected website design: ETH colours and logo, a flexible research grid, people, and publications grouped by year.

**Start with [About the group](content/about.md) or a [research area](content/research/).** You can edit the text in your web browser. No software installation is needed for ordinary updates.

## Change text in GitHub

1. Open the file using one of the links below.
2. Click the **pencil icon** (Edit this file).
3. Change the text. Keep the settings between the two `---` lines at the top; ordinary paragraphs go below the second line.
4. Click **Commit changes**, add a short description, and commit to `main`.
5. Open the repository's **Actions** tab. Once “Build and publish group website” is green, refresh the live site.

GitHub's **Preview** tab previews the Markdown text. The live website uses the site's design. Publication normally follows the successful workflow within a few minutes. If a build fails, the last successfully published website remains online.

For a change you want someone to review first, select **Create a new branch** when committing and open a pull request. It is checked automatically but only published after merging into `main`.

| What you want to change | File |
| --- | --- |
| Main title, introductory paragraph, selected papers | [content/home.md](content/home.md) |
| About the group | [content/about.md](content/about.md) |
| Research page title and introduction | [content/research.md](content/research.md) |
| Research areas, summaries, and detailed text | [content/research/](content/research/) |
| News | [content/news/](content/news/) |
| Team names, roles, interests, links, photographs | [data/people.yaml](data/people.yaml) |
| People page title and description | [content/people.md](content/people.md) |
| Alumni | [data/alumni.yaml](data/alumni.yaml) |
| Biography and awards | [content/lars-lindemann.md](content/lars-lindemann.md) |
| Teaching introduction and student projects | [content/teaching.md](content/teaching.md) |
| Course list | [data/courses.yaml](data/courses.yaml) |
| Contact and recruitment text | [content/contact.md](content/contact.md) |
| Email, address, group name, and Scholar link | [site.yaml](site.yaml) |
| Publications | [data/publications.json](data/publications.json) |
| Publication page title and archive note | [content/publications.md](content/publications.md) |
| Imprint and privacy text | [content/imprint.md](content/imprint.md), [content/privacy.md](content/privacy.md) |
| Pictures | [static/assets/](static/assets/) |

## Write paragraphs, headings, and links

Below the second `---` line, write ordinary paragraphs with a blank line between them:

```markdown
Our group studies the foundations of safe autonomous systems.

### Current directions

We connect **formal methods** with learning and control.

- First research question
- Second research question

Read our [publication archive](publications.html).
```

In research descriptions, use `###` for subsection headings. Elsewhere, use `##` for sections. The page already supplies its main heading, so do not add a `#` heading.

The settings above the second `---` line use YAML. Keep field names unchanged. For titles or short descriptions containing a colon, use quotes, for example `title: 'Robotics: theory and practice'`. Keep list entries indented consistently. Long descriptions can use `summary: >-` followed by indented lines.

## Add a research area

There is **no limit of three research areas**. One file supplies both the homepage card and the research page section.

1. Open [templates/research-area.md](templates/research-area.md), click **Code** or **Raw**, and copy its full text, including the settings between `---` lines.
2. In [content/research/](content/research/), select **Add file → Create new file**.
3. Name it something like `robot-learning.md` and paste the template.
4. Set a unique `id`, a `title`, a short `summary`, and an `order` number. Lower numbers appear first. Existing areas use 10, 20, and 30.
5. Write the full description below the second `---`. Add as many paragraphs and subsections as you need.
6. Commit the new file.

The homepage grid, research index, and detailed sections update together. Remove a file to remove its area from both pages. Reorder areas by changing `order`. Keep the `id` unchanged when renaming a title so existing links to that section continue to work.

Optional fields:

- `image`: e.g. `assets/robot-learning.jpg`; leave `''` for no image.
- `image_alt`: describe what the image shows.
- `image_credit` and `image_source`: caption and source URL.
- `tags`: a list of topic labels, or `[]`.
- `papers`: IDs copied from `data/publications.json`, or `[]`.

## Upload pictures

In `static/assets/`, choose **Add file → Upload files**. Upload a reasonably sized JPG, PNG, or SVG. Use a short filename with hyphens and no spaces. Refer to it in content as `assets/your-picture.jpg` (omit `static/`). Commit the image before adding its reference, or include both in one pull request.

A picture inside a description uses `![Descriptive alternative text](assets/your-picture.jpg)`. Preserve original image credits and the ETH logo.

## Add news and people

Copy an existing file in `content/news/`, give it a new filename, update its date, title, URL, and paragraph, then commit. News appears newest first. Dates use `YYYY-MM-DD`.

For people, copy an existing entry in `data/people.yaml` and change its fields. The list order controls display order; `group` controls the People page section. Set `image: null` if there is no portrait. `featured_people` in `content/home.md` controls how many people from the beginning of the list appear on the homepage.

## Update publications

Each object in `data/publications.json` is one displayed record. Copy an existing object of the same `type` and give it a unique `id`. Keep commas between objects. Valid types are `journal`, `conference`, `preprint`, and `thesis`.

Year grouping, title sorting, search, type filters, and the BibTeX download are regenerated automatically. Add a record's ID to `selected_publications` in `content/home.md` to feature it, or to a research area's `papers` to associate it with that area.

The migrated archive has **109 records: 108 paper entries and one thesis**. Google Scholar blocked the original lookup, so the archive was assembled from DBLP, arXiv, and publisher records. It is **not yet reconciled against a Google Scholar export**. See [source-notes.txt](source-notes.txt) and [data/provenance/](data/provenance/). A Scholar CSV/BibTeX export is needed before claiming completeness. Publications are not automatically scraped from Scholar.

## First-time GitHub Pages setup

These steps are needed once, by the repository owner:

1. Create a **public** repository, for example `ast-lab`, with default branch `main`.
2. Add this package's source files at the repository root, including `.github/workflows/pages.yml`. Upload the extracted files, not the ZIP file. The `.github` folder may be hidden in your file browser; make sure it is included.
3. Open **Settings → Pages → Build and deployment → Source** and choose **GitHub Actions**.
4. Open **Actions → Build and publish group website → Run workflow** on `main`.
5. After the deployment succeeds, open the website URL in **Settings → Pages** or the `github-pages` environment.

A project repository named `ast-lab` normally publishes at `https://YOUR-ACCOUNT.github.io/ast-lab/`. This is an example, not an already-created site URL. The repository contents and the website are public. The included workflow uses GitHub's built-in token; no personal access token or extra secret needs to be saved in this repository.

The footer's **Edit this page** link is generated automatically from the repository name during GitHub builds. On Research it opens the research content folder; on People and Publications it opens the corresponding data file. Only repository collaborators with write access can commit directly.

If Actions shows an error, open the failed run and its red step. Missing pictures, broken internal links, invalid YAML, and unknown publication IDs are checked before publishing. Fix the referenced source file and commit again. To undo a text edit, the file's **History** lets you view/copy its previous version back into the editor.

## Build locally (optional)

Requires Python 3.12 or newer. Ordinary browser edits do not need these commands.

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python build.py
python check_site.py
python -m http.server --directory dist 8000
```

Open `http://localhost:8000`. On Windows, activate with `.venv\Scripts\activate` instead. `dist/` is regenerated on every build; edit `content/`, `data/`, and `static/` instead. All site links are relative so the build works under either a repository path or a custom domain.

## Design and future AEM move

`static/styles.css` contains the shared design. The official ETH palette and unmodified ETH logo are retained. Ordinary content edits do not require CSS or Python changes.

This version is a static GitHub Pages website. A future move into ETH AEM uses ETH's supported templates and components; the text and assets can be reused, but this is not an AEM theme package. The original Google Site and private design preview remain separate.

References: [GitHub file editor](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files) · [GitHub Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) · [ETH palette](https://ethz.ch/staffnet/en/service/communication/corporate-design/farbe.html) · [ETH logo](https://ethz.ch/staffnet/en/service/communication/corporate-design/logo.html).
