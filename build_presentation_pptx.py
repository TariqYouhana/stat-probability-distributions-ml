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

    def add_header(slide, title_text, category_text="GROUP 8 | BINOMIAL & NEGATIVE BINOMIAL IN ML & DATA SCIENCE"):
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
        p.text = "Binomial & Negative Binomial Distributions in Machine Learning & Data Science — Group 8"
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
    p1.text = "Binomial & Negative Binomial Distributions\nin Machine Learning & Data Science"
    p1.font.size = Pt(34)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)
    p1.space_after = Pt(14)

    p2 = tf1.add_paragraph()
    p2.text = "Complementary Views, Overdispersion Modeling, and Empirical Simulation"
    p2.font.size = Pt(15)
    p2.font.color.rgb = RGBColor(226, 232, 240)
    p2.space_after = Pt(18)

    p3 = tf1.add_paragraph()
    p3.text = "STA293 | Probability Distribution | Fall'26 | Section 2  •  Submitted to: Afsana Al Sharmin"
    p3.font.size = Pt(13)
    p3.font.bold = True
    p3.font.color.rgb = RGBColor(147, 197, 253)
    p3.space_after = Pt(10)

    p4 = tf1.add_paragraph()
    p4.text = "Group 8 Members: Tasfia Rahman Rodoshi [ID], Tariq Youhana Leon [ID], Shinjiny Anan Apsora [ID], Moumita Akter Mou [ID], Rehnuma Tasnim [ID]"
    p4.font.size = Pt(11.5)
    p4.font.color.rgb = RGBColor(203, 213, 225)

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
        ("Discrete Nature: ", "The random variable X takes integer counts from the finite support set X ∈ {0, 1, 2, ..., n}."),
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
    add_header(s4, "Mathematical Formulation: Probability Mass Function (PMF) [1]")
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
    add_header(s5, "Expectation, Dispersion & Theoretical Properties [1]")
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
        ("Underdispersion (σ² < μ): ", "Because (1 - p) < 1, Binomial variance is always strictly less than its mean."),
        ("Peak Uncertainty at p = 0.5: ", "The term p(1-p) achieves its global maximum at p = 0.5 (0.25) and vanishes at p = 0 or 1."),
        ("Linearity of Expectation: ", "Even if trials exhibit weak correlation, E[X] = np remains exact because expectation is strictly linear."),
        ("MLE Estimator: ", "Closed-form Maximum Likelihood Estimator is the sample proportion: p̂_MLE = k / n.")
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
    p1.text = "• Discrete step function: jumps at each integer k by P(X = k).\n• At k = 12, cumulative probability reaches 58%, crossing the median."
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
    # SLIDE 9: Introducing the Negative Binomial Distribution
    # ═══════════════════════════════════════════════════════
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "The Negative Binomial Distribution: Definition & PMF [1]")
    add_footer(s9, 9)

    # Top Formula Banner
    add_card(s9, Inches(0.8), Inches(1.5), Inches(11.733), Inches(1.0), bg_color=HIGHLIGHT_BG, border_color=ACCENT)
    tb9_f = s9.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(11.333), Inches(0.75))
    tf9_f = tb9_f.text_frame
    p9_f = tf9_f.paragraphs[0]
    p9_f.text = "PMF:   P(X = k) = (k + r − 1 choose k) · p^r · (1 − p)^k     for  k ∈ {0, 1, 2, ... ∞}"
    p9_f.font.size = Pt(18)
    p9_f.font.bold = True
    p9_f.font.color.rgb = ACCENT
    p9_f.alignment = PP_ALIGN.CENTER

    # Left: Flipped Question
    add_card(s9, Inches(0.8), Inches(2.7), Inches(5.8), Inches(4.0))
    tb9_l = s9.shapes.add_textbox(Inches(1.0), Inches(2.9), Inches(5.4), Inches(3.6))
    tf9_l = tb9_l.text_frame
    tf9_l.word_wrap = True
    p = tf9_l.paragraphs[0]
    p.text = "The Flipped Question"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(8)

    nb_pts = [
        ("Opposite Framing: ", "Instead of fixing trials n and counting successes, we fix target successes r and count failures X = k before the r-th success."),
        ("Convention: ", "X = number of failures before the r-th success (X = 0, 1, 2, ...). If we count total trials Y = X + r instead, E[Y] = r/p; the variance is unchanged."),
        ("Special Case (r = 1): ", "When r = 1, Negative Binomial reduces directly to the Geometric(p) distribution.")
    ]
    for title_t, desc_t in nb_pts:
        p_n = tf9_l.add_paragraph()
        r1 = p_n.add_run()
        r1.text = "• " + title_t
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_n.add_run()
        r2.text = desc_t
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_n.space_after = Pt(8)

    # Right: Parameter Table
    add_card(s9, Inches(6.9), Inches(2.7), Inches(5.633), Inches(4.0))
    tb9_r = s9.shapes.add_textbox(Inches(7.1), Inches(2.9), Inches(5.2), Inches(3.6))
    tf9_r = tb9_r.text_frame
    tf9_r.word_wrap = True
    p = tf9_r.paragraphs[0]
    p.text = "Parameters & Combinatorial Logic"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(8)

    nb_params = [
        ("r ∈ {1, 2, 3, ...}: ", "Fixed target number of successes required to stop (a positive integer)."),
        ("k ∈ {0, 1, 2, ...}: ", "Unbounded count of failures observed before the r-th success."),
        ("p ∈ (0, 1]: ", "Constant probability of success on each independent trial."),
        ("Combinatorial Term: ", "The final trial must be the r-th success; (k + r − 1 choose k) arranges k failures across the preceding k + r − 1 trials.")
    ]
    for title_t, desc_t in nb_params:
        p_n = tf9_r.add_paragraph()
        r1 = p_n.add_run()
        r1.text = "• " + title_t
        r1.font.bold = True
        r1.font.size = Pt(11.5)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_n.add_run()
        r2.text = desc_t
        r2.font.size = Pt(11)
        r2.font.color.rgb = TEXT_DARK
        p_n.space_after = Pt(8)

    # ═══════════════════════════════════════════════════════
    # SLIDE 10: Negative Binomial Properties, Overdispersion & Graphs
    # ═══════════════════════════════════════════════════════
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Negative Binomial: Moments, Overdispersion & Shape [1, 3]")
    add_footer(s10, 10)

    add_card(s10, Inches(0.8), Inches(1.45), Inches(11.733), Inches(3.75))
    if os.path.exists("fig_negbinom_pmf_variations.png"):
        s10.shapes.add_picture("fig_negbinom_pmf_variations.png", Inches(1.2), Inches(1.52), width=Inches(10.9))

    # Bottom Left: Moments & MLE
    add_card(s10, Inches(0.8), Inches(5.35), Inches(5.7), Inches(1.55))
    tb10_l = s10.shapes.add_textbox(Inches(1.0), Inches(5.45), Inches(5.3), Inches(1.35))
    tf10_l = tb10_l.text_frame
    tf10_l.word_wrap = True
    p = tf10_l.paragraphs[0]
    p.text = "Moments & MLE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(4)
    p1 = tf10_l.add_paragraph()
    p1.text = "Mean: μ = r(1 − p)/p   |   Var: σ² = r(1 − p)/p² = μ + μ²/r\nMLE Estimator: p̂_MLE = r / (r + x̄)"
    p1.font.size = Pt(11.5)
    p1.font.color.rgb = TEXT_DARK

    # Bottom Right: Overdispersion Highlight
    add_card(s10, Inches(6.8), Inches(5.35), Inches(5.733), Inches(1.55), bg_color=HIGHLIGHT_BG, border_color=ACCENT)
    tb10_r = s10.shapes.add_textbox(Inches(7.0), Inches(5.45), Inches(5.3), Inches(1.35))
    tf10_r = tb10_r.text_frame
    tf10_r.word_wrap = True
    p = tf10_r.paragraphs[0]
    p.text = "Mechanism & Overdispersion (σ² > μ) [3]"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(4)
    p1 = tf10_r.add_paragraph()
    p1.text = "NB arises as a Poisson-Gamma mixture: X | λ ~ Poisson(λ), λ ~ Gamma(shape r, scale (1-p)/p). Hence Var = mean + mean² / r > mean."
    p1.font.size = Pt(11)
    p1.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 11: Positive vs Negative Binomial Duality
    # ═══════════════════════════════════════════════════════
    s11 = prs.slides.add_slide(blank_layout)
    add_header(s11, "Binomial vs. Negative Binomial: Complementary Views")
    add_footer(s11, 11)

    # Left: Comparison Figure
    add_card(s11, Inches(0.8), Inches(1.55), Inches(6.3), Inches(5.2))
    if os.path.exists("fig_comparison_pos_neg.png"):
        s11.shapes.add_picture("fig_comparison_pos_neg.png", Inches(0.92), Inches(1.85), width=Inches(6.05))
    cap11 = s11.shapes.add_textbox(Inches(1.0), Inches(6.15), Inches(5.9), Inches(0.45))
    p_c11 = cap11.text_frame.paragraphs[0]
    p_c11.text = "Figure 11: Underdispersed Binomial vs. Overdispersed Negative Binomial"
    p_c11.font.size = Pt(10)
    p_c11.alignment = PP_ALIGN.CENTER
    p_c11.font.color.rgb = TEXT_MUTED

    # Right: Duality Table + ML Bridge
    add_card(s11, Inches(7.3), Inches(1.55), Inches(5.233), Inches(3.25))
    tb11_t = s11.shapes.add_textbox(Inches(7.45), Inches(1.68), Inches(4.95), Inches(3.0))
    tf11_t = tb11_t.text_frame
    tf11_t.word_wrap = True
    p = tf11_t.paragraphs[0]
    p.text = "Side-by-Side Comparison"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(6)

    comp_rows = [
        ("Fixed: ", "Trials n  vs.  Target Successes r"),
        ("Random k: ", "Successes {0..n}  vs.  Failures {0..∞}"),
        ("Mean (μ): ", "np  vs.  r(1 − p)/p"),
        ("Variance (σ²): ", "np(1−p) < μ (Under)  vs.  r(1−p)/p² > μ (Over) [3]")
    ]
    for c_k, c_v in comp_rows:
        p_c = tf11_t.add_paragraph()
        r1 = p_c.add_run()
        r1.text = "• " + c_k
        r1.font.bold = True
        r1.font.size = Pt(11)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_c.add_run()
        r2.text = c_v
        r2.font.size = Pt(10.5)
        r2.font.color.rgb = TEXT_DARK
        p_c.space_after = Pt(5)

    add_card(s11, Inches(7.3), Inches(4.95), Inches(5.233), Inches(1.8), bg_color=HIGHLIGHT_BG, border_color=SUCCESS_COLOR)
    tb11_b = s11.shapes.add_textbox(Inches(7.45), Inches(5.08), Inches(4.95), Inches(1.55))
    tf11_b = tb11_b.text_frame
    tf11_b.word_wrap = True
    p = tf11_b.paragraphs[0]
    p.text = "ML Model Bridge"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = SUCCESS_COLOR
    p.space_after = Pt(4)
    p1 = tf11_b.add_paragraph()
    p1.text = "The Binomial underlies A/B testing and logistic regression [2, 4]; the Negative Binomial underlies count regression for overdispersed data [3]."
    p1.font.size = Pt(10.5)
    p1.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 12: Combined ML Applications
    # ═══════════════════════════════════════════════════════
    s12 = prs.slides.add_slide(blank_layout)
    add_header(s12, "Real-World ML Applications: Binomial vs. Negative Binomial")
    add_footer(s12, 12)

    # Left: Binomial Applications
    add_card(s12, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.1), border_color=PRIMARY)
    tb12_l = s12.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.7))
    tf12_l = tb12_l.text_frame
    tf12_l.word_wrap = True
    p = tf12_l.paragraphs[0]
    p.text = "Binomial (Bounded Counts)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = PRIMARY
    p.space_after = Pt(12)

    pos_apps = [
        ("A/B Testing (Hypothetical): ", "Layout A (n=1000, 10%) vs. B (n=1000, 13%): Pooled SE=0.0143, Z=2.1027, p=0.0177 (one-sided), p=0.0355 (two-sided). Reject H0 at alpha=0.05 (one-sided); check practical significance before rollout."),
        ("Click-Through Rate (CTR): ", "Model expected clicks k ~ Bin(n, pCTR) across n impressions to price real-time ad bids."),
        ("Logistic Regression [2, 4]: ", "Binary Cross-Entropy in Logistic Regression & Neural Nets optimizes Binomial log-likelihood.")
    ]
    for a_t, a_d in pos_apps:
        p_a = tf12_l.add_paragraph()
        r1 = p_a.add_run()
        r1.text = "• " + a_t
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_a.add_run()
        r2.text = a_d
        r2.font.size = Pt(11.5)
        r2.font.color.rgb = TEXT_DARK
        p_a.space_after = Pt(12)

    # Right: Negative Binomial Applications
    add_card(s12, Inches(6.8), Inches(1.6), Inches(5.733), Inches(5.1), border_color=ACCENT)
    tb12_r = s12.shapes.add_textbox(Inches(7.0), Inches(1.8), Inches(5.3), Inches(4.7))
    tf12_r = tb12_r.text_frame
    tf12_r.word_wrap = True
    p = tf12_r.paragraphs[0]
    p.text = "Negative Binomial (Overdispersed Counts) [3]"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(12)

    neg_apps = [
        ("Negative Binomial Regression (GLMs) [3]: ", "Overdispersion is common in real count data (e.g., ER visits, insurance claims, RNA-seq reads) where σ² ≫ μ."),
        ("Customer & Churn Analytics: ", "Models repeat purchases or support tickets before customer churn."),
        ("Bioinformatics (RNA-Seq): ", "Powers differential gene expression tools (DESeq2, edgeR) on overdispersed sequencing read counts.")
    ]
    for a_t, a_d in neg_apps:
        p_a = tf12_r.add_paragraph()
        r1 = p_a.add_run()
        r1.text = "• " + a_t
        r1.font.bold = True
        r1.font.size = Pt(12)
        r1.font.color.rgb = PRIMARY_DARK
        r2 = p_a.add_run()
        r2.text = a_d
        r2.font.size = Pt(11.5)
        r2.font.color.rgb = TEXT_DARK
        p_a.space_after = Pt(12)

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
    p_desc.text = "• Consistent with the Law of Large Numbers: With N=1,000 samples, Binomial errors are under 1%.\n• Closed-form MLE p̂ = 12.072 / 20 = 0.6036 [1] recovers true p (0.6000)."
    p_desc.font.size = Pt(11)
    p_desc.font.color.rgb = TEXT_DARK

    # ═══════════════════════════════════════════════════════
    # SLIDE 14: Practical Demo Part B (Negative Binomial Simulation)
    # ═══════════════════════════════════════════════════════
    s14 = prs.slides.add_slide(blank_layout)
    add_header(s14, "Practical Demo — Part B: Negative Binomial Simulation")
    add_footer(s14, 14)

    # Left: Plot
    add_card(s14, Inches(0.8), Inches(1.6), Inches(5.8), Inches(5.1))
    if os.path.exists("fig_negbinom_simulation.png"):
        s14.shapes.add_picture("fig_negbinom_simulation.png", Inches(0.95), Inches(1.8), width=Inches(5.5))
    cap_box = s14.shapes.add_textbox(Inches(1.0), Inches(6.1), Inches(5.4), Inches(0.5))
    tf_cap = cap_box.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "Figure 14: 1,000 Simulated Samples vs Theoretical NegBin PMF (r=5, p=0.4)"
    p_cap.font.size = Pt(10)
    p_cap.alignment = PP_ALIGN.CENTER
    p_cap.font.color.rgb = TEXT_MUTED

    # Right: Moment Comparison Table
    add_card(s14, Inches(6.9), Inches(1.6), Inches(5.633), Inches(5.1), bg_color=HIGHLIGHT_BG, border_color=ACCENT)
    tb14_r = s14.shapes.add_textbox(Inches(7.1), Inches(1.8), Inches(5.2), Inches(4.7))
    tf14_r = tb14_r.text_frame
    tf14_r.word_wrap = True

    p = tf14_r.paragraphs[0]
    p.text = "Empirical vs. Theoretical Moments (N=1,000)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = ACCENT
    p.space_after = Pt(10)

    nb_res = [
        ("Mean (μ): ", "Theoretical = 7.5000  |  Simulated = 7.4860 (Diff: 0.0140)"),
        ("Variance (σ²): ", "Theoretical = 18.7500  |  Simulated = 20.0398 (Diff: 1.2898)"),
        ("Std Dev (σ): ", "Theoretical = 4.3301  |  Simulated = 4.4766 (Diff: 0.1465)"),
        ("Dispersion (σ²/μ): ", "2.6770 (Theoretical: 2.5000 > 1.0 → Overdispersed!)"),
        ("MLE Parameter (p̂): ", "r / (r + x̄) = 0.4004  (True p = 0.4000)")
    ]
    for r_title, r_desc in nb_res:
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
    p_dec.text = "\nKey Takeaway:"
    p_dec.font.size = Pt(13)
    p_dec.font.bold = True
    p_dec.font.color.rgb = PRIMARY
    p_dec.space_after = Pt(4)

    p_decd = tf14_r.add_paragraph()
    p_decd.text = "Simulated variance (20.04) is about 2.7× the mean (7.49), which supports overdispersion; the MLE recovers p closely (0.4004 vs true 0.4000)."
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
        ("Complementary views: ", "Binomial models bounded successes (σ² < μ), while Negative Binomial models unbounded failures (σ² > μ) [1, 3]."),
        ("ML Foundations: ", "The Binomial underlies A/B testing and logistic regression [2, 4]; the Negative Binomial underlies count regression for overdispersed data [3]."),
        ("Simulation Summary: ", "Both simulations are consistent with theory. Binomial errors are under 1%. The Negative Binomial variance is noisier because of its heavy right tail.")
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
        ("Violation of Independence: ", "Viral loops, social contagion, and referral networks violate the independence assumption."),
        ("Probability Drift (Non-Constant p): ", "Conversion and failure rates fluctuate by time of day, season, and fatigue."),
        ("Zero-Inflation: ", "Datasets with excessive zeros require Zero-Inflated Negative Binomial (ZINB) models.")
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
        "[1] Casella, G., & Berger, R. L. Statistical Inference, 2nd ed., Duxbury Press, 2002.  |  "
        "[2] Bishop, C. M. Pattern Recognition and Machine Learning, Springer, 2006.\n"
        "[3] Hilbe, J. M. Negative Binomial Regression, 2nd ed., Cambridge University Press, 2011.  |  "
        "[4] Hastie, T., Tibshirani, R., & Friedman, J. The Elements of Statistical Learning, 2nd ed., Springer, 2009.\n"
        "AI tools were used to help draft text, code and figures: [EDIT: describe actual use]. The group checked all results."
    )
    p_ref = tf15_b.add_paragraph()
    p_ref.text = refs
    p_ref.font.size = Pt(9)
    p_ref.font.color.rgb = RGBColor(148, 163, 184)

    prs.save("slides.pptx")
    print("Successfully built new 15-slide Binomial deck in slides.pptx!")

if __name__ == "__main__":
    create_binomial_deck()
