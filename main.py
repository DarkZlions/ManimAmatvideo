from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

titel_font_size = 100
subtitle_font_size = 30
titels = []
titel = Text("Lambda Kalkül", font_size=titel_font_size)
author = Text("Andrija Divjak, Besar Miftari und Leon Aiello", font_size=20)
author.next_to(titel, DOWN)
lb_term = Text("Lambda Terme", font_size=subtitle_font_size).shift(2 * UP)
titels.append(lb_term)
b_rd = Text("Beta Reduktion", font_size=subtitle_font_size)
titels.append(b_rd)
var_cap = Text("Variable Capture", font_size=subtitle_font_size)
titels.append(var_cap)
syn_tree = Text("Syntax Trees", font_size=subtitle_font_size)
titels.append(syn_tree)
redu = Text("Reduktionsstrategien", font_size=subtitle_font_size)
titels.append(redu)
ari = Text("Arithmetik ", font_size=subtitle_font_size)
titels.append(ari)
logic = Text("Logik", font_size=subtitle_font_size)
titels.append(logic)
recu = Text("Rekursion (eager und lazy)", font_size=subtitle_font_size)
titels.append(recu)
rack = Text("Beispiele in Racket", font_size=subtitle_font_size)
titels.append(rack)

kanti = Text("Kantonsschule Baden", font_size=subtitle_font_size)


def getline():
    return Line(titel.get_left(), titel.get_right(), color=WHITE)


def wline(scene):
    return Line(start=LEFT * scene.camera.frame_width / 2, end=RIGHT * scene.camera.frame_width * 2, color=WHITE)




class introduction(Scene):
    def construct(self):

        for x in range(len(titels) - 1):
            titels[x + 1].next_to(titels[x], DOWN)

        line = getline()
        line1 = getline()

        line.next_to(titels[0], UP)
        line1.next_to(rack, DOWN)

        self.play(FadeIn(titel), FadeIn(author), run_time=2)
        self.wait(3)
        self.remove(author)
        self.play(titel.animate.scale(0.6))
        self.play(titel.animate.to_edge(UP))
        self.add(line)
        self.add(line1)
        for x in range(len(titels)):
            self.add(titels[x])
            self.play(FadeIn(titels[x]), run_time=0.4)
        self.wait(5)

class teil_eins(Scene):
    def construct(self):
        max = 4

        for x in range(max):
            titels[x + 1].next_to(titels[x], DOWN)

        part_1 = Text("Teil 1", font_size=subtitle_font_size)
        line = getline()
        line1 = getline()

        line.next_to(titels[0], UP)
        line1.next_to(titels[3], DOWN)

        kanti.next_to(author, DOWN)

        #######INTRO########
        self.play(FadeIn(titel), Write(author), Write(kanti), run_time=3)
        self.wait(4)
        self.remove(author, kanti)
        self.play(titel.animate.scale(0.5))
        self.play(titel.animate.to_edge(UP))
        part_1.next_to(titel, RIGHT)
        self.add(part_1)
        self.play(FadeIn(line), FadeIn(line1), run_time=0.5)
        for x in range(max):
            self.add(titels[x])
            self.play(FadeIn(titels[x]), run_time=0.4)
        self.wait(5)
        #######LAMBDATERM####
        self.remove(line, line1, titel, titels[1], titels[2], titels[3], part_1)
        self.play(titels[0].animate.to_corner(UP + LEFT))
        sub_line = wline(self)
        sub_line.next_to(titels[0], DOWN)
        self.add(sub_line)

        rect = Rectangle(width=5, height=4, fill_opacity=0.2, color=LIGHT_GRAY)

        desc_size = 20

        desc_content = "Beschreibung von Funktion \n \n Lambda-Abstraktion \n (Funktionsdefinition) \n \n Gekennzeichnet durch λ"
        desc = Text(desc_content, font_size=desc_size)
        desc.scale_to_fit_width(4.3)
        desc.move_to(rect.get_center())

        text_box = VGroup(rect, desc)
        # text_box.arrange(buff=0.5)
        text_box.move_to(LEFT * 4)
        self.play(FadeIn(text_box))
        self.wait(0.5)
        lambda_abstr = Text("λx.M", font_size=60)
        lambda_abstr.move_to(RIGHT * 3.5)
        self.play(Write(lambda_abstr))
        ar_1 = Arrow(start=lambda_abstr[1].get_bottom() + DOWN * 1.5 + LEFT,
                     end=lambda_abstr[1].get_center() + DOWN * 0.2, color=YELLOW)
        ar_2 = Arrow(start=lambda_abstr[3].get_bottom() + DOWN * 1.5 + RIGHT,
                     end=lambda_abstr[3].get_center() + DOWN * 0.2, color=YELLOW)

        desc_ar1 = Text("Variable", font_size=30)
        desc_ar2 = Text("λ-Term", font_size=30)

        desc_ar1.move_to(ar_1.get_start() + DOWN * 0.5)
        desc_ar2.move_to(ar_2.get_start() + DOWN * 0.5)
        highlight_col = RED_B
        self.play(lambda_abstr[1].animate.set_color(highlight_col), FadeIn(ar_1), Write(desc_ar1), run_time=0.5)
        self.play(lambda_abstr[3].animate.set_color(highlight_col), FadeIn(ar_2), Write(desc_ar2), run_time=0.5)
        self.wait()
        self.play(lambda_abstr[1].animate.set_color(WHITE), lambda_abstr[3].animate.set_color(WHITE))
        self.play(FadeOut(text_box))
        func_ex = Tex(r"$f(x) = x + 1$", font_size=60)
        lambda_ex = Text("λx.(x + 1)", font_size=60)
        equal_s = Text("=", font_size=65)
        lambda_ex.move_to(RIGHT * 3.5)
        func_ex.move_to(LEFT * 4)
        self.play(Write(func_ex), FadeOut(desc_ar1), FadeOut(desc_ar2), FadeOut(ar_1), FadeOut(ar_2))
        self.play(ReplacementTransform(lambda_abstr, lambda_ex), FadeIn(equal_s))

        curved_arrow = CurvedArrow(DOWN * 0.5 + lambda_ex[1].get_right(), DOWN * 0.5 + lambda_ex[0].get_left(),
                                   tip_style={'fill_opacity': 1, 'stroke_width': 0.1}, radius=-10,
                                   stroke_color=YELLOW).scale(0.65)
        desc_1 = Text("Gebunden", font_size=desc_size)
        desc_1.next_to(curved_arrow, DOWN)
        self.play(lambda_ex[1].animate.scale(1.2), Create(curved_arrow), Write(desc_1))
        self.play(lambda_ex[0].animate.scale(1.2), lambda_ex[1].animate.scale(1 / 1.2))
        self.play(lambda_ex[0].animate.scale(1 / 1.2))
        self.wait(1)
        self.remove(curved_arrow, desc_1)
        self.play(lambda_ex[-5:].animate.scale(1.2))
        self.play(lambda_ex[-5:].animate.scale(1 / 1.2))
        self.wait(2)
        subtitle = Text("Gebundene und Ungebundene Variablen", font_size=subtitle_font_size)
        subtitle.shift(UP * 2.5)
        self.add(lambda_ex)
        self.remove(curved_arrow, desc_1, lambda_ex, lambda_abstr, func_ex, equal_s)
        self.play(Write(subtitle))

        desc_bound = Text("Gebunden", font_size=30)
        desc_bound_1 = Text("Innerhalb der Abstraktion", font_size=30)
        term_bound = Text("λx.(x + 1)", font_size=30)
        desc_bound.shift(UP * 1.5)
        term_bound.next_to(desc_bound, DOWN)
        desc_bound_1.next_to(term_bound, DOWN)

        desc_ubound = Text("Ungebunden", font_size=30)
        desc_ubound_1 = Text("Ausserhalb der Abstraktion", font_size=30)
        term_ubound = Text("λx.(y + 1)", font_size=30)
        desc_ubound.next_to(desc_bound, DOWN * 3).shift(DOWN)
        term_ubound.next_to(desc_ubound, DOWN)
        desc_ubound_1.next_to(term_ubound, DOWN)

        self.play(Write(desc_bound), Write(desc_ubound))
        self.play(Write(term_bound), Write(term_ubound))
        self.play(term_bound[4].animate.set_color(highlight_col), Write(desc_bound_1))
        self.play(term_bound[1].animate.set_color(highlight_col))
        self.play(term_ubound[4].animate.set_color(BLUE), Write(desc_ubound_1))
        self.play(term_ubound[1].animate.set_color(highlight_col))
        self.wait()
        self.remove(desc_bound, desc_bound_1, term_bound, desc_ubound, desc_ubound_1, term_ubound, subtitle)
        self.play(FadeOut(titels[0]))
        titels[1].to_corner(UP + LEFT)
        self.play(Write(titels[1]))
        br_func = Text("((λx.M)N)", font_size=40)
        curved_arrow_1 = CurvedArrow(DOWN * 0.5 + br_func[7].get_right(), DOWN * 0.5 + br_func[5].get_left(),
                                     tip_style={'fill_opacity': 1, 'stroke_width': 0.1}, radius=-10,
                                     stroke_color=YELLOW).scale(0.65)

        self.play(Write(br_func))
        self.play(br_func[7].animate.scale(1.2), Create(curved_arrow_1))
        self.play(br_func[5].animate.scale(1.2), br_func[7].animate.scale(1 / 1.2))
        self.play(br_func[5].animate.scale(1 / 1.2))

        self.wait(1)
        self.remove(curved_arrow_1)
        example_text = Text("Beispiel: ", font_size=40)
        example_text.shift(UP * 2)
        br_ex = Text("((λx.(x + 1) 2)", font_size=40)
        curved_arrow_2 = CurvedArrow(DOWN * 0.5 + br_ex[10].get_right(), DOWN * 0.5 + br_ex[6].get_left(),
                                     tip_style={'fill_opacity': 1, 'stroke_width': 0.1}, radius=-10,
                                     stroke_color=YELLOW).scale(0.65)
        self.play(ReplacementTransform(br_func, br_ex), FadeIn(example_text))
        self.wait(1)
        self.play(br_ex[10].animate.set_color(highlight_col), Create(curved_arrow_2))
        self.play(br_ex[6].animate.scale(1.2), run_time=0.5)
        self.play(br_ex[6].animate.scale(1 / 1.2))
        br_ex_1 = Text("((λx.(2 + 1) 2)", font_size=40)
        br_ex_1[6].set_color(highlight_col)
        br_ex_1[10].set_color(highlight_col)
        self.play(ReplacementTransform(br_ex, br_ex_1), FadeOut(curved_arrow_2))
        br_ex_2 = Text("(2 + 1) = 3", font_size=40)
        br_ex_2.next_to(br_ex_1, DOWN)
        self.play(Write(br_ex_2))
        self.wait(3)
        self.remove(br_ex_2, br_ex_1, example_text)
        self.play(FadeOut(titels[1]))
        titels[2].to_corner(UP + LEFT)
        self.play(Write(titels[2]))
        desc_vr = MarkupText(
            f'Wenn eine <span fgcolor="{RED_B}"> freie Variable</span>, die im ursprünglichen Ausdruck nicht <span fgcolor="{RED_B}">gebunden</span> war,\n von einer Lambda-Abstraktion <span fgcolor="{RED_B}">gebunden</span> wird, dann spricht man von <span fgcolor="{RED_B}">Variable Capture</span>.',
            font_size=20)

        desc_vr_1 = MarkupText(
            f'Kann vermieden werden, wenn alle Variablen <span fgcolor="{RED_B}">einzigartige</span> Namen haben.',
            font_size=20)
        desc_vr_1.next_to(desc_vr, DOWN * 1.2)
        self.play(Write(desc_vr), Write(desc_vr_1))
        self.wait(5)
        self.play(FadeOut(desc_vr), FadeOut(desc_vr_1))
        self.play(Write(example_text))
        vr_ex = Text("(λx.(λy.x + y)) y", font_size=40)
        vr_ex_1 = Text("(λy.y + y)", font_size=40)
        vr_ex.to_edge(LEFT).shift(UP * 0.5)
        vr_ex_1.next_to(vr_ex, DOWN * 2)
        self.play(Write(vr_ex))
        self.play(vr_ex[2].animate.set_color(highlight_col))
        self.play(vr_ex[6].animate.set_color(highlight_col))
        self.play(vr_ex[13].animate.set_color(BLUE))
        self.play(Write(vr_ex_1))
        ar_3 = Arrow(start=vr_ex[13].get_bottom(), end=vr_ex_1[4].get_top(), color=YELLOW)
        self.play(Create(ar_3), vr_ex_1[4].animate.set_color(BLUE), vr_ex_1[2].animate.set_color(highlight_col))
        self.play(vr_ex_1[4].animate.set_color(highlight_col))
        vr_ex_2 = Text("(λx.(λz.x + z)) y", font_size=40)
        vr_ex_3 = Text("(λx.(λy.x + y)) y", font_size=40)
        vr_ex_3.to_edge(RIGHT)
        vr_ex_2.to_edge(RIGHT)
        self.play(Write(vr_ex_3))
        self.wait()
        self.play(vr_ex_3[6].animate.set_color(highlight_col), vr_ex_3[10].animate.set_color(highlight_col),
                  vr_ex_3[13].animate.set_color(BLUE))
        self.play(ReplacementTransform(vr_ex_3, vr_ex_2))
        self.play(vr_ex_2[6].animate.set_color(highlight_col), vr_ex_2[10].animate.set_color(highlight_col),
                  vr_ex_2[13].animate.set_color(BLUE))
        self.wait(3)
        self.remove(vr_ex_2, ar_3, vr_ex, vr_ex_1, example_text)
        self.play(FadeOut(titels[2]))
        titels[3].to_corner(UP + LEFT)
        self.play(Write(titels[3]))
        syn_desc = MarkupText(
            f'<span fgcolor="{RED_B}">3</span> Elemente: \n\n Variablen \n λ-Abstraktion \n Applikation @',
            font_size=18)

        rect_1 = Rectangle(width=4.6, height=5, fill_opacity=0.2, color=LIGHT_GRAY)
        syn_desc.scale_to_fit_width(3.6)
        syn_desc.move_to(rect_1.get_center())

        text_box_1 = VGroup(rect_1, syn_desc)
        # text_box.arrange(buff=0.5)

        self.play(FadeIn(text_box_1))
        self.wait(2)
        example_text.shift(RIGHT * 2).scale(0.75)
        self.play(text_box_1.animate.to_edge(LEFT), Write(example_text))
        syn_ex = Text("(λv.x v)(λwu.w u w)", font_size=30)
        syn_ex.next_to(example_text, DOWN)
        self.play(Write(syn_ex))
        self.wait()

        ani_text = [
            syn_ex, syn_ex[1], syn_ex[2], syn_ex[4:6], syn_ex[4], syn_ex[5], syn_ex[7:], syn_ex[9], syn_ex[8], syn_ex[10], syn_ex[12:], syn_ex[12], syn_ex[13:], syn_ex[13], syn_ex[14]
        ]

        ex = extra_animation(self, ani_text)

        level = []
        level.append(syntax_node(None, '@'))
        level.append([syntax_node(level[0], 'λ'), syntax_node(level[0], 'λ')])
        level.append([syntax_node(level[1][0], 'v'), syntax_node(level[1][0], '@'), syntax_node(level[1][1], 'w'), syntax_node(level[1][1], 'λ')])
        level.append([syntax_node(level[2][1], 'x'), syntax_node(level[2][1], 'v'), syntax_node(level[2][3], 'u'), syntax_node(level[2][3], '@')])
        level.append([syntax_node(level[3][3], 'w'), syntax_node(level[3][3], '@')])
        level.append([syntax_node(level[4][1], 'u'), syntax_node(level[4][1], 'w')])

        level[0].get_value().next_to(syn_ex, DOWN)
        level[0].extra_animate(self, ex)

        self.wait(5)

        outro(self)

class teil_zwei(Scene):
    def construct(self):
        titels = [
            Text("Reduktionsstrategien", font_size=subtitle_font_size),
        Text("Arithmetik", font_size=subtitle_font_size),
        Text("Logik", font_size=subtitle_font_size)
        ]
        max = 2

        part_1 = Text("Teil 2", font_size=subtitle_font_size)
        line = getline()
        line1 = getline()

        kanti.next_to(author, DOWN)

        #######INTRO########
        self.play(FadeIn(titel), Write(author), Write(kanti), run_time=3)
        self.wait(4)
        self.remove(author, kanti)
        self.play(titel.animate.scale(0.5))
        self.play(titel.animate.to_edge(UP))
        part_1.next_to(titel, RIGHT)
        titels[0].next_to(titel, DOWN*4)
        for x in range(max):
            titels[x+1].next_to(titels[x], DOWN*1.5)
        line.next_to(titels[0], UP)
        line1.next_to(titels[2], DOWN)
        self.add(part_1)
        self.play(FadeIn(line), FadeIn(line1), run_time=0.5)
        for x in range(max+1):
            self.add(titels[x])
            self.play(FadeIn(titels[x]), run_time=0.4)
        self.wait(5)

        self.remove(line, line1, titel, titels[1], titels[2], part_1)
        self.play(titels[0].animate.to_corner(UP + LEFT))
        sub_line = wline(self)
        sub_line.next_to(titels[0], DOWN)
        self.add(sub_line)
        desc_lazy = Text('Lazy', font_size=35)
        desc_eager = Text('Eager / Strict', font_size=35)
        desc_lazy.to_edge(LEFT*0.5)
        desc_eager.to_edge(RIGHT*0.5)
        self.play(Write(desc_lazy), Write(desc_eager))
        self.wait()
        self.play(desc_eager.animate.shift(UP*2), desc_lazy.animate.shift(UP*2))
        self.wait()
        bsp = Text('Beispiel:', font_size=35)
        bsp1 = Text('(λx.(x + 1)) ((λy.y + 2) 3)', font_size=25)
        bsp.shift(UP*2)
        bsp1.next_to(bsp, DOWN*0.5)
        self.play(Write(bsp), Write(bsp1))
        lazy1 = Text('(λx.(x + 1)) ((λy.y + 2) 3)', font_size=25)
        lazy1.to_edge(LEFT).shift(UP*1.4)
        lazy2 = Text('(λx.(((λy.y + 2) 3) + 1))', font_size=25)
        lazy2.next_to(lazy1, DOWN)
        lazy3 = Text('(((λy.y + 2) 3) + 1)', font_size=25)
        lazy3.next_to(lazy1, DOWN)
        lazy4 = Text('(((λy.3 + 2) 3) + 1)', font_size=25)
        lazy4.next_to(lazy3, DOWN)
        lazy5 = Text('((3 + 2) + 1)', font_size=25)
        lazy5.next_to(lazy3, DOWN)
        lazy6 = Text('6', font_size=25)
        lazy6.next_to(lazy5, DOWN)

        self.play(FadeOut(bsp1))
        self.play(Write(lazy1))
        self.play(lazy1[-11:].animate.set_color(BLUE))
        self.wait()
        self.play(Write(lazy2))
        self.play(lazy2[4:16].animate.set_color(BLUE))
        self.play(ReplacementTransform(lazy2, lazy3))
        self.play(lazy3[10].animate.set_color(BLUE))
        self.wait()
        self.play(Write(lazy4))
        self.play(lazy4[6].animate.set_color(BLUE))
        self.play(ReplacementTransform(lazy4, lazy5))
        self.wait()
        self.play(Write(lazy6))
        self.wait()

        eager1 = Text('(λx.(x + 1)) ((λy.y + 2) 3)', font_size=25)
        eager2 = Text('(λx.(x + 1)) ((λy.3 + 2) 3)', font_size=25)
        eager3 = Text('(λx.(x + 1)) (3 + 2)', font_size=25)
        eager4 = Text('(λx.((3 + 2) + 1))', font_size=25)
        eager5 = Text('(3 + 2) + 1', font_size=25)
        eager6 = Text('6', font_size=25)

        eager1.to_edge(RIGHT).shift(UP*1.4)
        eager2.next_to(eager1, DOWN)
        eager3.next_to(eager1,  DOWN)
        eager4.next_to(eager3, DOWN)
        eager5.next_to(eager3, DOWN)
        eager6.next_to(eager5, DOWN)

        self.play(Write(eager1))
        self.play(eager1[-2:-1].animate.set_color(BLUE))
        self.wait()
        self.play(Write(eager2))
        self.play(eager2[-6:-5].animate.set_color(BLUE))
        self.play(ReplacementTransform(eager2, eager3))
        self.play(eager3[-5:].animate.set_color(BLUE))
        self.wait()
        self.play(Write(eager4))
        self.play(eager4[5:10].animate.set_color(BLUE))
        self.play(ReplacementTransform(eager4, eager5))
        self.wait()
        self.play(Write(eager6))
        self.wait(2)

        self.add(eager1, eager2, eager3, eager4, eager5, eager6, lazy1, lazy2, lazy3, lazy4, lazy5, lazy6, bsp)
        self.remove(eager1, eager2, eager3, eager4, eager5, eager6, lazy1, lazy2, lazy3, lazy4, lazy5, lazy6, bsp, desc_eager, desc_lazy)

        tree = [
            Text('T', font_size=35),
            Text('E', font_size=35),
            Text('F', font_size=35),
            Text('S', font_size=35),
        ]

        tree[0].shift(UP*1.5)
        tree[1].shift(LEFT*1.5)
        tree[2].shift(RIGHT*1.5)
        tree[3].shift(DOWN*1.5)

        l1 = Line(start=tree[0].get_bottom() + DOWN*0.2, end=tree[1].get_top()+UP*0.2, color=WHITE)
        l2 = Line(start=tree[0].get_bottom()+DOWN*0.2, end=tree[2].get_top()+UP*0.2, color=WHITE)
        l3 = Line(start=tree[1].get_bottom()+DOWN*0.2, end=tree[3].get_top()+UP*0.2, color=WHITE)
        l4 = Line(start=tree[2].get_bottom()+DOWN*0.2, end=tree[3].get_top()+UP*0.2, color=WHITE)

        self.play(Write(tree[0]))
        self.play(Create(l1), Create(l2))
        self.play(Write(tree[1]), Write(tree[2]))
        self.play(Create(l3), Create(l4))
        self.play(Write(tree[3]))

        a = Text('Theorem (Church-Rosser, 1936, 1965). If a term T can be reduced using different strategies \n to terms E and F, then there are strategies and a term S such that both E and F can be \n reduced tothe same term S.', font_size=20)

        a.next_to(tree[3], DOWN)
        self.play(Write(a))
        self.wait(5)

        self.remove(tree[0], tree[1], tree[2], tree[3], l1, l2, l3, l4, a)

        self.play(FadeOut(titels[0]))
        titels[1].to_corner(UP + LEFT)
        self.play(Write(titels[1]))
        self.wait()


        ar0 = Text('0 := λf.(λx.x)', font_size=30)
        ar1 = Text('1 := λf.(λx.f x) ', font_size=30)
        ar2 = Text('2 := λf.(λx.f f x)', font_size=30)
        ar3 = Text('3 := λf.(λx.f f f x)', font_size=30)
        succ = Text('Successor Funktion: S = λn.λf.λx.f (n f x)', font_size=30)
        self.play(Write(succ))
        self.wait()
        self.play(succ.animate.shift(UP*1.5))
        ar0.next_to(succ, DOWN*1.2)
        ar1.next_to(ar0, DOWN)
        ar2.next_to(ar1, DOWN)
        ar3.next_to(ar2, DOWN)
        self.play(Write(ar0), Write(ar1), Write(ar2), Write(ar3))

        self.wait()
        self.remove(ar0, ar1, ar2, ar3, succ)
        bsp = Text('Beispiel:', font_size=30)
        bsp1 = Text('S 2', font_size=30)
        bsp2 = Text('(λn.λf.λx.f (n f x)) 2', font_size=25)
        bsp3 = Text('λf.λx.f(2 f x)', font_size=25)
        bsp4 = Text('f.λx.f(λf.(λx.f f x) f x)', font_size=25)
        bsp5 = Text('λf.λx.f(f f x) = 3', font_size=25)
        bsp.shift(UP*1.5)
        self.play(Write(bsp))
        self.wait()
        bsp1.next_to(bsp, DOWN)
        self.play(Write(bsp1))
        self.wait()
        bsp2.next_to(bsp1, DOWN)
        self.play(Write(bsp2))
        self.play(bsp2[-1:].animate.set_color(BLUE))
        self.wait()
        bsp3.next_to(bsp2, DOWN)
        self.play(Write(bsp3))
        self.play(bsp3[8].animate.set_color(BLUE))
        self.wait()
        bsp4.next_to(bsp3, DOWN)
        self.play(Write(bsp4))
        self.play(bsp4[7:18].animate.set_color(BLUE))
        self.wait()
        bsp5.next_to(bsp4, DOWN)
        self.play(Write(bsp5))
        self.wait(2)
        self.add(bsp, bsp1, bsp2, bsp3, bsp4, bsp5)
        self.remove(bsp, bsp1, bsp2, bsp3, bsp4, bsp5)
        addi = Text('+ := λm.λn.m S n', font_size=25)
        self.play(Write(addi))
        self.wait()
        addi1 = Text('(+ 1 1)', font_size=25)
        addi2 = Text('(λm.λn.m S n) 1 1', font_size=25)
        addi3 = Text('(λm.λn.1 S 1)', font_size=25)
        addi4 = Text('1 S 1', font_size=25)
        addi5 = Text('λf.(λx.f x) S 1', font_size=25)
        addi6 = Text('λf.(λx.S 1)', font_size=25)
        addi7 = Text('S 1 = 2', font_size=25)
        addi1.next_to(bsp, DOWN)
        addi2.next_to(addi1, DOWN)
        addi3.next_to(addi2, DOWN)
        addi4.next_to(addi3, DOWN)
        addi5.next_to(addi4, DOWN)
        addi6.next_to(addi5, DOWN)
        addi7.next_to(addi6, DOWN)
        self.play(Write(bsp), FadeOut(addi))
        self.play(Write(addi1))
        self.play(addi1[1].animate.set_color(BLUE))
        self.wait()
        self.play(Write(addi2))
        self.play(addi2[0:11].animate.set_color(BLUE))
        self.wait()
        self.play(Write(addi3))
        self.wait()
        self.play(Write(addi4))
        self.wait()
        self.play(Write(addi5))
        self.wait()
        self.play(Write(addi6))
        self.wait()
        self.play(Write(addi7))
        self.wait()

        self.add(addi, addi1, addi2, addi3, addi4, addi5, addi6, addi7, bsp)
        self.remove(addi, addi1, addi2, addi3, addi4, addi5, addi6, addi7, bsp)

        self.play(FadeOut(titels[1]))
        titels[2].to_corner(UP + LEFT)
        self.play(Write(titels[2]))
        self.wait()

        lo = Text('T := λxλy.x ', font_size=25)
        lo1 = Text('F := λxλy.y', font_size=25)
        lo2 = Text('Negation: ¬ := λx.[x (λuv.v) (λab.a)] = λx.[x F T]', font_size=25)
        lo3 = Text('Konjunktion (und): ∧ := λxy.xy(λuv.v) = λxy.xyF', font_size=25)
        lo4 = Text('Disjunktion (oder): ∨ := λxy.x(λuv.u)y = λxy.xTy', font_size=25)
        lo.shift(UP*1.5)
        lo1.next_to(lo, DOWN)
        lo2.next_to(lo1, DOWN)
        lo3.next_to(lo2, DOWN)
        lo4.next_to(lo3, DOWN)
        self.play(Write(lo), Write(lo1), Write(lo2), Write(lo3), Write(lo4))
        self.wait(2)
        self.remove(lo, lo1, lo2, lo3, lo4)
        lg = Text('Beispiel:', font_size=25)
        lg1 = Text('¬T', font_size=25)
        lg2 = Text('(λx.[x F T]) T', font_size=25)
        lg3 = Text('T F T', font_size=25)
        lg4 = Text('((λx.λy.x) F T', font_size=25)
        lg5 = Text('(λy.F) T', font_size=25)
        lg6 = Text('F', font_size=25)

        lg.shift(UP*1.5)
        lg1.next_to(lg, DOWN)
        lg2.next_to(lg1, DOWN)
        lg3.next_to(lg2, DOWN)
        lg4.next_to(lg3, DOWN)
        lg5.next_to(lg4, DOWN)
        lg6.next_to(lg5, DOWN)

        self.play(Write(lg))
        self.wait()
        self.play(Write(lg1))
        self.wait()
        self.play(Write(lg2))
        self.wait()
        self.play(Write(lg3))
        self.wait()
        self.play(Write(lg4))
        self.wait()
        self.play(Write(lg5))
        self.wait()
        self.play(Write(lg6))
        self.wait()
        outro(self)

class teil_drei(Scene):
    def construct(self):
        titels = [
            Text("Rekursion", font_size=subtitle_font_size),
        Text("Racket", font_size=subtitle_font_size),
        ]
        max = 1

        part_1 = Text("Teil 3", font_size=subtitle_font_size)
        line = getline()
        line1 = getline()

        kanti.next_to(author, DOWN)

        #######INTRO########
        self.play(FadeIn(titel), Write(author), Write(kanti), run_time=3)
        self.wait(4)
        self.remove(author, kanti)
        self.play(titel.animate.scale(0.5))
        self.play(titel.animate.to_edge(UP))
        part_1.next_to(titel, RIGHT)
        titels[0].next_to(titel, DOWN*4)
        for x in range(max):
            titels[x+1].next_to(titels[x], DOWN*1.5)
        line.next_to(titels[0], UP)
        line1.next_to(titels[1], DOWN)
        self.add(part_1)
        self.play(FadeIn(line), FadeIn(line1), run_time=0.5)
        for x in range(max+1):
            self.add(titels[x])
            self.play(FadeIn(titels[x]), run_time=0.4)
        self.wait(5)

        self.remove(line, line1, titel, titels[1], part_1)
        self.play(titels[0].animate.to_corner(UP + LEFT))
        sub_line = wline(self)
        sub_line.next_to(titels[0], DOWN)
        self.add(sub_line)
        self.wait(1)
        ykomb = Text('Y-Kombinator:', font_size=30)
        ykomb1 = Text('Y := λf.((λx.f(xx))(λy.f(yy)))', font_size=30)
        ykomb2 = Text('Ermöglicht im λ-Kalkül, dass Funktionen sich selber aufrufen können.', font_size=25)
        ykomb.shift(UP*1.5)
        ykomb1.next_to(ykomb, DOWN)

        self.play(FadeIn(ykomb))
        self.wait()
        self.play(Write(ykomb1))
        self.wait()
        self.play(Write(ykomb2))
        self.wait()
        self.play(FadeOut(ykomb), FadeOut(ykomb1), FadeOut(ykomb2))

        fg = Text('Funktion g', font_size=30)
        lazy = Text('Lazy', font_size=28)
        lazy1 = Text('Yg = (λf.((λx.f(xx))(λy.f(yy))))g', font_size=24)
        lazy2 = Text('((λx.g(xx))(λy.g(yy))))', font_size=24)
        lazy3 = Text('g((λy.g(yy))(λy.g(yy))))', font_size=24)
        lazy4 = Text('g(g((λy.g(yy))(λy.g(yy)))))', font_size=24)
        lazy5 = Text('g(g(g...usw.', font_size=24)

        fg.shift(UP*1.6)
        lazy.shift(UP*1.5+LEFT*4)
        lazy1.next_to(lazy, DOWN)
        lazy2.next_to(lazy1, DOWN)
        lazy3.next_to(lazy2, DOWN)
        lazy4.next_to(lazy3, DOWN)
        lazy5.next_to(lazy4, DOWN)

        eager = Text('Eager', font_size=28)
        eager1 = Text('Yg = (λf.((λx.f(xx))(λy.f(yy))))g', font_size=24)
        eager2 = Text('(λf.f((λy.f(yy))(λy.f(yy))))g', font_size=24)
        eager3 = Text('(λf.ff((λy.f(yy))(λy.f(yy))))g', font_size=24)
        eager4 = Text('(λf.fff((λy.f(yy))(λy.f(yy))))g', font_size=24)
        eager5 = Text('(λf.fff...usw.', font_size=24)

        eager.shift(UP*1.5+RIGHT*4)
        eager1.next_to(eager, DOWN)
        eager2.next_to(eager1, DOWN)
        eager3.next_to(eager2, DOWN)
        eager4.next_to(eager3, DOWN)
        eager5.next_to(eager4, DOWN)

        ca = CurvedArrow(eager1[24].get_bottom(), eager1[13].get_bottom(),
                    tip_style={'fill_opacity': 1, 'stroke_width': 0.1}, radius=-5,
                    stroke_color=BLUE).scale(0.65)
        ca1 = CurvedArrow(eager1[24].get_bottom(), eager1[11].get_bottom(),
                    tip_style={'fill_opacity': 1, 'stroke_width': 0.1}, radius=-2,
                    stroke_color=BLUE).scale(0.65)
        ca2 = CurvedArrow(RIGHT*0.7+lazy1[-1:].get_bottom(), lazy1[7].get_bottom(),
                    tip_style={'fill_opacity': 1, 'stroke_width': 0.1}, radius=-7,
                    stroke_color=BLUE).scale(0.65)
        ca3 = CurvedArrow(RIGHT*0.3+lazy1[-1:].get_bottom(), lazy1[19].get_bottom(),
                          tip_style={'fill_opacity': 1, 'stroke_width': 0.1}, radius=-3.5,
                          stroke_color=BLUE).scale(0.65)


        self.play(FadeIn(lazy), FadeIn(eager), FadeIn(fg))
        self.wait()
        self.play(Write(eager1))
        self.play(eager1[18:28].animate.set_color(BLUE))
        self.play(Create(ca))
        self.play(Create(ca1))
        self.play(Write(eager2))
        self.play(Write(eager3))
        self.play(Write(eager4))
        self.play(Write(eager5))
        self.wait(0.2)
        self.play(eager2[4].animate.set_color(BLUE), eager3[4:5].animate.set_color(BLUE),
                  eager4[4:6].animate.set_color(BLUE), eager5[4:6].animate.set_color(BLUE))
        self.wait()
        self.play(Write(lazy1))
        self.play(Create(ca2))
        self.play(Create(ca3))
        self.play(Write(lazy2))
        self.play(Write(lazy3))
        self.play(Write(lazy4))
        self.play(Write(lazy5))
        self.wait(0.2)
        self.play(lazy3[0].animate.set_color(BLUE), lazy4[0].animate.set_color(BLUE), lazy4[2].animate.set_color(BLUE),
                  lazy5[0].animate.set_color(BLUE), lazy5[2].animate.set_color(BLUE), lazy5[4].animate.set_color(BLUE))
        self.wait()
        self.play(FadeOut(eager, eager1, eager2, eager3, eager4, eager5, ca, ca1, ca2, ca3, fg, lazy, lazy1, lazy4, lazy5))

        yg = Text('Yg', font_size=24)
        yg1 = Text('g(Yg)', font_size=24)
        yg2 = Text(' = ', font_size=24)
        yg3 = Text(' = ', font_size=24)
        yg4 = Text(' = ', font_size=24)
        yg2.next_to(lazy2, RIGHT)
        yg3.next_to(lazy3, RIGHT)
        yg.next_to(yg2, RIGHT)
        yg1.next_to(yg3, RIGHT)

        self.play(FadeIn(yg, yg1, yg2, yg3))
        self.play(FadeOut(lazy2, lazy3, yg2, yg3), FadeIn(yg4), yg.animate.next_to(yg4, LEFT), yg1.animate.next_to(yg4, RIGHT))
        self.wait()
        su = Text('0 + 1 + 2 + 3 + 4 + ... + n', font_size=30)
        fr = Text('R := λr.(λn.0?n 0 (+ n (r(pred n))))', font_size=25)
        ifn = Text('if n is 0', font_size=17)
        el = Text('else', font_size=17)
        pred = Text('pred 2 = 1', font_size=17)
        ifn.next_to(fr[11], DOWN*0.2)
        el.next_to(fr[15], DOWN*0.2)
        pred.next_to(fr[23], DOWN*0.2)
        su.shift(UP*1.5)
        fr.shift(UP*0.5)
        self.play(FadeOut(yg4, yg, yg1), FadeIn(su))
        self.wait()
        self.play(Write(fr))
        self.play(fr[3:5].animate.set_color(BLUE), fr[7:9].animate.set_color(BLUE), run_time=0.9)
        self.play(fr[3:5].animate.set_color(WHITE), fr[7:9].animate.set_color(WHITE), run_time=0.4)
        self.wait(0.5)
        self.play(fr[11].animate.set_color(BLUE), fr[12].animate.set_color(RED_A), fr[10].animate.set_color(RED_A), run_time=0.75)
        self.play(FadeIn(ifn))
        self.play(fr[11].animate.set_color(WHITE), fr[12].animate.set_color(WHITE), fr[10].animate.set_color(WHITE), run_time=0.4)
        self.wait(0.5)
        self.play(fr[13].animate.set_color(BLUE), fr[14:].animate.set_color(BLUE))
        self.play(FadeIn(el))
        self.play(FadeIn(pred))

        self.wait()
        bsp = Text('Beispiel:', font_size=30)
        su3 = Text('sum 3', font_size=30)
        yr = Text('Y R 3', font_size=30)
        yr3 = Text('R (Y R) 3', font_size=30)
        bsp.shift(UP*1.5)
        su3.shift(UP*0.5)

        self.play(FadeOut(su, fr, el, pred, ifn), FadeIn(bsp), Write(su3))
        self.wait(0.5)
        self.play(Write(yr))
        self.play(ReplacementTransform(yr, yr3))
        self.wait()
        self.play(FadeOut(bsp, su3, yr), yr3.animate.shift(UP*1.4+LEFT*4))
        self.wait()
        syr = Text(' = (λr.(λn.0?n 0 (+ n(r(pred n))))) (YR) 3', font_size=30)
        syr.next_to(yr3, RIGHT)
        self.play(Write(syr))
        s1 = CurvedArrow(syr[-1:].get_bottom(), syr[7].get_bottom(),
                          tip_style={'fill_opacity': 1, 'stroke_width': 0}, radius=-15,
                          stroke_color=BLUE)
        s2 = CurvedArrow(syr[-6].get_bottom(), syr[2].get_bottom(),
                          tip_style={'fill_opacity': 1, 'stroke_width': 0}, radius=-13,
                          stroke_color=BLUE)
        self.play(Create(s1), Create(s2))
        self.wait()
        syr1 = Text('(0?3 0 (+ 3((YR)(pred 3))))', font_size=30)

        syr2 = Text('(3 S((YR)(2)))', font_size=30)
        syr3 = Text('(YR)(2)', font_size=30)
        syr1.next_to(syr, DOWN*1.2)
        syr2.next_to(syr1, DOWN*1.2)

        self.play(Write(syr1), FadeOut(s1, s2))
        self.wait()
        self.play(Write(syr2))
        self.wait()
        self.play(FadeOut(syr, syr1, yr3))
        self.play(syr2.animate.center().shift(UP*1.8))
        syr3.center().shift(UP*1.8)
        self.wait()
        self.play(ReplacementTransform(syr2, syr3))
        syr4 = Text('((λx.R(xx))(λy.R(yy)))(2)', font_size=30)

        syr4.next_to(syr3, DOWN*1.2)
        self.play(Write(syr4))
        syr5 = Text('(R((λy.R(yy))(λy.R(yy)))(2)', font_size=30)
        syr6 = Text('0?2 0(+2(((λy.R(yy))(λy.R(yy)))(pred 2)))', font_size=30)
        syr7 = Text('(2 S(((λy.R(yy))(λy.R(yy)))(1))', font_size=30)
        syr8 = Text('(3 S(2 S(...)',font_size=30)
        syr9 = Text('(((λy.R(yy))(λy.R(yy)))(1))', font_size=30)
        syr10 = Text('(R((λy.R(yy))(λy.R(yy)))(1)', font_size=30)
        syr11 = Text('(1 S(((λy.R(yy))(λy.R(yy)))(0))', font_size=30)
        syr12 = Text('...')
        syr13 = Text('0?0 0', font_size=30)
        syr14 = Text('(1 S(0))', font_size=30)
        syr15 = Text('(3 S(2 S(1 S(0)))) = 6', font_size=30)

        syr5.next_to(syr4, DOWN*1.2)
        syr6.next_to(syr5, DOWN*1.2)
        syr7.next_to(syr6, DOWN*1.2)

        self.play(Write(syr5))
        self.wait(0.25)
        self.play(Write(syr6))
        self.wait(0.5)
        self.play(Write(syr7))
        self.wait(0.25)
        self.play(FadeOut(syr5, syr6, syr4, syr3, syr2), syr7.animate.center().shift(UP*1.8))
        syr8.center().shift(UP*1.8)
        self.play(ReplacementTransform(syr7, syr8))
        syr9.next_to(syr8, DOWN*1.2)
        self.play(Write(syr9))
        syr10.next_to(syr9, DOWN*1.2)
        syr11.next_to(syr10, DOWN*1.2)
        self.play(Write(syr10))
        self.play(Write(syr11))
        self.wait(0.5)
        self.play(FadeOut(syr7, syr8, syr9, syr10), syr11.animate.center().shift(UP*1.8))
        syr12.next_to(syr11, DOWN*1.2)
        syr13.next_to(syr12, DOWN*1.2)
        self.play(Write(syr12))
        self.play(Write(syr13))
        self.wait(.25)
        self.play(syr13[-1:].animate.set_color(RED))
        self.wait(.25)
        syr14.center().shift(UP*1.8)
        syr15.next_to(syr14, DOWN*1.2)
        self.play(ReplacementTransform(syr11, syr14), FadeOut(syr13, syr12))
        self.play(Write(syr15))
        self.wait(0.5)

        self.play(FadeOut(titels[0], syr11, syr14, syr15))
        titels[1].to_corner(UP + LEFT)
        self.play(Write(titels[1]))
        self.wait(1.5)
        rac0 = Text('Racket:', font_size=30)
        rac1 = Text('Programmiersprache & Vereinfachung von λ', font_size=30)
        rac0.shift(UP*1.8)
        rac1.next_to(rac0, DOWN*1.5)
        self.play(Write(rac0))
        self.play(Write(rac1))
        self.wait()
        self.play(FadeOut(rac0, rac1))
        code = '''
        (define Y
            (λ (f)
                ((λ (x) (f (x x)))
                (λ (x) (f (x x))))))
        '''
        code1 = '''
        (define R
            (λ (r)
                (λ (n)
                    (if (zero? n)
                    0
                    (+ n (r (- n 1)))))))
        '''
        ycode = Code(code=code, tab_width=4, background="window",
                             language="Racket", font="Monospace", font_size=25)



        scode = Code(code=code1, tab_width=4, background="window",
                             language="rkt", font="Monospace", font_size=25)
        ytit = Text('Y-Kombinator', font_size=30)
        rfun = Text('R-Funktion', font_size=30)
        ytit.next_to(ycode, UP).to_edge(LEFT)
        rfun.next_to(scode, UP).to_edge(RIGHT)
        scode.scale(0.75).to_edge(RIGHT)
        ycode.scale(0.75).to_edge(LEFT)

        self.play(FadeIn(ycode), FadeIn(scode), Write(ytit), Write(rfun))
        self.wait()
        self.play(FadeOut(ycode, scode, ytit, rfun))
        outco = Code(code='((Y R) 3) = 6', tab_width=4, background="window",
                     language="rkt", font="Monospace", font_size=25)
        self.play(FadeIn(outco))
        self.wait()
        concode = '''
        (define sum
            (λ (n)
                (if (= 0 n)
                0
                (+ n (sum (- n 1))))))

        (sum 3) = 6
        '''

        condoe = Code(code=concode, tab_width=4, background="window",
                     language="rkt", font="Monospace", font_size=25)
        self.play(FadeOut(outco), FadeIn(condoe))

        self.wait(2)
        outro(self)











class test(Scene):
    def construct(self):
        ari.to_corner(UP+LEFT)
        sub_line = wline(self)
        sub_line.next_to(ari, DOWN)
        self.add(sub_line, ari)

        s = Text('Successor Funktion = S', font_size=35)
        s1 = Text('S(0) = 1', font_size=35)
        s2 = Text('S(S(0)) = 2', font_size=35)
        s.shift(UP*1.2)
        s1.next_to(s, DOWN)
        s2.next_to(s1, DOWN)
        self.play(Write(s))
        self.wait()
        self.play(Write(s1))
        self.play(Write(s2))
        self.wait()
        self.play(FadeOut(s, s1, s2))
        self.wait()




def outro(scene):
    scene.clear()
    outro_text = Text("Vielen Dank fürs Zuhören!", font_size=69)
    scene.play(Write(outro_text))
    scene.wait(2)



class syntax_node():
    def __init__(self, parent, value):
        self.parent = parent
        self.value = Text(value, font_size=20)
        self.children = []
        if parent != None:
            parent.add_child(self)

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_children(self):
        return self.children

    def set_position(self):
        l_const = DOWN * 2 + LEFT * 0.4
        r_const = DOWN * 2 + RIGHT * 0.4
        children = self.get_parent().get_children()

        if self.get_parent().get_parent() == None:
            l_const = l_const + LEFT*1.5
            r_const = r_const + RIGHT*1.5

        if self == children[0]:
            self.get_value().next_to(self.get_parent().get_value(), l_const)
        else:
            self.get_value().next_to(self.get_parent().get_value(), r_const)

    def recursive_animate(self, scene):
        if self.parent != None:
            self.set_position()
            scene.play(Create(self.get_line_to_parent()), run_time=0.3)

        scene.play(FadeIn(self.get_value()), run_time=0.3)
        for x in self.get_children():
            x.animate(scene)


    def extra_animate(self, scene, extra):
        extra.call()
        if self.parent != None:
            self.set_position()
            scene.play(Create(self.get_line_to_parent()), run_time=0.3)

        scene.play(FadeIn(self.get_value()), run_time=0.3)
        for x in self.get_children():
            x.extra_animate(scene, extra)

    def get_value(self):
        return self.value

    def get_parent(self):
        return self.parent

    def get_line_to_parent(self):
        offset = DOWN * 0.1
        offset_ = UP * 0.1
        return Line(start=self.parent.get_value().get_bottom() + offset, end=self.get_value().get_top() + offset_, color=WHITE,
                    stroke_width=0.75)
class extra_animation():
    def __init__(self, scene, animation_obj):
        self.counter = 0
        self.scene = scene
        self.animation_obj = animation_obj


    def call(self):
        self.play_animation()
        self.counter = self.counter+1

    def play_animation(self):
        if self.counter <= len(self.animation_obj)-1:
            self.scene.play(self.animation_obj[self.counter].animate.scale(1.2), run_time=0.2)
            self.scene.play(self.animation_obj[self.counter].animate.scale(1/1.2), run_time=0.15)