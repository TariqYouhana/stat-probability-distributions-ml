import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    PRIMARY = RGBColor(37, 99, 235)      # #2563EB Blue
    PRIMARY_DARK = RGBColor(30, 41, 59)  # #1E293B Dark Slate
    ACCENT = RGBColor(124, 58, 237)      # #7C3AED Purple
    TEXT_DARK = RGBColor(30, 41, 59)    # #1E293B
    TEXT_MUTED = RGBColor(100, 116, 139)# #64748B
    BG_LIGHT = RGBColor(248, 250, 252)   # #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)
    BORDER_COLOR = RGBColor(226, 232, 240)
    HIGHLIGHT_BG = RGBColor(238, 242, 255)
    SUCCESS_COLOR = RGBColor(16, 185, 129)
    TAG_BLUE = RGBColor(219, 234, 254)
    TAG_PURPLE = RGBColor(237, 233, 254)

    def add_header(slide, title_text, category_text="GROUP 8 | PROBABILITY DISTRIBUTIONS IN ML & DATA SCIENCE"):
        # Top banner background line
        top_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.08))
        top_line.fill.solid()
        top_line.fill.fore_color.rgb = PRIMARY
        top_line.line.color.rgb = PRIMARY

        # Category text
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = PRIMARY

        # Title text
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.5), Inches(0.65))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = PRIMARY_DARK

    def add_footer(slide, slide_num):
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.35))
        tf = footer_box.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = "Probability Distributions in Machine Learning & Data Science — Group 8"
        p.font.size = Pt(9.5)
        p.font.color.rgb = TEXT_MUTED
        
        num_box = slide.shapes.add_textbox(Inches(11.5), Inches(7.0), Inches(1.0), Inches(0.35))
        tf_num = num_box.text_frame
        p_num = tf_num.paragraphs[0]
        p_num.alignment = PP_ALIGN.RIGHT
        p_num.text = f"{slide_num} / 15"
        p_num.font.size = Pt(10)
        p_num.font.bold = True
        p_num.font.color.rgb = PRIMARY

    def add_card(slide, left, top, width, height, bg_color=CARD_BG, border_color=BORDER_COLOR):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        if border_color:
            shape.line.color.rgb = border_color
            shape.line.width = Pt(1.2)
        else:
            shape.line.fill.background()
        return shape

    # ═══════════════════════════════════════════════════════
    # SLIDE 1: Title Slide
    # ═══════════════════════════════════════════════════════
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = PRIMARY_DARK
    bg1.line.fill.background()

    # Accent decorative block
    dec = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.2), Inches(11.733), Inches(5.1))
    dec.fill.solid()
    dec.fill.fore_color.rgb = RGBColor(37, 50, 75)
    dec.line.color.rgb = PRIMARY
    dec.line.width = Pt(1.5)

    tb = slide1.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11), Inches(4.3))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "GROUP 8 PRESENTATION"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(147, 197, 253)
    p0.space_after = Pt(14)

    p1 = tf.add_paragraph()
    p1.text = "Probability Distributions in\nMachine Learning & Data Science"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)
    p1.space_after = Pt(16)

    p2 = tf.add_paragraph()
    p2.text = "Exploring the Gaussian Distribution, Naive Bayes Classification, and Maximum Likelihood Estimation"
    p2.font.size = Pt(16)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_after = Pt(28)

    p3 = tf.add_paragraph()
    p3.text = "Group 8  •  Probability Distribution & Statistical Modeling Course"
    p3.font.size = Pt(13)
    p3.font.color.rgb = RGBColor(148, 163, 184)

    # ═══════════════════════════════════════════════════════
    # SLIDE 2: Why Distributions Matter in Data Science
    # ═══════════════════════════════════════════════════════
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Why Probability Distributions Matter in Data Science")
    add_footer(slide2, 2)

    # Left card: Key Drivers
    add_card(slide2, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb2_left = slide2.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf2_l = tb2_left.text_frame
    tf2_l.word_wrap = True
    
    p = tf2_l.paragraphs[0]
    p.text = "Key Roles in Statistical Learning"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(12)

    bullets = [
        ("Quantify Uncertainty: ", "Every real-world sensor, survey, and clinical test carries natural variation. Distributions allow us to model, bound, and evaluate risk rigorously."),
        ("Foundation of Machine Learning: ", "Algorithms like Naive Bayes, Gaussian Mixture Models, and Kalman Filters model parameters directly via probability distributions."),
        ("Synthetic Data & Monte Carlo: ", "Understanding the governing distribution lets data scientists simulate thousands of scenarios and perform stress-testing."),
        ("Probabilistic Inference: ", "Converts uncalibrated scores into true posterior probabilities P(Y|X) for optimal real-world decision thresholds.")
    ]
    for b_title, b_desc in bullets:
        p_b = tf2_l.add_paragraph()
        run1 = p_b.add_run()
        run1.text = "• " + b_title
        run1.font.bold = True
        run1.font.size = Pt(12.5)
        run1.font.color.rgb = PRIMARY_DARK
        run2 = p_b.add_run()
        run2.text = b_desc
        run2.font.size = Pt(12)
        run2.font.color.rgb = TEXT_DARK
        p_b.space_after = Pt(10)

    # Right Card 1: Core Insight
    add_card(slide2, Inches(6.9), Inches(1.6), Inches(5.6), Inches(2.4), bg_color=HIGHLIGHT_BG, border_color=PRIMARY)
    tb2_r1 = slide2.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(2.0))
    tf2_r1 = tb2_r1.text_frame
    tf2_r1.word_wrap = True
    p = tf2_r1.paragraphs[0]
    p.text = "Distributions are the Language Data Speaks"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(8)
    p_desc = tf2_r1.add_paragraph()
    p_desc.text = "Raw data appears as random noise. Once we characterize its underlying distribution, noise transforms into predictable structure, enabling anomaly detection, hypothesis testing, and accurate predictive classification."
    p_desc.font.size = Pt(12)
    p_desc.font.color.rgb = TEXT_DARK

    # Right Card 2: Core Principle
    add_card(slide2, Inches(6.9), Inches(4.3), Inches(5.6), Inches(2.4))
    tb2_r2 = slide2.shapes.add_textbox(Inches(7.1), Inches(4.5), Inches(5.2), Inches(2.0))
    tf2_r2 = tb2_r2.text_frame
    tf2_r2.word_wrap = True
    p = tf2_r2.paragraphs[0]
    p.text = "Explicit vs. Implicit Assumptions"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_DARK
    p.space_after = Pt(8)
    p_desc = tf2_r2.add_paragraph()
    p_desc.text = "• Explicit: Generative classifiers like Naive Bayes explicitly assume P(X|C) follows Gaussian, Bernoulli, or Multinomial densities.\n• Implicit: Even Ordinary Least Squares (OLS) regression relies on Gaussian assumptions to prove the Gauss-Markov optimal estimator theorem."
    p_desc.font.size = Pt(12)
    p_desc.font.color.rgb = TEXT_MUTED

    # ═══════════════════════════════════════════════════════
    # SLIDE 3: The Gaussian (Normal) Distribution
    # ═══════════════════════════════════════════════════════
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "The Gaussian (Normal) Distribution — Overview")
    add_footer(slide3, 3)

    # Left content
    add_card(slide3, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1))
    tb3 = slide3.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.7))
    tf3 = tb3.text_frame
    tf3.word_wrap = True

    p = tf3.paragraphs[0]
    p.text = "The Bell Curve — Continuous Cornerstone"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(10)

    g_bullets = [
        ("Continuous Random Variable: ", "Takes on any real value along (-∞, +∞). The total area under the curve equals exactly 1.0."),
        ("Ubiquitous in Reality: ", "Heights, weights, standardized exam scores, sensor measurement errors, and financial returns cluster around a central mean."),
        ("Central Limit Theorem (CLT): ", "The sum or mean of n independent and identically distributed random variables tends toward a Normal distribution as n grows, regardless of parent shape!"),
        ("The 68-95-99.7 Empirical Rule: ", "A powerful heuristic for rapid spread estimation:\n  • 68.27% of observations fall within μ ± 1σ\n  • 95.45% of observations fall within μ ± 2σ\n  • 99.73% of observations fall within μ ± 3σ")
    ]
    for b_title, b_desc in g_bullets:
        p_b = tf3.add_paragraph()
        run1 = p_b.add_run()
        run1.text = "• " + b_title
        run1.font.bold = True
        run1.font.size = Pt(12)
        run1.font.color.rgb = PRIMARY_DARK
        run2 = p_b.add_run()
        run2.text = b_desc
        run2.font.size = Pt(11.5)
        run2.font.color.rgb = TEXT_DARK
        p_b.space_after = Pt(8)

    # Right Image: fig_empirical_rule.png
    add_card(slide3, Inches(6.7), Inches(1.6), Inches(5.8), Inches(5.1))
    if os.path.exists("fig_empirical_rule.png"):
        slide3.shapes.add_picture("fig_empirical_rule.png", Inches(6.9), Inches(1.9), width=Inches(5.4))
    cap_box = slide3.shapes.add_textbox(Inches(6.9), Inches(6.1), Inches(5.4), Inches(0.5))
    tf_cap = cap_box.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Figure: The 68-95-99.7% Empirical Rule with Shaded Standard Deviation Bands"
    p_cap.font.size = Pt(10.5)
    p_cap.alignment = PP_ALIGN.CENTER
    p_cap.font.color.rgb = TEXT_MUTED

    # ═══════════════════════════════════════════════════════
    # SLIDE 4: Mathematical Foundation
    # ═══════════════════════════════════════════════════════
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Gaussian Distribution — Mathematical Formulation")
    add_footer(slide4, 4)

    # Formula Box
    f_box = add_card(slide4, Inches(0.8), Inches(1.5), Inches(11.733), Inches(1.1), bg_color=HIGHLIGHT_BG, border_color=ACCENT)
    tb_f = slide4.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.333), Inches(0.9))
    tf_f = tb_f.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.alignment = PP_ALIGN.CENTER
    p_f.text = "f(x) =  [ 1 / (σ √(2π)) ] · exp( − (x − μ)² / (2σ²) )"
    p_f.font.size = Pt(22)
    p_f.font.bold = True
    p_f.font.color.rgb = ACCENT

    # Left: Parameter Table
    add_card(slide4, Inches(0.8), Inches(2.8), Inches(6.5), Inches(3.9))
    tb_t = slide4.shapes.add_textbox(Inches(1.0), Inches(3.0), Inches(6.1), Inches(3.5))
    tf_t = tb_t.text_frame
    tf_t.word_wrap = True
    p = tf_t.paragraphs[0]
    p.text = "Parameter Breakdown & Symbols"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(8)

    symbols = [
        ("x ∈ (-∞, +∞)", "Continuous random variable realization"),
        ("μ = E[X]", "Location parameter: Mean, Median, and Mode"),
        ("σ > 0", "Scale parameter: Standard deviation (dispersion)"),
        ("σ² = Var(X)", "Variance: Squared dispersion around the mean"),
        ("1 / (σ√(2π))", "Normalizing constant ensuring total area under PDF = 1"),
        ("exp(-(x-μ)²/2σ²)", "Exponential decay kernel creating symmetric bell tail")
    ]
    for sym, desc in symbols:
        p_s = tf_t.add_paragraph()
        r1 = p_s.add_run()
        r1.text = sym + "  :  "
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_s.add_run()
        r2.text = desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_s.space_after = Pt(4)

    # Right: Properties & Assumptions
    add_card(slide4, Inches(7.6), Inches(2.8), Inches(4.933), Inches(3.9))
    tb_pr = slide4.shapes.add_textbox(Inches(7.8), Inches(3.0), Inches(4.5), Inches(3.5))
    tf_pr = tb_pr.text_frame
    tf_pr.word_wrap = True

    p = tf_pr.paragraphs[0]
    p.text = "Essential Properties & Assumptions"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(8)

    props = [
        ("Perfect Symmetry: ", "Skewness = 0. Centered exactly at μ."),
        ("Inflection Points: ", "Curvature changes concavity at x = μ ± σ."),
        ("Linear Transformation: ", "If X ~ N(μ, σ²), then aX + b ~ N(aμ + b, a²σ²)."),
        ("Standard Normal: ", "Z = (X - μ)/σ ~ N(0, 1), standardizing any scale."),
        ("Key Assumptions: ", "Data is continuous, symmetric, unimodal, and free from fat, heavy-tailed outliers.")
    ]
    for p_title, p_desc in props:
        p_p = tf_pr.add_paragraph()
        r1 = p_p.add_run()
        r1.text = "• " + p_title
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_p.add_run()
        r2.text = p_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_p.space_after = Pt(4)

    # ═══════════════════════════════════════════════════════
    # SLIDE 5: Shape, Parameters & CDF
    # ═══════════════════════════════════════════════════════
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Parameters & Cumulative Distribution Function (CDF)")
    add_footer(slide5, 5)

    # Left plot: Parameter effects
    add_card(slide5, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.1))
    if os.path.exists("fig_parameter_effects.png"):
        slide5.shapes.add_picture("fig_parameter_effects.png", Inches(0.95), Inches(1.8), width=Inches(5.4))
    tb5_l = slide5.shapes.add_textbox(Inches(1.0), Inches(4.7), Inches(5.3), Inches(1.8))
    tf5_l = tb5_l.text_frame
    tf5_l.word_wrap = True
    p = tf5_l.paragraphs[0]
    p.text = "Parameter Sensitivity Dynamics:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(4)
    p1 = tf5_l.add_paragraph()
    p1.text = "• μ shifts the distribution along the horizontal axis without changing spread or height.\n• σ widens the curve and lowers the peak (larger spread) or sharpens it (smaller spread)."
    p1.font.size = Pt(11)
    p1.font.color.rgb = TEXT_DARK

    # Right plot: CDF
    add_card(slide5, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.1))
    if os.path.exists("fig_cdf.png"):
        slide5.shapes.add_picture("fig_cdf.png", Inches(7.0), Inches(1.8), width=Inches(5.3))
    tb5_r = slide5.shapes.add_textbox(Inches(7.0), Inches(5.1), Inches(5.3), Inches(1.4))
    tf5_r = tb5_r.text_frame
    tf5_r.word_wrap = True
    p = tf5_r.paragraphs[0]
    p.text = "Cumulative Distribution Function: F(x) = P(X ≤ x)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(4)
    p1 = tf5_r.add_paragraph()
    p1.text = "• S-shaped curve monotonically increasing from 0 to 1.\n• F(μ) = 0.50 (50th percentile). Used for p-values, hypothesis tests, and confidence intervals."
    p1.font.size = Pt(11)
    p1.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 6: Bernoulli & Multinomial Distributions
    # ═══════════════════════════════════════════════════════
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Discrete Foundations: Bernoulli & Multinomial")
    add_footer(slide6, 6)

    # Left: Bernoulli Card + Multinomial Card
    add_card(slide6, Inches(0.8), Inches(1.6), Inches(5.8), Inches(2.4))
    tb6_b = slide6.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.4), Inches(2.1))
    tf6_b = tb6_b.text_frame
    tf6_b.word_wrap = True
    p = tf6_b.paragraphs[0]
    p.text = "Bernoulli Distribution (Binary Outcomes)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(4)
    p_f = tf6_b.add_paragraph()
    p_f.text = "P(X = k) = p^k · (1 − p)^(1−k),   k ∈ {0, 1}"
    p_f.font.size = Pt(12.5)
    p_f.font.bold = True
    p_f.font.color.rgb = PRIMARY
    p_f.space_after = Pt(4)
    p_d = tf6_b.add_paragraph()
    p_d.text = "• Mean = p  |  Variance = p(1 − p)\n• Applied in binary feature indicators (e.g. Word present in email: Yes/No)."
    p_d.font.size = Pt(11)
    p_d.font.color.rgb = TEXT_DARK

    add_card(slide6, Inches(0.8), Inches(4.2), Inches(5.8), Inches(2.5))
    tb6_m = slide6.shapes.add_textbox(Inches(1.0), Inches(4.3), Inches(5.4), Inches(2.2))
    tf6_m = tb6_m.text_frame
    tf6_m.word_wrap = True
    p = tf6_m.paragraphs[0]
    p.text = "Multinomial Distribution (Multi-Category Counts)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = SUCCESS_COLOR
    p.space_after = Pt(4)
    p_f = tf6_m.add_paragraph()
    p_f.text = "P(X₁=x₁,…,Xₖ=xₖ) = (n! / ∏ xᵢ!) · ∏ pᵢ^(xᵢ)"
    p_f.font.size = Pt(12)
    p_f.font.bold = True
    p_f.font.color.rgb = PRIMARY
    p_f.space_after = Pt(4)
    p_d = tf6_m.add_paragraph()
    p_d.text = "• Expected Count E[Xᵢ] = n · pᵢ  |  Var(Xᵢ) = n · pᵢ(1 − pᵢ)\n• Applied in term frequency count vectors for natural language processing."
    p_d.font.size = Pt(11)
    p_d.font.color.rgb = TEXT_DARK

    # Right: Embedded Plot
    add_card(slide6, Inches(6.9), Inches(1.6), Inches(5.633), Inches(5.1))
    if os.path.exists("fig_bernoulli_multinomial.png"):
        slide6.shapes.add_picture("fig_bernoulli_multinomial.png", Inches(7.05), Inches(1.9), width=Inches(5.3))
    cap_box = slide6.shapes.add_textbox(Inches(7.0), Inches(6.1), Inches(5.4), Inches(0.5))
    tf_cap = cap_box.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Figure: Probability Mass Functions for Binary and Categorical Outcomes"
    p_cap.font.size = Pt(10.5)
    p_cap.alignment = PP_ALIGN.CENTER
    p_cap.font.color.rgb = TEXT_MUTED

    # ═══════════════════════════════════════════════════════
    # SLIDE 7: Introduction to Naive Bayes
    # ═══════════════════════════════════════════════════════
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Introduction to Naive Bayes Classification")
    add_footer(slide7, 7)

    # Bayes Theorem Formula
    add_card(slide7, Inches(0.8), Inches(1.5), Inches(11.733), Inches(1.1), bg_color=HIGHLIGHT_BG, border_color=PRIMARY)
    tb_b = slide7.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.333), Inches(0.9))
    tf_b = tb_b.text_frame
    p_b = tf_b.paragraphs[0]
    p_b.alignment = PP_ALIGN.CENTER
    p_b.text = "P(Cₖ | X) = [ P(X | Cₖ) · P(Cₖ) ] / P(X)"
    p_b.font.size = Pt(22)
    p_b.font.bold = True
    p_b.font.color.rgb = PRIMARY

    # Left: Term Definitions
    add_card(slide7, Inches(0.8), Inches(2.8), Inches(6.0), Inches(3.9))
    tb7_l = slide7.shapes.add_textbox(Inches(1.0), Inches(3.0), Inches(5.6), Inches(3.5))
    tf7_l = tb7_l.text_frame
    tf7_l.word_wrap = True
    p = tf7_l.paragraphs[0]
    p.text = "Four Pillars of Bayes' Theorem"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_DARK
    p.space_after = Pt(8)

    bayes_terms = [
        ("Posterior: P(Cₖ | X)", "Probability that sample X belongs to class Cₖ after observing features."),
        ("Likelihood: P(X | Cₖ)", "Probability of observing the feature values given class membership Cₖ."),
        ("Prior: P(Cₖ)", "Baseline prevalence or frequency of class Cₖ in the population."),
        ("Evidence: P(X)", "Total probability of the features across all classes (acts as normalizer).")
    ]
    for t_name, t_desc in bayes_terms:
        p_t = tf7_l.add_paragraph()
        r1 = p_t.add_run()
        r1.text = "• " + t_name + "\n   "
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY
        r2 = p_t.add_run()
        r2.text = t_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_t.space_after = Pt(4)

    # Right: The Naive Assumption
    add_card(slide7, Inches(7.1), Inches(2.8), Inches(5.433), Inches(3.9))
    tb7_r = slide7.shapes.add_textbox(Inches(7.3), Inches(3.0), Inches(5.0), Inches(3.5))
    tf7_r = tb7_r.text_frame
    tf7_r.word_wrap = True
    p = tf7_r.paragraphs[0]
    p.text = "The 'Naive' Independence Assumption"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(8)

    p_eq = tf7_r.add_paragraph()
    p_eq.text = "P(x₁, …, x_d | Cₖ) = ∏ P(xⱼ | Cₖ)"
    p_eq.font.size = Pt(15)
    p_eq.font.bold = True
    p_eq.font.color.rgb = PRIMARY
    p_eq.space_after = Pt(10)

    p_exp = tf7_r.add_paragraph()
    p_exp.text = "• Simplification: Assumes every feature is conditionally independent of every other feature given the class label.\n• Why it works: Classification only requires finding the argmax class. Even when individual probability estimates are shifted due to feature correlation, the correct class ranking is preserved!"
    p_exp.font.size = Pt(11.5)
    p_exp.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 8: Gaussian Naive Bayes Classifier
    # ═══════════════════════════════════════════════════════
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Gaussian Naive Bayes (GNB) Classifier")
    add_footer(slide8, 8)

    # Left: Methodology
    add_card(slide8, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb8 = slide8.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf8 = tb8.text_frame
    tf8.word_wrap = True
    p = tf8.paragraphs[0]
    p.text = "Continuous Likelihood Formulation"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(8)

    p1 = tf8.add_paragraph()
    p1.text = "For real-valued numeric features, GNB assumes each feature conditioned on class Cₖ follows a 1-dimensional Gaussian distribution:"
    p1.font.size = Pt(11.5)
    p1.space_after = Pt(8)

    p_f = tf8.add_paragraph()
    p_f.text = "P(xⱼ | Cₖ) = [1 / (σₖⱼ√(2π))] · exp( −(xⱼ − μₖⱼ)² / (2σₖⱼ²) )"
    p_f.font.size = Pt(11.5)
    p_f.font.bold = True
    p_f.font.color.rgb = ACCENT
    p_f.space_after = Pt(12)

    gnb_steps = [
        ("Training Phase: ", "Compute sample mean μ̂ₖⱼ and sample variance σ̂²ₖⱼ for every feature j in each class k. Time complexity is O(N · d)."),
        ("Prediction Phase: ", "Evaluate the Gaussian PDF for test features x* under each class hypothesis."),
        ("Log-Space Decision: ", "argmax [ ln P(Cₖ) + ∑ ln P(xⱼ* | Cₖ) ] — avoids floating-point underflow.")
    ]
    for s_title, s_desc in gnb_steps:
        p_s = tf8.add_paragraph()
        r1 = p_s.add_run()
        r1.text = "• " + s_title
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_s.add_run()
        r2.text = s_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_s.space_after = Pt(6)

    # Right: Embedded plot
    add_card(slide8, Inches(6.9), Inches(1.6), Inches(5.633), Inches(5.1))
    if os.path.exists("fig_feature_distributions.png"):
        slide8.shapes.add_picture("fig_feature_distributions.png", Inches(7.05), Inches(1.9), width=Inches(5.3))
    cap_box = slide8.shapes.add_textbox(Inches(7.0), Inches(6.1), Inches(5.4), Inches(0.5))
    tf_cap = cap_box.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Figure: Class-Conditional Gaussian Densities for Features 1 & 2"
    p_cap.font.size = Pt(10.5)
    p_cap.alignment = PP_ALIGN.CENTER
    p_cap.font.color.rgb = TEXT_MUTED

    # ═══════════════════════════════════════════════════════
    # SLIDE 9: NB Variants Comparison
    # ═══════════════════════════════════════════════════════
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Naive Bayes Family — Architectural Comparison")
    add_footer(slide9, 9)

    cards_info = [
        ("Gaussian NB", "CONTINUOUS", PRIMARY, Inches(0.8), [
            ("Feature Domain", "Real numbers ℝ (continuous)"),
            ("Data Types", "Measurements, sensor readings, vitals, prices"),
            ("Likelihood", "Normal PDF: f(x; μ, σ²)"),
            ("Parameters", "Mean μₖⱼ and Variance σ²ₖⱼ per class"),
            ("Key Advantage", "Handles arbitrary continuous scales without binning")
        ]),
        ("Bernoulli NB", "BINARY", ACCENT, Inches(4.8), [
            ("Feature Domain", "Binary values {0, 1}"),
            ("Data Types", "Word presence/absence, yes/no flags"),
            ("Likelihood", "Bernoulli PMF: p^x (1-p)^(1-x)"),
            ("Parameters", "Probability of occurrence pₖⱼ"),
            ("Key Advantage", "Directly penalizes the non-occurrence of expected tokens")
        ]),
        ("Multinomial NB", "COUNTS", SUCCESS_COLOR, Inches(8.8), [
            ("Feature Domain", "Non-negative integers ℕ₀"),
            ("Data Types", "Term frequency counts, token occurrences"),
            ("Likelihood", "Multinomial PMF: ∏ θⱼ^(xⱼ)"),
            ("Parameters", "Token occurrence frequency ratio θₖⱼ"),
            ("Key Advantage", "Standard baseline for text classification and topic modeling")
        ])
    ]

    for title, tag, color, left_pos, details in cards_info:
        add_card(slide9, left_pos, Inches(1.6), Inches(3.733), Inches(4.3), border_color=color)
        tb_c = slide9.shapes.add_textbox(left_pos + Inches(0.2), Inches(1.8), Inches(3.333), Inches(3.9))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True

        p = tf_c.paragraphs[0]
        p.text = title
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = color
        p.space_after = Pt(2)

        p_tag = tf_c.add_paragraph()
        p_tag.text = f"[{tag}]"
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = TEXT_MUTED
        p_tag.space_after = Pt(10)

        for d_title, d_val in details:
            p_d = tf_c.add_paragraph()
            r1 = p_d.add_run()
            r1.text = d_title + ": "
            r1.font.bold = True
            r1.font.size = Pt(11)
            r1.font.color.rgb = PRIMARY_DARK
            r2 = p_d.add_run()
            r2.text = d_val
            r2.font.size = Pt(10.5)
            r2.font.color.rgb = TEXT_DARK
            p_d.space_after = Pt(6)

    # Bottom unified principle box
    add_card(slide9, Inches(0.8), Inches(6.1), Inches(11.733), Inches(0.8), bg_color=HIGHLIGHT_BG, border_color=PRIMARY)
    tb_u = slide9.shapes.add_textbox(Inches(1.0), Inches(6.15), Inches(11.333), Inches(0.7))
    tf_u = tb_u.text_frame
    p_u = tf_u.paragraphs[0]
    p_u.text = "Unified Principle: All three models share the exact same Bayesian logic and independence assumption. The only structural difference is the likelihood distribution selected to match feature types."
    p_u.font.size = Pt(11.5)
    p_u.font.bold = True
    p_u.font.color.rgb = PRIMARY_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 10: Likelihood & Maximum Likelihood Estimation
    # ═══════════════════════════════════════════════════════
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Likelihood & Maximum Likelihood Estimation (MLE)")
    add_footer(slide10, 10)

    # Left: Concept
    add_card(slide10, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb10_l = slide10.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf10_l = tb10_l.text_frame
    tf10_l.word_wrap = True

    p = tf10_l.paragraphs[0]
    p.text = "The Concept of Likelihood"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(8)

    p1 = tf10_l.add_paragraph()
    p1.text = "Given an observed sample dataset D = {x₁, x₂, …, xₙ}, the likelihood function L(θ | D) evaluates how probable the data is under different parameter values θ:"
    p1.font.size = Pt(11.5)
    p1.space_after = Pt(6)

    p_lf = tf10_l.add_paragraph()
    p_lf.text = "L(θ | D) = ∏ f(xᵢ | θ)   ⇒   ln L(θ) = ∑ ln f(xᵢ | θ)"
    p_lf.font.size = Pt(12)
    p_lf.font.bold = True
    p_lf.font.color.rgb = ACCENT
    p_lf.space_after = Pt(12)

    p2 = tf10_l.add_paragraph()
    p2.text = "Maximum Likelihood Estimation (MLE)"
    p2.font.size = Pt(15)
    p2.font.bold = True
    p2.font.color.rgb = PRIMARY
    p2.space_after = Pt(8)

    p3 = tf10_l.add_paragraph()
    p3.text = "MLE selects the parameter values θ̂ that maximize the likelihood of having generated the observed data:\n   θ̂_MLE = argmax_θ ln L(θ | D)"
    p3.font.size = Pt(11.5)
    p3.space_after = Pt(8)

    # Right: Gaussian Analytical Solution
    add_card(slide10, Inches(6.9), Inches(1.6), Inches(5.633), Inches(5.1))
    tb10_r = slide10.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(4.7))
    tf10_r = tb10_r.text_frame
    tf10_r.word_wrap = True

    p = tf10_r.paragraphs[0]
    p.text = "Closed-Form Gaussian Solution"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = SUCCESS_COLOR
    p.space_after = Pt(8)

    p1 = tf10_r.add_paragraph()
    p1.text = "Setting partial derivatives to zero yields analytical closed-form solutions:"
    p1.font.size = Pt(11.5)
    p1.space_after = Pt(10)

    p_m1 = tf10_r.add_paragraph()
    p_m1.text = "• Mean MLE:       μ̂ = (1 / n) ∑ xᵢ  (Sample Mean)"
    p_m1.font.size = Pt(12)
    p_m1.font.bold = True
    p_m1.font.color.rgb = PRIMARY
    p_m1.space_after = Pt(6)

    p_m2 = tf10_r.add_paragraph()
    p_m2.text = "• Variance MLE:  σ̂² = (1 / n) ∑ (xᵢ − μ̂)²  (Sample Variance)"
    p_m2.font.size = Pt(12)
    p_m2.font.bold = True
    p_m2.font.color.rgb = PRIMARY
    p_m2.space_after = Pt(16)

    p_box = tf10_r.add_paragraph()
    p_box.text = "Why this is a Major Advantage:"
    p_box.font.size = Pt(13)
    p_box.font.bold = True
    p_box.font.color.rgb = PRIMARY_DARK
    p_box.space_after = Pt(6)

    p_box_desc = tf10_r.add_paragraph()
    p_box_desc.text = "• Zero iterative gradient descent required (unlike deep learning).\n• Parameters are computed instantaneously in a single linear pass.\n• Intuitive sample statistics are theoretically optimal."
    p_box_desc.font.size = Pt(11.5)
    p_box_desc.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 11: Real-Life Application 1 — Email Spam Filtering
    # ═══════════════════════════════════════════════════════
    slide11 = prs.slides.add_slide(blank_layout)
    add_header(slide11, "Application 1: Email Spam Classification")
    add_footer(slide11, 11)

    # Left: Process Workflow
    add_card(slide11, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb11_l = slide11.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf11_l = tb11_l.text_frame
    tf11_l.word_wrap = True

    p = tf11_l.paragraphs[0]
    p.text = "End-to-End Bayesian Spam Filter"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(10)

    spam_steps = [
        ("Tokenization & Cleaning: ", "Email text is parsed into tokens, removing punctuation and stop-words."),
        ("Feature Extraction: ", "Converted to binary indicators (Bernoulli NB) or word count vectors (Multinomial NB)."),
        ("Likelihood Estimation: ", "Words like 'lottery', 'wire', 'act now' exhibit high P(w | Spam) and low P(w | Ham)."),
        ("Laplace Smoothing: ", "Adds pseudo-counts (α = 1) so novel words never produce zero probability: (count + 1)/(N + |V|)."),
        ("Real-Time Prediction: ", "Classifies incoming emails in less than 2 milliseconds.")
    ]
    for s_title, s_desc in spam_steps:
        p_s = tf11_l.add_paragraph()
        r1 = p_s.add_run()
        r1.text = "• " + s_title
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_s.add_run()
        r2.text = s_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_s.space_after = Pt(8)

    # Right: Why it works & Historical Note
    add_card(slide11, Inches(6.9), Inches(1.6), Inches(5.633), Inches(2.6), bg_color=HIGHLIGHT_BG, border_color=PRIMARY)
    tb11_r1 = slide11.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(2.2))
    tf11_r1 = tb11_r1.text_frame
    tf11_r1.word_wrap = True
    p = tf11_r1.paragraphs[0]
    p.text = "Why Naive Bayes Excels in Text Classification"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(6)
    p1 = tf11_r1.add_paragraph()
    p1.text = "• Handles high dimensionality easily: Vocabulary size can exceed 20,000 words without causing overfitting.\n• Online learning: When a user clicks 'Mark as Spam', priors and likelihoods update incrementally without retraining the whole model."
    p1.font.size = Pt(11.5)
    p1.font.color.rgb = TEXT_DARK

    add_card(slide11, Inches(6.9), Inches(4.4), Inches(5.633), Inches(2.3))
    tb11_r2 = slide11.shapes.add_textbox(Inches(7.1), Inches(4.6), Inches(5.2), Inches(1.9))
    tf11_r2 = tb11_r2.text_frame
    tf11_r2.word_wrap = True
    p = tf11_r2.paragraphs[0]
    p.text = "Historical Impact"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(6)
    p1 = tf11_r2.add_paragraph()
    p1.text = "Paul Graham's landmark 2002 paper 'A Plan for Spam' proved Naive Bayes could achieve >99% spam detection with near-zero false positives. It formed the basis for SpamAssassin, Mozilla Thunderbird, and original Gmail spam filters."
    p1.font.size = Pt(11)
    p1.font.color.rgb = TEXT_MUTED

    # ═══════════════════════════════════════════════════════
    # SLIDE 12: Real-Life Application 2 — Medical Diagnosis
    # ═══════════════════════════════════════════════════════
    slide12 = prs.slides.add_slide(blank_layout)
    add_header(slide12, "Application 2: Medical Diagnostic Screening")
    add_footer(slide12, 12)

    # Left: Medical Pipeline
    add_card(slide12, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb12_l = slide12.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf12_l = tb12_l.text_frame
    tf12_l.word_wrap = True

    p = tf12_l.paragraphs[0]
    p.text = "Continuous Biomarker Triage"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(10)

    med_steps = [
        ("Clinical Features: ", "Patient vitals like fasting glucose (mg/dL), systolic BP (mmHg), cholesterol, and BMI are continuous metrics."),
        ("Biological Normality: ", "Biomarkers in healthy vs. diseased populations naturally cluster around distinct means with symmetric dispersion."),
        ("Gaussian Likelihood: ", "GNB fits separate Normal distributions N(μ_healthy, σ²) and N(μ_disease, σ²) for each laboratory test."),
        ("Calibrated Probability: ", "Outputs calibrated risk scores P(Disease = 1 | vitals) that clinicians use for triage thresholds.")
    ]
    for s_title, s_desc in med_steps:
        p_s = tf12_l.add_paragraph()
        r1 = p_s.add_run()
        r1.text = "• " + s_title
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_s.add_run()
        r2.text = s_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_s.space_after = Pt(8)

    # Right: Clinical Benefits & Benchmarks
    add_card(slide12, Inches(6.9), Inches(1.6), Inches(5.633), Inches(2.7), bg_color=HIGHLIGHT_BG, border_color=SUCCESS_COLOR)
    tb12_r1 = slide12.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(2.3))
    tf12_r1 = tb12_r1.text_frame
    tf12_r1.word_wrap = True
    p = tf12_r1.paragraphs[0]
    p.text = "Clinical Advantages in Healthcare"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = SUCCESS_COLOR
    p.space_after = Pt(6)
    p1 = tf12_r1.add_paragraph()
    p1.text = "• Full Interpretability: Unlike deep learning 'black boxes', doctors can inspect μ and σ for every biomarker to see exactly which test raised suspicion.\n• Robust to Missing Data: If a patient didn't take a cholesterol test, that term is simply dropped from the product rule without retraining."
    p1.font.size = Pt(11.5)
    p1.font.color.rgb = TEXT_DARK

    add_card(slide12, Inches(6.9), Inches(4.5), Inches(5.633), Inches(2.2))
    tb12_r2 = slide12.shapes.add_textbox(Inches(7.1), Inches(4.7), Inches(5.2), Inches(1.8))
    tf12_r2 = tb12_r2.text_frame
    tf12_r2.word_wrap = True
    p = tf12_r2.paragraphs[0]
    p.text = "Standard Medical Benchmarks"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_DARK
    p.space_after = Pt(6)
    p1 = tf12_r2.add_paragraph()
    p1.text = "On benchmark clinical datasets (e.g. Wisconsin Breast Cancer, Pima Indians Diabetes), Gaussian NB routinely achieves 93–96% classification accuracy, serving as a rapid first-pass screening tool before costly biopsies."
    p1.font.size = Pt(11)
    p1.font.color.rgb = TEXT_MUTED

    # ═══════════════════════════════════════════════════════
    # SLIDE 13: Practical Demo — Part A: Distribution Simulation
    # ═══════════════════════════════════════════════════════
    slide13 = prs.slides.add_slide(blank_layout)
    add_header(slide13, "Practical Demo — Part A: Distribution Simulation")
    add_footer(slide13, 13)

    # Left: Histogram image
    add_card(slide13, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    if os.path.exists("fig_histogram_overlay.png"):
        slide13.shapes.add_picture("fig_histogram_overlay.png", Inches(0.95), Inches(1.8), width=Inches(5.5))
    cap_box = slide13.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(5.4), Inches(0.5))
    tf_cap = cap_box.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Figure: 1,000 Random Samples vs Theoretical PDF N(μ=50, σ=10)"
    p_cap.font.size = Pt(10.5)
    p_cap.alignment = PP_ALIGN.CENTER
    p_cap.font.color.rgb = TEXT_MUTED

    # Right: Results table & interpretation
    add_card(slide13, Inches(6.9), Inches(1.6), Inches(5.633), Inches(5.1))
    tb13 = slide13.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(4.7))
    tf13 = tb13.text_frame
    tf13.word_wrap = True

    p = tf13.paragraphs[0]
    p.text = "Empirical vs Theoretical Moments"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(10)

    stats_lines = [
        ("Parameter", "Theoretical", "Sample (n=1000)", "Abs Error"),
        ("Mean (μ)", "50.0000", "50.1933", "0.1933 (0.38%)"),
        ("Variance (σ²)", "100.0000", "95.8864", "4.1136 (4.11%)"),
        ("Std Dev (σ)", "10.0000", "9.7922", "0.2078 (2.07%)")
    ]
    for row in stats_lines:
        p_row = tf13.add_paragraph()
        p_row.text = f"{row[0]:<15} | {row[1]:<12} | {row[2]:<15} | {row[3]}"
        p_row.font.size = Pt(11)
        p_row.font.name = "Courier New"
        if row[0] == "Parameter":
            p_row.font.bold = True
            p_row.font.color.rgb = PRIMARY
        else:
            p_row.font.color.rgb = TEXT_DARK
        p_row.space_after = Pt(4)

    p_div = tf13.add_paragraph()
    p_div.text = "─" * 45
    p_div.font.size = Pt(10)
    p_div.font.color.rgb = BORDER_COLOR
    p_div.space_after = Pt(8)

    p_int = tf13.add_paragraph()
    p_int.text = "Statistical Interpretation:"
    p_int.font.size = Pt(13)
    p_int.font.bold = True
    p_int.font.color.rgb = PRIMARY_DARK
    p_int.space_after = Pt(4)

    p_desc = tf13.add_paragraph()
    p_desc.text = "• Law of Large Numbers (LLN): As sample size n increases, the sample mean converges in probability to the true population expectation μ.\n• Histogram closely mirrors the bell curve without skew or excess kurtosis, validating our random sampling engine."
    p_desc.font.size = Pt(11)
    p_desc.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 14: Practical Demo — Part B: Gaussian NB Classifier
    # ═══════════════════════════════════════════════════════
    slide14 = prs.slides.add_slide(blank_layout)
    add_header(slide14, "Practical Demo — Part B: Gaussian NB Classifier")
    add_footer(slide14, 14)

    # Left: Decision boundary plot
    add_card(slide14, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    if os.path.exists("fig_decision_boundary.png"):
        slide14.shapes.add_picture("fig_decision_boundary.png", Inches(0.95), Inches(1.8), width=Inches(5.5))
    cap_box = slide14.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(5.4), Inches(0.5))
    tf_cap = cap_box.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Figure 14A: Learned Quadratic Decision Boundary on 2D Gaussian Features"
    p_cap.font.size = Pt(10.5)
    p_cap.alignment = PP_ALIGN.CENTER
    p_cap.font.color.rgb = TEXT_MUTED

    # Right Top: Confusion matrix plot
    add_card(slide14, Inches(6.9), Inches(1.6), Inches(5.633), Inches(2.7))
    if os.path.exists("fig_confusion_matrix.png"):
        slide14.shapes.add_picture("fig_confusion_matrix.png", Inches(7.9), Inches(1.75), height=Inches(2.2))
    cap_box = slide14.shapes.add_textbox(Inches(7.1), Inches(4.0), Inches(5.2), Inches(0.35))
    tf_cap = cap_box.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Figure 14B: Confusion Matrix (Test Split n=300)"
    p_cap.font.size = Pt(10)
    p_cap.alignment = PP_ALIGN.CENTER
    p_cap.font.color.rgb = TEXT_MUTED

    # Right Bottom: Results Card
    add_card(slide14, Inches(6.9), Inches(4.45), Inches(5.633), Inches(2.25), bg_color=HIGHLIGHT_BG, border_color=SUCCESS_COLOR)
    tb14_r = slide14.shapes.add_textbox(Inches(7.1), Inches(4.55), Inches(5.2), Inches(2.0))
    tf14_r = tb14_r.text_frame
    tf14_r.word_wrap = True

    p = tf14_r.paragraphs[0]
    p.text = "Classifier Evaluation Metrics"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = SUCCESS_COLOR
    p.space_after = Pt(4)

    p1 = tf14_r.add_paragraph()
    p1.text = "• Test Set Accuracy:  97.67%  (293 / 300 test samples correct)\n• Learned Class 0:     μ̂ = [2.01, 2.98],  σ̂² = [1.53, 1.01]\n• Learned Class 1:     μ̂ = [4.99, 6.02],  σ̂² = [1.18, 1.32]\n• Quadratic Boundary: The boundary is curved because the two classes possess different covariance structures."
    p1.font.size = Pt(10.5)
    p1.font.color.rgb = PRIMARY_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 15: Conclusion & References
    # ═══════════════════════════════════════════════════════
    slide15 = prs.slides.add_slide(blank_layout)
    bg15 = slide15.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg15.fill.solid()
    bg15.fill.fore_color.rgb = PRIMARY_DARK
    bg15.line.fill.background()

    # Title
    t_box = slide15.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(0.7))
    tf15_t = t_box.text_frame
    p = tf15_t.paragraphs[0]
    p.text = "Conclusion & Academic References"
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = RGBColor(147, 197, 253)

    # Left Card: Summary
    add_card(slide15, Inches(0.8), Inches(1.3), Inches(5.7), Inches(4.2), bg_color=RGBColor(37, 50, 75), border_color=PRIMARY)
    tb15_l = slide15.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(5.3), Inches(3.8))
    tf15_l = tb15_l.text_frame
    tf15_l.word_wrap = True

    p = tf15_l.paragraphs[0]
    p.text = "Key Takeaways"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.space_after = Pt(10)

    summary_pts = [
        ("Gaussian Distribution: ", "Foundational for modeling continuous data due to symmetry, mathematical tractability, and the Central Limit Theorem."),
        ("Model Selection Framework: ", "Match your Naive Bayes variant directly to feature type:\n  • Continuous Features → Gaussian NB\n  • Binary Indicators → Bernoulli NB\n  • Count Frequencies → Multinomial NB"),
        ("Maximum Likelihood: ", "Delivers optimal, instantaneous closed-form estimates without requiring iterative solvers.")
    ]
    for s_title, s_desc in summary_pts:
        p_s = tf15_l.add_paragraph()
        r1 = p_s.add_run()
        r1.text = "• " + s_title
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = RGBColor(147, 197, 253)
        r2 = p_s.add_run()
        r2.text = s_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = RGBColor(226, 232, 240)
        p_s.space_after = Pt(8)

    # Right Card: Limitations
    add_card(slide15, Inches(6.8), Inches(1.3), Inches(5.733), Inches(4.2), bg_color=RGBColor(37, 50, 75), border_color=RGBColor(248, 113, 113))
    tb15_r = slide15.shapes.add_textbox(Inches(7.0), Inches(1.5), Inches(5.3), Inches(3.8))
    tf15_r = tb15_r.text_frame
    tf15_r.word_wrap = True

    p = tf15_r.paragraphs[0]
    p.text = "Critical Limitations & Assumptions"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(252, 165, 165)
    p.space_after = Pt(10)

    limits = [
        ("Naive Independence Assumption: ", "Features are rarely truly independent in practice. Highly correlated features lead to overconfident probability estimates."),
        ("Normality Assumption Risk: ", "If features are multimodal, heavily skewed, or fat-tailed, Gaussian NB underperforms (consider Kernel Density Estimation or Random Forests)."),
        ("Zero-Frequency Problem: ", "Unseen categorical features produce zero likelihood; always apply additive Laplace smoothing.")
    ]
    for l_title, l_desc in limits:
        p_l = tf15_r.add_paragraph()
        r1 = p_l.add_run()
        r1.text = "⚠️ " + l_title
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = RGBColor(254, 202, 202)
        r2 = p_l.add_run()
        r2.text = l_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = RGBColor(226, 232, 240)
        p_l.space_after = Pt(8)

    # References Bottom Bar
    add_card(slide15, Inches(0.8), Inches(5.7), Inches(11.733), Inches(1.3), bg_color=RGBColor(30, 41, 59), border_color=RGBColor(71, 85, 105))
    tb15_b = slide15.shapes.add_textbox(Inches(1.0), Inches(5.75), Inches(11.333), Inches(1.2))
    tf15_b = tb15_b.text_frame
    p_ref_h = tf15_b.paragraphs[0]
    p_ref_h.text = "Academic References:"
    p_ref_h.font.size = Pt(10)
    p_ref_h.font.bold = True
    p_ref_h.font.color.rgb = RGBColor(148, 163, 184)

    refs = (
        "[1] Wackerly, D., Mendenhall, W., & Scheaffer, R. Mathematical Statistics with Applications, 7th ed., Cengage, 2008.\n"
        "[2] Bishop, C. M. Pattern Recognition and Machine Learning. Springer, 2006. | [3] Murphy, K. P. Machine Learning: A Probabilistic Perspective, MIT Press, 2012.\n"
        "[3] Pedregosa, F., et al. Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research 12, pp. 2825-2830, 2011."
    )
    p_ref = tf15_b.add_paragraph()
    p_ref.text = refs
    p_ref.font.size = Pt(9)
    p_ref.font.color.rgb = RGBColor(148, 163, 184)

    # Save
    prs.save("slides.pptx")
    print("Successfully built slides.pptx with all 15 slides and embedded figures!")

if __name__ == "__main__":
    create_deck()
