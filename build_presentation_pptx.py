import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_binomial_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette
    PRIMARY = RGBColor(37, 99, 235)      # #2563EB Blue
    PRIMARY_DARK = RGBColor(30, 41, 59)  # #1E293B Dark Slate
    ACCENT = RGBColor(124, 58, 237)      # #7C3AED Purple
    TEXT_DARK = RGBColor(30, 41, 59)     # #1E293B
    TEXT_MUTED = RGBColor(100, 116, 139) # #64748B
    CARD_BG = RGBColor(255, 255, 255)
    BORDER_COLOR = RGBColor(226, 232, 240)
    HIGHLIGHT_BG = RGBColor(238, 242, 255)
    SUCCESS_COLOR = RGBColor(16, 185, 129)
    DANGER_COLOR = RGBColor(220, 38, 38)

    def add_header(slide, title_text, category_text="GROUP 8 | THE BINOMIAL DISTRIBUTION IN ML & DATA SCIENCE"):
        top_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.08))
        top_line.fill.solid()
        top_line.fill.fore_color.rgb = PRIMARY
        top_line.line.color.rgb = PRIMARY

        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(10.5)
        p_cat.font.bold = True
        p_cat.font.color.rgb = PRIMARY

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
        p.text = "The Binomial Distribution in Machine Learning & Data Science — Group 8"
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
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = PRIMARY_DARK
    bg1.line.fill.background()

    dec1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.2), Inches(11.733), Inches(5.1))
    dec1.fill.solid()
    dec1.fill.fore_color.rgb = RGBColor(37, 50, 75)
    dec1.line.color.rgb = PRIMARY
    dec1.line.width = Pt(1.5)

    tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(1.6), Inches(11), Inches(4.3))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p0 = tf1.paragraphs[0]
    p0.text = "GROUP 8 PRESENTATION"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = RGBColor(147, 197, 253)
    p0.space_after = Pt(14)

    p1 = tf1.add_paragraph()
    p1.text = "The Binomial Distribution in\nMachine Learning & Data Science"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)
    p1.space_after = Pt(16)

    p2 = tf1.add_paragraph()
    p2.text = "Mathematical Theory, Graphical Dynamics, Maximum Likelihood, and Conversion Modeling"
    p2.font.size = Pt(16)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_after = Pt(28)

    p3 = tf1.add_paragraph()
    p3.text = "Group 8  •  Probability Distributions & Statistical Modeling Course"
    p3.font.size = Pt(13)
    p3.font.color.rgb = RGBColor(148, 163, 184)

    # ═══════════════════════════════════════════════════════
    # SLIDE 2: Why Distributions Matter in Data Science
    # ═══════════════════════════════════════════════════════
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Why Probability Distributions Matter in Data Science")
    add_footer(s2, 2)

    add_card(s2, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb2_l = s2.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf2_l = tb2_l.text_frame
    tf2_l.word_wrap = True
    
    p = tf2_l.paragraphs[0]
    p.text = "The Mathematical Engine of Data Science"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(12)

    bullets2 = [
        ("Quantify Uncertainty: ", "Every real-world survey, ad impression, and clinical trial carries natural noise. Distributions allow us to bound variability and evaluate risk."),
        ("Foundation of Machine Learning: ", "Classification, regression, and clustering algorithms optimize likelihood functions rooted in specific probability distributions."),
        ("Hypothesis Testing & Validation: ", "Provides the theoretical null distributions required to calculate p-values, verifying whether an observed lift is genuine or random luck."),
        ("Optimal Decision Making: ", "Converts raw binary counts into calibrated posterior probabilities for high-stakes business deployment decisions.")
    ]
    for b_title, b_desc in bullets2:
        p_b = tf2_l.add_paragraph()
        r1 = p_b.add_run()
        r1.text = "• " + b_title
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_b.add_run()
        r2.text = b_desc
        r2.font.size = Pt(11.5)
        r2.font.color.rgb = TEXT_DARK
        p_b.space_after = Pt(10)

    # Right Cards
    add_card(s2, Inches(6.9), Inches(1.6), Inches(5.633), Inches(2.4), bg_color=HIGHLIGHT_BG, border_color=PRIMARY)
    tb2_r1 = s2.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(2.0))
    tf2_r1 = tb2_r1.text_frame
    tf2_r1.word_wrap = True
    p = tf2_r1.paragraphs[0]
    p.text = "Distributions are the Language Data Speaks"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(8)
    p_desc = tf2_r1.add_paragraph()
    p_desc.text = "Raw data appears as random noise. Once we characterize its governing distribution, noise transforms into predictable structure, enabling anomaly detection, conversion modeling, and statistical inference."
    p_desc.font.size = Pt(12)
    p_desc.font.color.rgb = TEXT_DARK

    add_card(s2, Inches(6.9), Inches(4.3), Inches(5.633), Inches(2.4))
    tb2_r2 = s2.shapes.add_textbox(Inches(7.1), Inches(4.5), Inches(5.2), Inches(2.0))
    tf2_r2 = tb2_r2.text_frame
    tf2_r2.word_wrap = True
    p = tf2_r2.paragraphs[0]
    p.text = "The Omnipresence of Binary Events"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY_DARK
    p.space_after = Pt(8)
    p_desc = tf2_r2.add_paragraph()
    p_desc.text = "Did a user click or scroll past? Buy or abandon cart? Churn or retain? Transact normally or commit fraud? Whenever individual binary decisions aggregate over fixed cohorts, they form the Binomial Distribution."
    p_desc.font.size = Pt(12)
    p_desc.font.color.rgb = TEXT_MUTED

    # ═══════════════════════════════════════════════════════
    # SLIDE 3: Introducing the Binomial Distribution
    # ═══════════════════════════════════════════════════════
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "The Binomial Distribution: Definition & Foundations")
    add_footer(s3, 3)

    add_card(s3, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1))
    tb3 = s3.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.2), Inches(4.7))
    tf3 = tb3.text_frame
    tf3.word_wrap = True

    p = tf3.paragraphs[0]
    p.text = "Discrete Benchmark for Repeated Trials"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(10)

    b_pts = [
        ("Discrete Nature: ", "The random variable X takes on strictly non-negative integer counts from the finite support set X ∈ {0, 1, 2, ..., n}."),
        ("Formal Definition: ", "Models the exact probability of obtaining k successes across n identical, independent trials with constant success probability p."),
        ("Special Case (n = 1): ", "When n = 1, the Binomial distribution reduces to the single-trial Bernoulli distribution."),
        ("Real-World Foundation: ", "Serves as the theoretical standard for A/B testing conversion rates, digital ad click tracking, and survey polling.")
    ]
    for b_title, b_desc in b_pts:
        p_b = tf3.add_paragraph()
        r1 = p_b.add_run()
        r1.text = "• " + b_title
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_b.add_run()
        r2.text = b_desc
        r2.font.size = Pt(11.5)
        r2.font.color.rgb = TEXT_DARK
        p_b.space_after = Pt(10)

    # Right: BINS Framework
    add_card(s3, Inches(6.7), Inches(1.6), Inches(5.833), Inches(5.1))
    tb3_r = s3.shapes.add_textbox(Inches(6.9), Inches(1.8), Inches(5.4), Inches(4.7))
    tf3_r = tb3_r.text_frame
    tf3_r.word_wrap = True

    p = tf3_r.paragraphs[0]
    p.text = "The 4 Core Assumptions (BINS)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(10)

    bins_items = [
        ("B — Binary Outcomes: ", "Each trial results in strictly one of two mutually exclusive outcomes: Success (1) or Failure (0)."),
        ("I — Independent Trials: ", "The outcome of any given trial provides zero information about any other trial: P(A ∩ B) = P(A)P(B)."),
        ("N — Number of Trials Fixed: ", "The experiment consists of a predetermined, finite integer count n of trials."),
        ("S — Same Probability: ", "The probability of success p is strictly identical and constant across all trials.")
    ]
    for b_title, b_desc in bins_items:
        p_b = tf3_r.add_paragraph()
        r1 = p_b.add_run()
        r1.text = b_title
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = PRIMARY
        r2 = p_b.add_run()
        r2.text = b_desc
        r2.font.size = Pt(11.5)
        r2.font.color.rgb = TEXT_DARK
        p_b.space_after = Pt(8)

    # ═══════════════════════════════════════════════════════
    # SLIDE 4: Mathematical Formulation (PMF)
    # ═══════════════════════════════════════════════════════
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Mathematical Formulation: Probability Mass Function (PMF)")
    add_footer(s4, 4)

    # Formula Box
    add_card(s4, Inches(0.8), Inches(1.5), Inches(11.733), Inches(1.1), bg_color=HIGHLIGHT_BG, border_color=ACCENT)
    tb_f = s4.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.333), Inches(0.9))
    tf_f = tb_f.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.alignment = PP_ALIGN.CENTER
    p_f.text = "P(X = k) =  ( n! / [k! (n − k)!] ) · p^k · (1 − p)^(n − k)     for  k ∈ {0, 1, …, n}"
    p_f.font.size = Pt(21)
    p_f.font.bold = True
    p_f.font.color.rgb = ACCENT

    # Left: Parameter Table
    add_card(s4, Inches(0.8), Inches(2.8), Inches(6.5), Inches(3.9))
    tb4_l = s4.shapes.add_textbox(Inches(1.0), Inches(3.0), Inches(6.1), Inches(3.5))
    tf4_l = tb4_l.text_frame
    tf4_l.word_wrap = True
    p = tf4_l.paragraphs[0]
    p.text = "Parameter Breakdown & Symbol Mapping"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(8)

    symbols = [
        ("n ∈ ℕ", "Total number of independent trials conducted"),
        ("k ∈ [0, n]", "Specific number of successes being evaluated"),
        ("p ∈ [0, 1]", "Probability of success on any single trial"),
        ("1 − p", "Probability of failure on any single trial"),
        ("p^k (1−p)^(n−k)", "Probability of observing one specific sequence of k successes"),
        ("( n choose k )", "Binomial coefficient: total combinations of k successes")
    ]
    for sym, desc in symbols:
        p_s = tf4_l.add_paragraph()
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

    # Right: Mathematical Proof
    add_card(s4, Inches(7.6), Inches(2.8), Inches(4.933), Inches(3.9))
    tb4_r = s4.shapes.add_textbox(Inches(7.8), Inches(3.0), Inches(4.5), Inches(3.5))
    tf4_r = tb4_r.text_frame
    tf4_r.word_wrap = True
    p = tf4_r.paragraphs[0]
    p.text = "Mathematical Proof of Validity"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(8)

    p_proof = tf4_r.add_paragraph()
    p_proof.text = "By the algebraic Binomial Theorem:\n∑ (n choose k) a^k b^(n-k) = (a + b)^n\n\nSubstituting a = p and b = 1 - p:\n∑ P(X = k) = [ p + (1 − p) ]^n = (1)^n = 1.0\n\nThis proves that the total probability mass across all outcomes sums strictly to 1.0."
    p_proof.font.size = Pt(11.5)
    p_proof.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 5: Expectation & Variance
    # ═══════════════════════════════════════════════════════
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Expectation, Dispersion & Theoretical Properties")
    add_footer(s5, 5)

    add_card(s5, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb5_l = s5.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf5_l = tb5_l.text_frame
    tf5_l.word_wrap = True

    p = tf5_l.paragraphs[0]
    p.text = "Population Moments"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(8)

    p_m = tf5_l.add_paragraph()
    p_m.text = "Expected Value (Mean):   μ = E[X] = n · p"
    p_m.font.size = Pt(13)
    p_m.font.bold = True
    p_m.font.color.rgb = PRIMARY_DARK
    p_m.space_after = Pt(4)
    p_md = tf5_l.add_paragraph()
    p_md.text = "Intuition: If an ad has a 5% click rate and is shown 1,000 times, you expect exactly 1,000 × 0.05 = 50 clicks."
    p_md.font.size = Pt(11)
    p_md.font.color.rgb = TEXT_MUTED
    p_md.space_after = Pt(12)

    p_v = tf5_l.add_paragraph()
    p_v.text = "Variance:  σ² = Var(X) = n · p · (1 − p)\nStd Dev:   σ = √(n · p · (1 − p))"
    p_v.font.size = Pt(13)
    p_v.font.bold = True
    p_v.font.color.rgb = ACCENT
    p_v.space_after = Pt(4)
    p_vd = tf5_l.add_paragraph()
    p_vd.text = "Because trials are independent, variances add directly without covariance terms: Var(∑ Y_i) = ∑ Var(Y_i) = np(1-p)."
    p_vd.font.size = Pt(11)
    p_vd.font.color.rgb = TEXT_MUTED

    # Right: Variance Dynamics
    add_card(s5, Inches(6.9), Inches(1.6), Inches(5.633), Inches(5.1))
    tb5_r = s5.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(4.7))
    tf5_r = tb5_r.text_frame
    tf5_r.word_wrap = True

    p = tf5_r.paragraphs[0]
    p.text = "Variance Dynamics & Risk Insight"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = SUCCESS_COLOR
    p.space_after = Pt(8)

    v_pts = [
        ("Peak Uncertainty at p = 0.5: ", "The term p(1-p) achieves its global maximum at p = 0.5 (0.25). A coin flip has the highest outcome entropy."),
        ("Zero Variance at Extremes: ", "As p approaches 0.0 or 1.0, variance drops to 0. When an event is impossible or guaranteed, dispersion vanishes."),
        ("Linearity of Expectation: ", "Even if trials exhibit weak correlation, E[X] = np remains exact because expectation is always strictly linear."),
        ("Standard Deviation Scaling: ", "Spread grows with √n rather than n. A 4x increase in trials only doubles the absolute spread!")
    ]
    for v_title, v_desc in v_pts:
        p_b = tf5_r.add_paragraph()
        r1 = p_b.add_run()
        r1.text = "• " + v_title
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_b.add_run()
        r2.text = v_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_b.space_after = Pt(8)

    # ═══════════════════════════════════════════════════════
    # SLIDE 6: Shape Dynamics (Varying p)
    # ═══════════════════════════════════════════════════════
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Shape Dynamics: How Success Probability Governs Skewness")
    add_footer(s6, 6)

    add_card(s6, Inches(0.8), Inches(1.5), Inches(11.733), Inches(3.6))
    if os.path.exists("fig_binomial_pmf_variations.png"):
        s6.shapes.add_picture("fig_binomial_pmf_variations.png", Inches(0.95), Inches(1.6), width=Inches(11.4))

    add_card(s6, Inches(0.8), Inches(5.3), Inches(5.7), Inches(1.5), bg_color=HIGHLIGHT_BG, border_color=PRIMARY)
    tb6_l = s6.shapes.add_textbox(Inches(1.0), Inches(5.35), Inches(5.3), Inches(1.4))
    tf6_l = tb6_l.text_frame
    tf6_l.word_wrap = True
    p = tf6_l.paragraphs[0]
    p.text = "Skewness Interpretation:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p1 = tf6_l.add_paragraph()
    p1.text = "• p < 0.5: Right-skewed (success is rare; mass near 0).\n• p = 0.5: Perfectly symmetric bell shape (skewness = 0).\n• p > 0.5: Left-skewed (success is common; mass near n)."
    p1.font.size = Pt(10.5)
    p1.font.color.rgb = TEXT_DARK

    add_card(s6, Inches(6.8), Inches(5.3), Inches(5.733), Inches(1.5))
    tb6_r = s6.shapes.add_textbox(Inches(7.0), Inches(5.35), Inches(5.3), Inches(1.4))
    tf6_r = tb6_r.text_frame
    tf6_r.word_wrap = True
    p = tf6_r.paragraphs[0]
    p.text = "Mathematical Skewness Formula:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p1 = tf6_r.add_paragraph()
    p1.text = "γ₁ = (1 − 2p) / √(np(1 − p))\nNotice that as n grows large, the denominator √n drives skewness toward zero regardless of p, smoothly enforcing symmetry!"
    p1.font.size = Pt(10.5)
    p1.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 7: Trial Scaling & CDF
    # ═══════════════════════════════════════════════════════
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Scale Dynamics & Cumulative Density (CDF)")
    add_footer(s7, 7)

    # Left: n variations
    add_card(s7, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.1))
    if os.path.exists("fig_binomial_n_variations.png"):
        s7.shapes.add_picture("fig_binomial_n_variations.png", Inches(0.95), Inches(1.8), width=Inches(5.4))
    tb7_l = s7.shapes.add_textbox(Inches(1.0), Inches(4.7), Inches(5.3), Inches(1.8))
    tf7_l = tb7_l.text_frame
    tf7_l.word_wrap = True
    p = tf7_l.paragraphs[0]
    p.text = "Trial Scaling Dynamics:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p1 = tf7_l.add_paragraph()
    p1.text = "• Increasing n (10 → 30 → 100) increases absolute spread (σ ∝ √n).\n• Relative spread (σ / μ ∝ 1/√n) shrinks, concentrating sample proportions tightly around p."
    p1.font.size = Pt(10.5)
    p1.font.color.rgb = TEXT_DARK

    # Right: CDF plot
    add_card(s7, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.1))
    if os.path.exists("fig_binomial_cdf.png"):
        s7.shapes.add_picture("fig_binomial_cdf.png", Inches(7.0), Inches(1.8), width=Inches(5.3))
    tb7_r = s7.shapes.add_textbox(Inches(7.0), Inches(5.1), Inches(5.3), Inches(1.4))
    tf7_r = tb7_r.text_frame
    tf7_r.word_wrap = True
    p = tf7_r.paragraphs[0]
    p.text = "Cumulative Distribution Function: F(k) = P(X ≤ k)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p1 = tf7_r.add_paragraph()
    p1.text = "• Discrete step function: jumps at each integer k by P(X = k).\n• At k = 12, cumulative probability reaches 57%, crossing the median threshold."
    p1.font.size = Pt(10.5)
    p1.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 8: The Normal Approximation
    # ═══════════════════════════════════════════════════════
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Bridging Discrete & Continuous: De Moivre–Laplace Limit")
    add_footer(s8, 8)

    # Left: Plot
    add_card(s8, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    if os.path.exists("fig_normal_approximation.png"):
        s8.shapes.add_picture("fig_normal_approximation.png", Inches(0.95), Inches(1.8), width=Inches(5.5))
    cap_box = s8.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(5.4), Inches(0.5))
    tf_cap = cap_box.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Figure 8: Binomial(n=50, p=0.4) smoothly approximated by Normal N(20, 12)"
    p_cap.font.size = Pt(10)
    p_cap.alignment = PP_ALIGN.CENTER
    p_cap.font.color.rgb = TEXT_MUTED

    # Right: Concept
    add_card(s8, Inches(6.9), Inches(1.6), Inches(5.633), Inches(5.1))
    tb8 = s8.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(4.7))
    tf8 = tb8.text_frame
    tf8.word_wrap = True

    p = tf8.paragraphs[0]
    p.text = "The De Moivre–Laplace Theorem"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(8)

    p1 = tf8.add_paragraph()
    p1.text = "Historically discovered in 1738, the Gaussian bell curve was derived as an analytical approximation to Binomial coefficients for large n:"
    p1.font.size = Pt(11)
    p1.space_after = Pt(6)

    p_f = tf8.add_paragraph()
    p_f.text = "Binomial(n, p)  ≈  N( μ = np,   σ² = np(1 − p) )"
    p_f.font.size = Pt(12)
    p_f.font.bold = True
    p_f.font.color.rgb = ACCENT
    p_f.space_after = Pt(10)

    ap_pts = [
        ("Rule of Thumb: ", "Accurate when both np ≥ 10 and n(1 - p) ≥ 10."),
        ("Continuity Correction: ", "Adjust discrete boundaries by ± 0.5 to convert discrete bars into continuous area: P(a ≤ X ≤ b) ≈ P(a - 0.5 ≤ X_norm ≤ b + 0.5)."),
        ("Computational Advantage: ", "Avoids computing astronomically large factorials like 1,000! during statistical inference.")
    ]
    for a_title, a_desc in ap_pts:
        p_b = tf8.add_paragraph()
        r1 = p_b.add_run()
        r1.text = "• " + a_title
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_b.add_run()
        r2.text = a_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_b.space_after = Pt(6)

    # ═══════════════════════════════════════════════════════
    # SLIDE 9: Likelihood & MLE
    # ═══════════════════════════════════════════════════════
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Parameter Estimation via Maximum Likelihood Estimation (MLE)")
    add_footer(s9, 9)

    add_card(s9, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb9_l = s9.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf9_l = tb9_l.text_frame
    tf9_l.word_wrap = True

    p = tf9_l.paragraphs[0]
    p.text = "The Likelihood Formulation"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(8)

    p1 = tf9_l.add_paragraph()
    p1.text = "In real-world data science, p is unknown. We observe k successes in n trials and seek the parameter value that maximizes the likelihood of having generated the data:"
    p1.font.size = Pt(11)
    p1.space_after = Pt(6)

    p_f1 = tf9_l.add_paragraph()
    p_f1.text = "L(p | k) = (n choose k) · p^k · (1 − p)^(n − k)"
    p_f1.font.size = Pt(11.5)
    p_f1.font.bold = True
    p_f1.font.color.rgb = ACCENT
    p_f1.space_after = Pt(8)

    p2 = tf9_l.add_paragraph()
    p2.text = "Taking the log to obtain the Log-Likelihood:"
    p2.font.size = Pt(11)
    p2.space_after = Pt(4)

    p_f2 = tf9_l.add_paragraph()
    p_f2.text = "ln L(p) = ln(n choose k) + k ln(p) + (n − k) ln(1 − p)"
    p_f2.font.size = Pt(11)
    p_f2.font.bold = True
    p_f2.font.color.rgb = PRIMARY

    # Right: Derivation
    add_card(s9, Inches(6.9), Inches(1.6), Inches(5.633), Inches(5.1))
    tb9_r = s9.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(4.7))
    tf9_r = tb9_r.text_frame
    tf9_r.word_wrap = True

    p = tf9_r.paragraphs[0]
    p.text = "Analytical Solution & Optimality"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = SUCCESS_COLOR
    p.space_after = Pt(8)

    p1 = tf9_r.add_paragraph()
    p1.text = "Setting the derivative with respect to p to zero:\nd(ln L) / dp = (k / p) − (n − k) / (1 − p) = 0"
    p1.font.size = Pt(11.5)
    p1.space_after = Pt(8)

    p_opt = tf9_r.add_paragraph()
    p_opt.text = "p̂_MLE = k / n = (Observed Successes) / (Total Trials)"
    p_opt.font.size = Pt(13)
    p_opt.font.bold = True
    p_opt.font.color.rgb = PRIMARY
    p_opt.space_after = Pt(12)

    p_prop = tf9_r.add_paragraph()
    p_prop.text = "Theoretical Guarantees of p̂_MLE:\n• Unbiased: E[p̂] = E[k]/n = np/n = p\n• Minimum Variance: Achieves the Cramér-Rao Lower Bound\n• Asymptotically Efficient: Variance converges to p(1-p)/n as n grows"
    p_prop.font.size = Pt(11)
    p_prop.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 10: Application 1 — A/B Testing
    # ═══════════════════════════════════════════════════════
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Application 1: A/B Testing in Digital Product Analytics")
    add_footer(s10, 10)

    add_card(s10, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb10_l = s10.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf10_l = tb10_l.text_frame
    tf10_l.word_wrap = True

    p = tf10_l.paragraphs[0]
    p.text = "Online Controlled Experimentation"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(10)

    ab_steps = [
        ("The Business Setup: ", "Testing whether a redesigned checkout page (Variant B) drives more purchases than the existing layout (Control A)."),
        ("Binomial Allocation: ", "Incoming users are randomly split: X_A ~ Binomial(n_A, p_A) and X_B ~ Binomial(n_B, p_B)."),
        ("Hypothesis Formulation: ", "Null Hypothesis H_0: p_B ≤ p_A (No lift) vs. Alternative Hypothesis H_1: p_B > p_A (Real lift)."),
        ("Two-Proportion Z-Test: ", "Statisticians evaluate the Z-score using pooled variance to decide if the lift is statistically significant (p < 0.05).")
    ]
    for s_title, s_desc in ab_steps:
        p_s = tf10_l.add_paragraph()
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

    # Right: Formula & Impact
    add_card(s10, Inches(6.9), Inches(1.6), Inches(5.633), Inches(2.6), bg_color=HIGHLIGHT_BG, border_color=PRIMARY)
    tb10_r1 = s10.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(2.2))
    tf10_r1 = tb10_r1.text_frame
    tf10_r1.word_wrap = True
    p = tf10_r1.paragraphs[0]
    p.text = "Two-Proportion Z-Test Formula"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(6)
    p1 = tf10_r1.add_paragraph()
    p1.text = "Z = (p̂_B − p̂_A) / √[ p̂(1−p̂)(1/n_A + 1/n_B) ]\n\nWhere p̂ is the pooled conversion rate across all cohorts."
    p1.font.size = Pt(11.5)
    p1.font.color.rgb = TEXT_DARK

    add_card(s10, Inches(6.9), Inches(4.4), Inches(5.633), Inches(2.3))
    tb10_r2 = s10.shapes.add_textbox(Inches(7.1), Inches(4.6), Inches(5.2), Inches(1.9))
    tf10_r2 = tb10_r2.text_frame
    tf10_r2.word_wrap = True
    p = tf10_r2.paragraphs[0]
    p.text = "Industry Scale"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(6)
    p1 = tf10_r2.add_paragraph()
    p1.text = "Platforms like Netflix, Amazon, Meta, and Google run tens of thousands of simultaneous Binomial A/B experiments annually to guide multi-million dollar product deployment decisions."
    p1.font.size = Pt(11)
    p1.font.color.rgb = TEXT_MUTED

    # ═══════════════════════════════════════════════════════
    # SLIDE 11: Application 2 — CTR in Ad Tech
    # ═══════════════════════════════════════════════════════
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Application 2: Click-Through-Rate (CTR) & Auction Engines")
    add_footer(s11, 11)

    add_card(s11, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb11_l = s11.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf11_l = tb11_l.text_frame
    tf11_l.word_wrap = True

    p = tf11_l.paragraphs[0]
    p.text = "Real-Time Ad Auction Optimization"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(10)

    ad_steps = [
        ("The Impression Funnel: ", "Every ad display is an independent opportunity (n). The user clicking is a binary outcome with probability p = pCTR."),
        ("Binomial Modeling: ", "Total clicks follow k ~ Binomial(n, pCTR). Expected clicks = n × pCTR."),
        ("Auction Ranking: ", "Bidding engines evaluate ads by Expected Revenue = n × pCTR × Bid Price."),
        ("Poisson Bridge: ", "When impressions reach millions (n → ∞) and click probability is small (p < 0.01), Binomial converges to Poisson(λ = np).")
    ]
    for s_title, s_desc in ad_steps:
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

    # Right: Revenue equation & calibration
    add_card(s11, Inches(6.9), Inches(1.6), Inches(5.633), Inches(2.6), bg_color=HIGHLIGHT_BG, border_color=PRIMARY)
    tb11_r1 = s11.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(2.2))
    tf11_r1 = tb11_r1.text_frame
    tf11_r1.word_wrap = True
    p = tf11_r1.paragraphs[0]
    p.text = "Expected Revenue Formulation"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(6)
    p1 = tf11_r1.add_paragraph()
    p1.text = "Expected Value = n · pCTR · Cost-Per-Click Bid\n\nAd platforms run machine learning models (gradient boosted trees, deep neural nets) specifically to estimate the Binomial parameter pCTR."
    p1.font.size = Pt(11.5)
    p1.font.color.rgb = TEXT_DARK

    add_card(s11, Inches(6.9), Inches(4.4), Inches(5.633), Inches(2.3))
    tb11_r2 = s11.shapes.add_textbox(Inches(7.1), Inches(4.6), Inches(5.2), Inches(1.9))
    tf11_r2 = tb11_r2.text_frame
    tf11_r2.word_wrap = True
    p = tf11_r2.paragraphs[0]
    p.text = "Calibration Challenge"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(6)
    p1 = tf11_r2.add_paragraph()
    p1.text = "Because click rates are low (0.1% to 2.0%), slight miscalibration in p leads to massive financial losses in automated second-price auctions. Calibration curves are checked continuously."
    p1.font.size = Pt(11)
    p1.font.color.rgb = TEXT_MUTED

    # ═══════════════════════════════════════════════════════
    # SLIDE 12: Application 3 — Logistic Regression
    # ═══════════════════════════════════════════════════════
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Application 3: The Engine of Logistic Regression")
    add_footer(s12, 12)

    add_card(s12, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    tb12_l = s12.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.7))
    tf12_l = tb12_l.text_frame
    tf12_l.word_wrap = True

    p = tf12_l.paragraphs[0]
    p.text = "Generalized Linear Binomial Model"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(10)

    lr_steps = [
        ("Binary Prediction: ", "In classification, we want to predict p(x) = P(Y = 1 | x) conditioned on features x."),
        ("Logit Link: ", "Instead of assuming constant p, Logistic Regression models the log-odds linearly: ln[ p(x) / (1 − p(x)) ] = β^T x."),
        ("Sigmoid Inversion: ", "Inverting the logit yields the standard Sigmoid function: p(x) = 1 / (1 + e^(−β^T x))."),
        ("Loss Equivalence: ", "Binary Cross-Entropy (BCE) loss is mathematically identical to the negative log-likelihood of independent Binomial trials!")
    ]
    for s_title, s_desc in lr_steps:
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

    # Right: Formula & Takeaway
    add_card(s12, Inches(6.9), Inches(1.6), Inches(5.633), Inches(2.6), bg_color=HIGHLIGHT_BG, border_color=PRIMARY)
    tb12_r1 = s12.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(2.2))
    tf12_r1 = tb12_r1.text_frame
    tf12_r1.word_wrap = True
    p = tf12_r1.paragraphs[0]
    p.text = "Binary Cross-Entropy (BCE) Loss"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(6)
    p1 = tf12_r1.add_paragraph()
    p1.text = "Loss = − ∑ [ y_i ln(p_i) + (1 − y_i) ln(1 − p_i) ]\n\nDirectly derived from the negative log-likelihood of Bernoulli/Binomial outcomes!"
    p1.font.size = Pt(11.5)
    p1.font.color.rgb = TEXT_DARK

    add_card(s12, Inches(6.9), Inches(4.4), Inches(5.633), Inches(2.3))
    tb12_r2 = s12.shapes.add_textbox(Inches(7.1), Inches(4.6), Inches(5.2), Inches(1.9))
    tf12_r2 = tb12_r2.text_frame
    tf12_r2.word_wrap = True
    p = tf12_r2.paragraphs[0]
    p.text = "Deep Learning Foundation"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = SUCCESS_COLOR
    p.space_after = Pt(6)
    p1 = tf12_r2.add_paragraph()
    p1.text = "Every neural network performing binary classification with a Sigmoid output layer is actively estimating a parameter for a Bernoulli/Binomial trial. The Binomial distribution is alive in modern AI."
    p1.font.size = Pt(11)
    p1.font.color.rgb = TEXT_MUTED

    # ═══════════════════════════════════════════════════════
    # SLIDE 13: Practical Demo Part A (1000 Samples)
    # ═══════════════════════════════════════════════════════
    s13 = prs.slides.add_slide(blank_layout)
    add_header(s13, "Practical Demo — Part A: 1,000-Observation Simulation")
    add_footer(s13, 13)

    # Left: Simulation plot
    add_card(s13, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    if os.path.exists("fig_binomial_simulation.png"):
        s13.shapes.add_picture("fig_binomial_simulation.png", Inches(0.95), Inches(1.8), width=Inches(5.5))
    cap_box = s13.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(5.4), Inches(0.5))
    tf_cap = cap_box.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Figure 13: 1,000 Simulated Samples vs Theoretical PMF (n=20, p=0.6)"
    p_cap.font.size = Pt(10.5)
    p_cap.alignment = PP_ALIGN.CENTER
    p_cap.font.color.rgb = TEXT_MUTED

    # Right: Comparison Table
    add_card(s13, Inches(6.9), Inches(1.6), Inches(5.633), Inches(5.1))
    tb13 = s13.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(4.7))
    tf13 = tb13.text_frame
    tf13.word_wrap = True

    p = tf13.paragraphs[0]
    p.text = "Empirical vs Theoretical Moments"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(10)

    stats_lines = [
        ("Metric", "Theoretical", "Simulated (N=1000)", "Error"),
        ("Mean (μ = np)", "12.0000", "12.0720", "0.0720 (0.60%)"),
        ("Variance (σ²)", "4.8000", "4.8076", "0.0076 (0.16%)"),
        ("Std Dev (σ)", "2.1909", "2.1926", "0.0017 (0.08%)"),
        ("MLE Param (p̂)", "0.6000", "0.6036", "0.0036 (0.60%)")
    ]
    for row in stats_lines:
        p_row = tf13.add_paragraph()
        p_row.text = f"{row[0]:<15} | {row[1]:<12} | {row[2]:<16} | {row[3]}"
        p_row.font.size = Pt(11)
        p_row.font.name = "Courier New"
        if row[0] == "Metric":
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
    p_desc.text = "• Weak Law of Large Numbers (WLLN): With N=1,000 samples, empirical frequencies tightly align with theoretical PMF values.\n• Closed-form MLE p̂ = 12.072 / 20 = 0.6036 recovers true p with 99.4% accuracy."
    p_desc.font.size = Pt(11)
    p_desc.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 14: Practical Demo Part B (A/B Testing)
    # ═══════════════════════════════════════════════════════
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Practical Demo — Part B: Applied A/B Testing Evaluation")
    add_footer(s14, 14)

    # Left: Plot
    add_card(s14, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    if os.path.exists("fig_ab_testing_distributions.png"):
        s14.shapes.add_picture("fig_ab_testing_distributions.png", Inches(0.95), Inches(1.8), width=Inches(5.5))
    cap_box = s14.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(5.4), Inches(0.5))
    tf_cap = cap_box.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Figure 14: Conversion Distributions for Layout A (10%) vs. Layout B (13%)"
    p_cap.font.size = Pt(10)
    p_cap.alignment = PP_ALIGN.CENTER
    p_cap.font.color.rgb = TEXT_MUTED

    # Right: Statistical inference card
    add_card(s14, Inches(6.9), Inches(1.6), Inches(5.633), Inches(5.1), bg_color=HIGHLIGHT_BG, border_color=SUCCESS_COLOR)
    tb14_r = s14.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(4.7))
    tf14_r = tb14_r.text_frame
    tf14_r.word_wrap = True

    p = tf14_r.paragraphs[0]
    p.text = "A/B Testing Statistical Results"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = SUCCESS_COLOR
    p.space_after = Pt(10)

    ab_res = [
        ("Control (Layout A): ", "n = 1,000 visitors, 100 conversions (p_A = 10.0%)"),
        ("Variant (Layout B): ", "n = 1,000 visitors, 130 conversions (p_B = 13.0%)"),
        ("Observed Lift: ", "+3.00% absolute lift (+30.0% relative improvement)"),
        ("Test Statistic: ", "Pooled Z-Score = 2.1051"),
        ("p-Value: ", "0.0176 (1.76%)")
    ]
    for r_title, r_desc in ab_res:
        p_r = tf14_r.add_paragraph()
        r1 = p_r.add_run()
        r1.text = "• " + r_title
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_r.add_run()
        r2.text = r_desc
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_r.space_after = Pt(6)

    p_dec = tf14_r.add_paragraph()
    p_dec.text = "\nBusiness Decision:"
    p_dec.font.size = Pt(13)
    p_dec.font.bold = True
    p_dec.font.color.rgb = PRIMARY
    p_dec.space_after = Pt(4)

    p_decd = tf14_r.add_paragraph()
    p_decd.text = "Because p-value (0.0176) < 0.05, we reject the null hypothesis H_0 at the 95% confidence level. The platform should deploy Layout B immediately."
    p_decd.font.size = Pt(11)
    p_decd.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 15: Conclusion & References
    # ═══════════════════════════════════════════════════════
    s15 = prs.slides.add_slide(blank_layout)
    bg15 = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg15.fill.solid()
    bg15.fill.fore_color.rgb = PRIMARY_DARK
    bg15.line.fill.background()

    t_box = s15.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(0.7))
    tf15_t = t_box.text_frame
    p = tf15_t.paragraphs[0]
    p.text = "Conclusion, Real-World Limitations & Academic References"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = RGBColor(147, 197, 253)

    # Left: Summary
    add_card(s15, Inches(0.8), Inches(1.3), Inches(5.7), Inches(4.2), bg_color=RGBColor(37, 50, 75), border_color=PRIMARY)
    tb15_l = s15.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(5.3), Inches(3.8))
    tf15_l = tb15_l.text_frame
    tf15_l.word_wrap = True

    p = tf15_l.paragraphs[0]
    p.text = "Core Takeaways"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    p.space_after = Pt(10)

    summary_pts = [
        ("The Discrete Cornerstone: ", "The Binomial distribution is the mathematical standard for modeling discrete binary counts and conversion funnels."),
        ("Bridge to Machine Learning: ", "Connects discrete experiments to continuous AI via the De Moivre-Laplace theorem and Logistic Regression logit links."),
        ("Instant Parameter Estimation: ", "Closed-form MLE p̂ = k/n provides unbiased, optimal estimates without iterative gradient descent.")
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

    # Right: Limitations
    add_card(s15, Inches(6.8), Inches(1.3), Inches(5.733), Inches(4.2), bg_color=RGBColor(37, 50, 75), border_color=RGBColor(248, 113, 113))
    tb15_r = s15.shapes.add_textbox(Inches(7.0), Inches(1.5), Inches(5.3), Inches(3.8))
    tf15_r = tb15_r.text_frame
    tf15_r.word_wrap = True

    p = tf15_r.paragraphs[0]
    p.text = "Critical Real-World Limitations"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor(252, 165, 165)
    p.space_after = Pt(10)

    limits = [
        ("Violation of Independence: ", "Viral loops, social contagion, and referral networks violate the 'I' assumption in BINS."),
        ("Probability Drift (Non-Constant p): ", "Conversion rates fluctuate by time of day, season, and campaign fatigue, violating constant p."),
        ("Overdispersion: ", "When real-world variance exceeds np(1-p), models must upgrade to Beta-Binomial distributions.")
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

    # Bottom: References
    add_card(s15, Inches(0.8), Inches(5.7), Inches(11.733), Inches(1.3), bg_color=RGBColor(30, 41, 59), border_color=RGBColor(71, 85, 105))
    tb15_b = s15.shapes.add_textbox(Inches(1.0), Inches(5.75), Inches(11.333), Inches(1.2))
    tf15_b = tb15_b.text_frame
    p_ref_h = tf15_b.paragraphs[0]
    p_ref_h.text = "Academic References:"
    p_ref_h.font.size = Pt(10)
    p_ref_h.font.bold = True
    p_ref_h.font.color.rgb = RGBColor(148, 163, 184)

    refs = (
        "[1] Wackerly, D., Mendenhall, W., & Scheaffer, R. Mathematical Statistics with Applications, 7th ed., Cengage, 2008.\n"
        "[2] Montgomery, D. C., & Runger, G. C. Applied Statistics and Probability for Engineers, 7th ed., Wiley, 2018. | [3] Bishop, C. M. Pattern Recognition and Machine Learning, Springer, 2006.\n"
        "[4] Kohavi, R., Tang, D., & Xu, Y. Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing, Cambridge University Press, 2020."
    )
    p_ref = tf15_b.add_paragraph()
    p_ref.text = refs
    p_ref.font.size = Pt(9)
    p_ref.font.color.rgb = RGBColor(148, 163, 184)

    prs.save("slides.pptx")
    print("Successfully built new 15-slide Binomial deck in slides.pptx!")

if __name__ == "__main__":
    create_binomial_deck()
