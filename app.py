import gradio as gr
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from datetime import datetime

EBOOK_THEMES = {
    0: {"titre": "Finance pour Débutants", "sous_titre": "L'épargne est la fondation", "theme": "Épargne", "couleur_primaire": "#3498db", "couleur_secondaire": "#2980b9", "icone_emoji": "💰"},
    1: {"titre": "Finance pour Entrepreneurs", "sous_titre": "L'investissement est le levier", "theme": "Investissement", "couleur_primaire": "#27ae60", "couleur_secondaire": "#229954", "icone_emoji": "📈"},
    2: {"titre": "Finance pour Jeunes", "sous_titre": "Crypto & Tendances", "theme": "Crypto", "couleur_primaire": "#e74c3c", "couleur_secondaire": "#c0392b", "icone_emoji": "🚀"},
    3: {"titre": "Finance pour Femmes", "sous_titre": "Indépendance financière", "theme": "Indépendance", "couleur_primaire": "#e91e63", "couleur_secondaire": "#c2185b", "icone_emoji": "👩‍💼"},
    4: {"titre": "Finance Africaine", "sous_titre": "Solutions adaptées", "theme": "Africain", "couleur_primaire": "#f39c12", "couleur_secondaire": "#d68910", "icone_emoji": "🌍"},
    5: {"titre": "Finance Avancée", "sous_titre": "Stratégie complète", "theme": "Stratégie", "couleur_primaire": "#5c3d99", "couleur_secondaire": "#4a235a", "icone_emoji": "🎯"},
    6: {"titre": "Finance & Bien-Être", "sous_titre": "Psychologie financière", "theme": "Psychologie", "couleur_primaire": "#1abc9c", "couleur_secondaire": "#16a085", "icone_emoji": "🧠"}
}

class EbookGenerator:
    def __init__(self, jour):
        self.jour = jour
        self.theme = EBOOK_THEMES[jour]
        self.titre = self.theme["titre"]
        self.couleur_primaire = self.theme["couleur_primaire"]
        self.couleur_secondaire = self.theme["couleur_secondaire"]
        
    def generer_couverture(self):
        story = []
        styles = getSampleStyleSheet()
        titre_style = ParagraphStyle('CouvertureTitle', parent=styles['Heading1'], fontSize=48, textColor=colors.HexColor(self.couleur_primaire), spaceAfter=20, alignment=1)
        sous_titre_style = ParagraphStyle('CouvertureSousTitle', parent=styles['Normal'], fontSize=24, textColor=colors.HexColor(self.couleur_secondaire), spaceAfter=40, alignment=1)
        story.append(Spacer(1, 2*cm))
        story.append(Paragraph(self.theme["icone_emoji"] + " " + self.titre, titre_style))
        story.append(Spacer(1, 0.3*cm))
        story.append(Paragraph(self.theme["sous_titre"], sous_titre_style))
        story.append(Spacer(1, 1*cm))
        auteur_style = ParagraphStyle('Auteur', parent=styles['Normal'], fontSize=12, alignment=1)
        story.append(Paragraph("Expert en Finance & Investissement", auteur_style))
        story.append(Spacer(1, 0.2*cm))
        story.append(Paragraph(f"Généré le {datetime.now().strftime('%d/%m/%Y')}", auteur_style))
        return story
    
    def generer_table_matieres(self):
        story = []
        styles = getSampleStyleSheet()
        titre_style = ParagraphStyle('TableMatieresTitre', parent=styles['Heading1'], fontSize=24, textColor=colors.HexColor(self.couleur_primaire), spaceAfter=20)
        story.append(Paragraph("Table des matières", titre_style))
        story.append(Spacer(1, 0.3*cm))
        chapitres = ["Mentalité d'épargne", "Gérer son budget", "Créer un fonds d'urgence", "Introduction à l'investissement", "Types d'investissements", "Stratégies long terme", "Comprendre la crypto", "Investir en crypto simplement", "Sécurité et protection", "Plan financier personnel", "Discipline et habitudes", "Erreurs à éviter"]
        for i, chapitre in enumerate(chapitres, 1):
            item_style = ParagraphStyle('TableItem', parent=styles['Normal'], fontSize=11, leftIndent=20, spaceAfter=8)
            story.append(Paragraph(f"{i}. {chapitre}", item_style))
        story.append(PageBreak())
        return story
    
    def generer_introduction(self):
        story = []
        styles = getSampleStyleSheet()
        titre_style = ParagraphStyle('IntroTitre', parent=styles['Heading1'], fontSize=24, textColor=colors.HexColor(self.couleur_primaire), spaceAfter=20)
        body_style = ParagraphStyle('IntroBody', parent=styles['Normal'], fontSize=11, alignment=4, spaceAfter=12)
        story.append(Paragraph("Introduction", titre_style))
        story.append(Spacer(1, 0.2*cm))
        intro_text = f"Bienvenue dans ce guide complet sur {self.theme['theme'].lower()}. Ce guide de 50 pages vous fournira les connaissances pratiques pour transformer votre situation financière."
        story.append(Paragraph(intro_text, body_style))
        story.append(PageBreak())
        return story
    
    def generer_chapitres(self):
        story = []
        styles = getSampleStyleSheet()
        chapitres = ["Mentalité d'épargne", "Gérer son budget", "Créer un fonds d'urgence", "Introduction à l'investissement", "Types d'investissements", "Stratégies long terme", "Comprendre la crypto", "Investir en crypto simplement", "Sécurité et protection", "Plan financier personnel", "Discipline et habitudes", "Erreurs à éviter"]
        for chapitre in chapitres:
            titre_style = ParagraphStyle('ChapitreTitre', parent=styles['Heading1'], fontSize=24, textColor=colors.HexColor(self.couleur_primaire), spaceAfter=15, spaceBefore=15)
            story.append(Paragraph(chapitre, titre_style))
            body_style = ParagraphStyle('ChapitreBody', parent=styles['Normal'], fontSize=11, alignment=4, spaceAfter=12)
            contenu = f"Ce chapitre couvre les aspects essentiels de {chapitre.lower()}. Vous apprendrez les concepts clés et comment les appliquer dans votre vie quotidienne."
            story.append(Paragraph(contenu, body_style))
            story.append(Spacer(1, 0.3*cm))
            story.append(PageBreak())
        return story
    
    def generer_conclusion(self):
        story = []
        styles = getSampleStyleSheet()
        titre_style = ParagraphStyle('ConclusionTitre', parent=styles['Heading1'], fontSize=24, textColor=colors.HexColor(self.couleur_primaire), spaceAfter=20)
        body_style = ParagraphStyle('ConclusionBody', parent=styles['Normal'], fontSize=11, alignment=4, spaceAfter=12)
        story.append(Paragraph("Conclusion", titre_style))
        story.append(Spacer(1, 0.2*cm))
        conclusion_text = "Vous avez maintenant les connaissances pour transformer votre situation financière. Commencez dès aujourd'hui!"
        story.append(Paragraph(conclusion_text, body_style))
        story.append(PageBreak())
        return story
    
    def generer_bonus(self):
        story = []
        styles = getSampleStyleSheet()
        titre_style = ParagraphStyle('BonusTitre', parent=styles['Heading2'], fontSize=18, textColor=colors.HexColor(self.couleur_primaire), spaceAfter=15)
        body_style = ParagraphStyle('BonusBody', parent=styles['Normal'], fontSize=10, spaceAfter=10)
        story.append(Paragraph("BONUS - Plan d'action 30 jours", titre_style))
        story.append(Paragraph("Semaine 1: Diagnostic et planification", body_style))
        story.append(Paragraph("Semaine 2: Mise en place des bases", body_style))
        story.append(Paragraph("Semaine 3: Premiers investissements", body_style))
        story.append(Paragraph("Semaine 4: Suivi et ajustement", body_style))
        story.append(PageBreak())
        story.append(Paragraph("BONUS - Checklist complète", titre_style))
        story.append(Paragraph("☐ Diagnostic financier complété", body_style))
        story.append(Paragraph("☐ Budget créé et automatisé", body_style))
        story.append(Paragraph("☐ Fonds d'urgence établi", body_style))
        story.append(PageBreak())
        story.append(Paragraph("BONUS - Ressources et liens utiles", titre_style))
        story.append(Paragraph("• Investopedia.com", body_style))
        story.append(Paragraph("• Bogleheads.org", body_style))
        return story
    
    def generer_pdf(self, nom_fichier):
        doc = SimpleDocTemplate(nom_fichier, pagesize=A4, topMargin=2*cm, bottomMargin=2*cm, leftMargin=2.5*cm, rightMargin=2.5*cm)
        story = []
        story.extend(self.generer_couverture())
        story.append(PageBreak())
        story.extend(self.generer_table_matieres())
        story.extend(self.generer_introduction())
        story.extend(self.generer_chapitres())
        story.extend(self.generer_conclusion())
        story.extend(self.generer_bonus())
        doc.build(story)
        return nom_fichier

def generer_ebook(jour):
    try:
        generator = EbookGenerator(jour)
        nom_fichier = f"ebook_{jour}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        generator.generer_pdf(nom_fichier)
        return nom_fichier, f"✅ eBook '{generator.titre}' généré avec succès !"
    except Exception as e:
        return None, f"❌ Erreur : {str(e)}"

with gr.Blocks(title="eBook Generator") as demo:
    gr.Markdown("# 📚 Générateur d'eBooks Automatique")
    gr.Markdown("Générez des eBooks professionnels de 50 pages en un clic !")
    
    with gr.Row():
        jour_select = gr.Dropdown(
            choices=[
                ("Lundi - Finance Débutants", 0),
                ("Mardi - Finance Entrepreneurs", 1),
                ("Mercredi - Finance Jeunes", 2),
                ("Jeudi - Finance Femmes", 3),
                ("Vendredi - Finance Africaine", 4),
                ("Samedi - Finance Avancée", 5),
                ("Dimanche - Finance Bien-Être", 6)
            ],
            label="Sélectionnez le jour/thème",
            value=0
        )
        generer_btn = gr.Button("🚀 Générer l'eBook", variant="primary")
    
    with gr.Row():
        output_file = gr.File(label="📥 Télécharger le PDF")
        output_message = gr.Textbox(label="Statut", interactive=False)
    
    generer_btn.click(
        fn=generer_ebook,
        inputs=jour_select,
        outputs=[output_file, output_message]
    )

if __name__ == "__main__":
    demo.launch()
