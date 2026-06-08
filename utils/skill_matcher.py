# -------- SKILL DATABASE --------

role_skills = {

    "IT": [
        "python",
        "java",
        "sql",
        "machine learning",
        "data analysis",
        "html",
        "css",
        "javascript",
        "cloud",
        "aws",
        "git"
    ],

    "Finance": [
        "accounting",
        "excel",
        "financial analysis",
        "tax",
        "audit",
        "budgeting",
        "forecasting"
    ],

    "Healthcare": [
        "patient care",
        "clinical skills",
        "nursing",
        "medical knowledge",
        "diagnosis",
        "treatment"
    ],

    "Sales & Marketing": [
        "sales",
        "marketing",
        "communication",
        "negotiation",
        "seo",
        "branding",
        "lead generation"
    ]
}


def extract_skills(
    text,
    sector
):

    text = text.lower()

    skills = role_skills.get(
        sector,
        []
    )

    found = []

    for skill in skills:

        if skill.lower() in text:

            found.append(skill)

    return found


def match_skills(
    text,
    sector
):

    extracted = extract_skills(
        text,
        sector
    )

    required = role_skills.get(
        sector,
        []
    )

    missing = list(
        set(required)
        -
        set(extracted)
    )

    missing = missing[:5]

    return extracted, missing


def suggest_improvements(
    missing_skills
):

    suggestions = []

    skill_guidance = {

        "python":
        "Practice Python through real projects and APIs.",

        "java":
        "Build backend applications using Java and Spring Boot.",

        "sql":
        "Practice advanced SQL queries and database design.",

        "machine learning":
        "Build ML projects using scikit-learn and TensorFlow.",

        "html":
        "Create responsive websites using HTML5.",

        "css":
        "Learn Flexbox, Grid and responsive design.",

        "javascript":
        "Build dynamic web applications using JavaScript.",

        "aws":
        "Learn AWS EC2, S3 and cloud deployment.",

        "git":
        "Use GitHub regularly and practice version control.",

        "excel":
        "Practice Pivot Tables and advanced Excel formulas.",

        "financial analysis":
        "Learn financial modeling and reporting.",

        "marketing":
        "Learn digital marketing and campaign analytics.",

        "seo":
        "Practice website optimization and keyword analysis.",

        "communication":
        "Improve through presentations and mock interviews."
    }

    for skill in missing_skills:

        if skill in skill_guidance:

            suggestions.append(
                skill_guidance[skill]
            )

        else:

            suggestions.append(
                f"Gain practical experience in {skill}"
            )

    return suggestions