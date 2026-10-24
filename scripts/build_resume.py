"""Build the checked-in resume: python3 -m pip install -r scripts/requirements-resume.txt
Run python3 scripts/build_resume.py from any directory. No browser or external assets needed.
"""
from pathlib import Path
import reportlab
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import letter

FONT_DIR = Path(reportlab.__file__).parent / 'fonts'
pdfmetrics.registerFont(TTFont('Resume', str(FONT_DIR / 'Vera.ttf')))
pdfmetrics.registerFont(TTFont('Resume-Bold', str(FONT_DIR / 'VeraBd.ttf')))
pdfmetrics.registerFontFamily('Resume', normal='Resume', bold='Resume-Bold', italic='Resume', boldItalic='Resume-Bold')

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/Dioscar-Rodriguez-Resume.pdf'
OUT.parent.mkdir(exist_ok=True)
c = canvas.Canvas(str(OUT), pagesize=letter, invariant=1)
c.setTitle('Dioscar Rodriguez | Full-Stack Software Engineer')
c.setAuthor('Dioscar Rodriguez')
W, H = letter
LEFT, RIGHT = 42, 570
y = 0

def para(text, size=9.5, leading=13, indent=0, color='#222222', bold=False):
    global y
    style = ParagraphStyle('body', fontName='Resume-Bold' if bold else 'Resume', fontSize=size, leading=leading, textColor=HexColor(color))
    p = Paragraph(text, style)
    _, height = p.wrap(RIGHT-LEFT-indent, H)
    if y-height < 49:
        raise ValueError(f'Resume content exceeds page: {text[:60]}')
    p.drawOn(c, LEFT+indent, y-height)
    y -= height

def gap(n=8):
    global y
    y -= n

def section(title):
    global y
    gap(15)
    para(title.upper(), 9, 12, bold=True)
    y -= 5
    c.setStrokeColor(HexColor('#cccccc')); c.setLineWidth(.5)
    c.line(LEFT, y, RIGHT, y)
    y -= 10

def role(title, company, dates):
    global y
    c.setFont('Resume', 9); c.setFillColor(HexColor('#444444'))
    c.drawRightString(RIGHT, y-11, dates)
    para(title, 11, 14, bold=True)
    para(company, 9.5, 13, color='#555555')
    gap(7)

def bullet(text):
    global y
    c.setFont('Resume', 10); c.setFillColor(HexColor('#111111'))
    c.drawString(LEFT+2, y-10, '\u2022')
    para(text, indent=14)
    gap(5)

def footer(page):
    c.setFont('Resume', 8); c.setFillColor(HexColor('#666666'))
    c.drawString(LEFT, 29, 'Dioscar Rodriguez | Full-Stack Software Engineer')
    c.drawRightString(RIGHT, 29, f'{page} / 2')

# Reference-inspired split header; the body stays in a single reading column.
y = 751
para('Dioscar Rodriguez', 22, 26, bold=True)
para('Full-Stack Software Engineer', 11, 16, bold=True)
gap(6)
para('Cicero, NY | (347) 200-9415', 9, 13)
para('<link href="mailto:dioscarr@gmail.com">dioscarr@gmail.com</link> | <link href="https://github.com/dioscarr">github.com/dioscarr</link>', 9, 13)
c.setFont('Resume-Bold', 8.5); c.drawRightString(RIGHT, 746, "Bachelor's in Computer Information Systems")
c.setFont('Resume', 8.5); c.drawRightString(RIGHT, 732, 'New York City College of Technology | 2014')
section('Profile')
para('Full-stack software engineer with 12+ years of experience building enterprise web applications, modernizing legacy systems, and delivering database-backed business workflows. Core strengths in C#, .NET, Blazor, React, and SQL Server, with hands-on work in role-based access, API integrations, and AI-assisted development. Bilingual in English and Spanish.')
section('Professional experience')
role('Programmer', 'McNeil and Company', 'Jul 2020 - Present')
bullet('Modernize an enterprise e-learning platform serving approximately <b>108,000 users</b>, migrating ASP.NET WebForms / VB.NET functionality to <b>C#, .NET, and Blazor</b> while preserving business rules and learning records.')
bullet('Migrate Sybase data and inline SQL into <b>SQL Server</b>, stored procedures, table-valued functions, Entity Framework, and reusable C# service layers.')
bullet('Build role-scoped workflows for students, officers, and administrators, including assignments, user management, course history, certificates, documents, and reporting.')
bullet('Integrate <b>xAPI / Tin Can</b> content and an on-premises Veracity learning record store; translate learning statements into progress, quiz results, and completion records.')
bullet('Implement authentication and authorization with <b>Auth0</b>, claims, and role-based policies; support real-time notifications with <b>SignalR</b> and application diagnostics with Serilog and Seq.')
bullet('Develop customer portal workflows for insureds, brokers, carriers, and administrators, including documents, billing views, user management, and reusable Tailwind theme tokens.')
gap(7)
role('Lead Software Engineer', 'Third Mind Inc', 'May 2016 - Mar 2020')
bullet('Led full-stack development of web, CRM, extranet, and document automation applications using <b>ASP.NET Core, React, Entity Framework, and SQL Server</b>.')
bullet('Developed contract generation with <b>Open XML</b> and template variable replacement, converting HTML content into Word documents.')
bullet('Modernized legacy interfaces with React and AngularJS; maintained school CRM workflows and implemented authentication improvements across client applications.')
footer(1); c.showPage()
y = 750
para('Dioscar Rodriguez', 16, 21, bold=True)
para('Experience, selected projects & technical skills', 9.5, 14, color='#555555')
section('Earlier experience')
role('Full Stack Web Developer', 'Clever Design', 'Oct 2015 - May 2016')
bullet('Developed and deployed responsive ASP.NET / C# websites and CMS features using SQL Server, JavaScript, AJAX, and Bootstrap; built search and autosuggestion workflows.')
bullet('Tested and remediated SQL injection and cross-site scripting issues; guided clients in maintaining website content.')
gap(6)
role('Web Developer', 'Pointer Security', 'Jul 2014 - Oct 2015')
bullet('Built ASP.NET MVC5 applications with C#, Entity Framework, and SQL Server; contributed to application architecture, business logic, and database design.')
bullet('Implemented real-time notifications with SignalR and responsive interfaces using Knockout.js, jQuery, AJAX, and Bootstrap.')
section('Selected independent projects')
role('GlucoPlate AI', 'AI recipe companion | Python, FastAPI, Pydantic, SQLAlchemy', 'Personal project')
bullet('Build a recipe-generation and shopping application with structured API contracts, provider abstraction for GitHub Copilot SDK / Gemini, and local fallback generation.')
bullet('Implement recipe saving, ingredient normalization, product and store search, shopping carts, and route planning in a responsive PWA.')
para('<link href="https://github.com/dioscarr/glucoplate-ai">github.com/dioscarr/glucoplate-ai</link>', 9, 12, indent=14, color='#555555')
gap(11)
role('Web development & deployment tooling', 'WordPress / Divi and self-hosted applications', 'Personal projects')
bullet('Develop WordPress features for form-submission storage, service management, and application-specific access; assemble Divi pages through reusable JSON components.')
bullet('Use GitHub Actions, Podman, and Tailscale for branch-specific application deployments; apply coding assistants to implementation, debugging, and refactoring.')
section('Technical skills')
# Dark skills panel echoes the supplied resume while keeping readable selectable text.
rows = [
('<b>Backend & data</b>', 'C#, .NET, ASP.NET Core, Blazor, Entity Framework / EF Core, SQL Server, REST APIs, SignalR'),
('<b>Frontend</b>', 'React, TypeScript, JavaScript, HTML, CSS, Tailwind CSS, Bootstrap, WordPress / PHP'),
('<b>Delivery & security</b>', 'Git / GitHub, GitHub Actions, Docker / Podman, IIS, Auth0, role-based access, Serilog / Seq'),
('<b>AI & languages</b>', 'Python, FastAPI, Pydantic, GitHub Copilot, AI-assisted development; English and Spanish'),
]
height=122
if y-height<49: raise ValueError(f'Skills panel overflows: {y}')
c.setFillColor(HexColor('#181818')); c.rect(LEFT, y-height, RIGHT-LEFT, height, fill=1, stroke=0)
y-=10
for label, text in rows:
    para(f'{label}  {text}', 9, 12, indent=12, color='#ffffff')
    gap(5)
footer(2)
c.save()
print(OUT)
