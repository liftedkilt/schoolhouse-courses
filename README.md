# Schoolhouse courses

Course packages for Schoolhouse, a mastery-based math tutor for families. Each directory is one course: data only (a manifest, a skill graph, problem templates and the wording of worked steps and hints), with no code.

| Course | What it covers | Needs first |
|---|---|---|
| [`ratio_percent`](ratio_percent) | Ratio and rate, percent, and money: tax, tips, discounts, simple interest (18 skills) | Arithmetic: decimals and dividing fractions |
| [`cooking`](cooking) | Kitchen measures, scaling recipes, cooking times and oven temperatures, cost and nutrition (29 skills) | Arithmetic: multiplying and dividing fractions; Ratio and percent, unit 1 |
| [`household`](household) | Shopping, pay, budgets, bills and the home, sewing and fabric, borrowing and saving (28 skills) | All of Ratio and percent |

Course files here are kept in step with the Schoolhouse project, and each new version is released automatically.

## Adding these courses to Schoolhouse

This repository is a **course source** for Schoolhouse: every push rebuilds its index, `courses.json`, at a link that never changes:

```
https://github.com/liftedkilt/schoolhouse-courses/releases/download/index/courses.json
```

1. In Schoolhouse, go to **Parents › Courses**.
2. Under **Browse courses**, open **Course sources**. A new Schoolhouse already lists the link above. If yours doesn't, paste it into the box and press **Add source**.
3. The courses appear under **Browse courses**. Press **Install** on the ones you want, or **Update to …** when a newer version is out. **Check for new courses** reads the index again. Schoolhouse checks each course file against the SHA-256 in the index, then checks the whole course, before installing anything.
4. Add the course to a child's learning path on their **Settings** tab. The "Home: cooking and household" track sets up arithmetic, ratio and percent, cooking and household in order.

Installing a newer version of a course updates it and keeps every child's progress.

### Without a course source

Each course version is also a [release](../../releases) (`course-<id>-v<version>`) with its `.zip` attached. Paste the zip's link into **Install from link** in Parents › Courses, or download it and use **Choose a course file…**.

### Running your own course source

Any https link to a `courses.json` works as a source, so you can publish your own courses the same way. Fork this repository, or copy its `.github` folder: on every push its workflow releases each new course version and rebuilds the index. The index lists, for each course: `id`, `version`, `title`, `summary`, `ages`, `units`, `skills`, `requires`, `url` (the zip's https link) and `sha256` (of that zip), under `{"format": 1, "name": ..., "courses": [...]}`.

## About the content

- Every problem is generated from a template and checked by code, so answers are always right. Explanations and hints are written for this project (`source: own`).
- Any real-world figure a problem uses (a tax rate, the 7.65% payroll tax, a daily value) is quoted in the problem, so a learner is never marked on knowing it.
- Nutrition problems are arithmetic only; they give no dietary advice.

## Licence

[PolyForm Noncommercial 1.0.0](LICENSE.md): free for families, schools and other noncommercial use.
