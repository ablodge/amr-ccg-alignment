AMRs (Abstract Meaning Representations) for the 1562 sentences of Le Petit Prince, a 1943 novel by Antoine de Saint-Exupery
Version 1.6 - March 14, 2016

1. Chapter 1 . (lpp_1943.1)

```
(c / chapter
  :mod 1)
```
2. Once when I was six years old I saw a magnificent picture in a book , called True Stories from Nature , about the primeval forest . (lpp_1943.2)

```
(s / see-01
      :ARG0 (i / i)
      :ARG1 (p / picture
            :mod (m / magnificent)
            :location (b2 / book :wiki -
                  :name (n / name :op1 "True" :op2 "Stories" :op3 "from" :op4 "Nature")
                  :topic (f / forest
                        :mod (p2 / primeval))))
      :mod (o / once)
      :time (a / age-01
            :ARG1 i
            :ARG2 (t / temporal-quantity :quant 6
                  :unit (y / year))))
```
3. It was a picture of a boa constrictor in the act of swallowing an animal . (lpp_1943.3)

```
(p / picture
  :domain (i / it)
  :topic (b2 / boa
           :mod (c2 / constrictor)
           :ARG0-of (s / swallow-01
                      :ARG1 (a / animal))))
```
4. Here is a copy of the drawing . (lpp_1943.4)

```
(b / be-located-at-91
      :ARG1 (t2 / thing
            :ARG2-of (c / copy-01
                  :ARG1 (p / picture
                        :ARG1-of (d / draw-01))))
      :ARG2 (h / here))
```
5. In the book it said : " Boa constrictors swallow their prey whole , without chewing it . (lpp_1943.5)

```
(s2 / say-01
      :ARG0 (b2 / book)
      :ARG1 (s / swallow-01
            :ARG0 (b / boa
                  :mod (c / constrictor))
            :ARG1 (p / prey
                  :mod (w / whole)
                  :poss b)
            :manner (c2 / chew-01 :polarity -
                  :ARG0 b
                  :ARG1 p)))
```
6. After that they are not able to move , and they sleep through the six months that they need for digestion . " (lpp_1943.6)

```
(a / and
      :op1 (p / possible-01 :polarity -
            :ARG1 (m / move-01
                  :ARG0 (t / they)
                  :time (a2 / after
                        :op1 (t3 / that))))
      :op2 (s / sleep-01
            :ARG0 t
            :duration (t2 / temporal-quantity :quant 6
                  :unit (m2 / month)
                  :ARG1-of (n / need-01
                        :ARG0 t
                        :purpose (d / digest-01
                              :ARG0 t)))))
```
7. I pondered deeply , then , over the adventures of the jungle . (lpp_1943.7)

```
(p / ponder-01
      :ARG0 (i / i)
      :ARG1 (a / adventure
            :location (j / jungle))
      :ARG1-of (d / deep-02)
      :time (t / then))
```
8. And after some work with a colored pencil I succeeded in making my first drawing . (lpp_1943.8)

```
(a2 / and
      :op2 (s / succeed-01
            :ARG0 (i / i)
            :ARG1 (m / make-01
                  :ARG0 i
                  :ARG1 (p2 / picture
                        :ARG1-of (d / draw-01
                              :ARG0 i
                              :ord (o / ordinal-entity :value 1))))
            :time (a / after
                  :op1 (w / work-01
                        :ARG0 i
                        :instrument (p / pencil
                              :mod (c / color))
                        :mod (s2 / some)))))
```
9. My Drawing Number One . (lpp_1943.9)

```
(p / picture :wiki -
      :name (n2 / name :op1 "Drawing" :op2 "Number" :op3 "One")
      :poss (i / i))
```
10. It looked like this : I showed my masterpiece to the grown - ups , and asked them whether the drawing frightened them . (lpp_1943.10)

```
(a / and
      :op1 (l / look-02
            :ARG0 (i / it)
            :ARG1 (t / this))
      :op2 (s / show-01
            :ARG0 (i2 / i)
            :ARG1 (m / masterpiece
                  :poss i2)
            :ARG2 (g / grown-up))
      :op3 (a2 / ask-01
            :ARG0 i2
            :ARG1 (f / frighten-01 :mode interrogative
                  :ARG0 (p / picture
                        :ARG1-of (d / draw-01))
                  :ARG1 g)
            :ARG2 g))
```
11. But they answered : " Frighten ? (lpp_1943.11)

```
(c / contrast-01
  :ARG2 (a / answer-01
          :ARG0 (t / they)
          :ARG2 (f / frighten-01
                  :mode interrogative)))
```
12. Why should any one be frightened by a hat ? " (lpp_1943.12)

```
(f / frighten-01
  :ARG0 (h / hat)
  :ARG1 (o / one
          :mod (a / any))
  :ARG1-of (c / cause-01
             :ARG0 (a2 / amr-unknown)))
```
13. My drawing was not a picture of a hat . (lpp_1943.13)

```
(p / picture-01 :polarity -
      :ARG0 (p2 / picture
            :ARG1-of (d / draw-01
                  :ARG0 (i / i)))
      :ARG1 (h / hat))
```
14. It was a picture of a boa constrictor digesting an elephant . (lpp_1943.14)

```
(p / picture-01
  :ARG0 (i / it)
  :ARG1 (b2 / boa
          :mod (c / constrictor)
          :ARG0-of (d / digest-01
                     :ARG1 (e / elephant))))
```
15. But since the grown - ups were not able to understand it , I made another drawing : I drew the inside of the boa constrictor , so that the grown - ups could see it clearly . (lpp_1943.15)

```
(c / contrast-01
      :ARG2 (a2 / and
            :op1 (d3 / draw-01
                  :ARG0 (i / i)
                  :ARG1 (p2 / picture
                        :mod (a / another))
                  :ARG1-of (c3 / cause-01
                        :ARG0 (p3 / possible-01 :polarity -
                              :ARG1 (u / understand-01
                                    :ARG0 (g / grown-up)
                                    :ARG1 (i2 / it)))))
            :op2 (d / draw-01
                  :ARG0 i
                  :ARG1 (i3 / inside
                        :part-of (b2 / boa
                              :mod (c4 / constrictor)))
                  :purpose (p / possible-01
                        :ARG1 (s / see-01
                              :ARG0 g
                              :ARG1 (i4 / it)
                              :ARG1-of (c2 / clear-06))))))
```
16. They always need to have things explained . (lpp_1943.16)

```
(n / need-01
      :ARG0 (t / they)
      :ARG1 (e / explain-01)
      :time (a / always))
```
17. My Drawing Number Two looked like this : The grown - ups ' response , this time , was to advise me to lay aside my drawings of boa constrictors , whether from the inside or the outside , and devote myself instead to geography , history , arithmetic and grammar . (lpp_1943.17)

```
(a6 / and
      :op1 (l / look-02
            :ARG0 (p / picture :wiki - :name (n / name :op1 "Drawing" :op2 "Number" :op3 "Two")
                  :poss i)
            :ARG1 (t2 / this))
      :op2 (r / respond-01
            :ARG0 (g / grown-up)
            :ARG1 (i / i)
            :ARG2 (a / advise-01
                  :ARG0 g
                  :ARG1 i
                  :ARG2 (a3 / and
                        :op1 (l2 / lay-01
                              :ARG0 i
                              :ARG1 (p2 / picture
                                    :ARG1-of (d2 / draw-01
                                          :ARG0 i)
                                    :topic (b2 / boa
                                          :mod (c2 / constrictor)
                                          :mod (o / or
                                                :op1 (i2 / inside)
                                                :op2 (o2 / outside))))
                              :ARG2 (a2 / aside))
                        :op2 (d3 / devote-01
                              :ARG0 i
                              :ARG1 i
                              :ARG2 (a4 / and
                                    :op1 (g2 / geography)
                                    :op2 (h / history)
                                    :op3 (a5 / arithmetic)
                                    :op4 (g3 / grammar))
                              :ARG1-of (i4 / instead-of-91
                                    :ARG2 d2))))
            :time (t4 / time
                  :mod (t5 / this))))
```
18. That is why , at the age of six , I gave up what might have been a magnificent career as a painter . (lpp_1943.18)

```
(c2 / cause-01
      :ARG0 (t2 / that)
      :ARG1 (g / give-up-07
            :ARG0 (i / i)
            :ARG1 (c / career
                  :mod (m / magnificent)
                  :topic (p / person
                        :ARG0-of (p2 / paint-02)))
            :time (a / age-01
                  :ARG1 i
                  :ARG2 (t / temporal-quantity :quant 6
                        :unit (y / year)))))
```
19. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two . (lpp_1943.19)

```
(d / dishearten-01
      :ARG0 (f / fail-01
            :ARG1 (a / and
                  :op1 (p / picture :wiki -
                        :name (n / name :op1 "Drawing" :op2 "Number" :op3 "One"))
                  :op2 (p2 / picture :wiki -
                        :name (n2 / name :op1 "Drawing" :op2 "Number" :op3 "Two"))
                  :poss i))
      :ARG1 (i / i))
```
20. Grown - ups never understand anything by themselves , and it is tiresome for children to be always and forever explaining things to them . (lpp_1943.20)

```
(a / and
      :op1 (u / understand-01 :polarity -
            :ARG0 (g / grown-up)
            :ARG1 (a3 / anything)
            :time (e2 / ever)
            :mod (b / by-oneself))
      :op2 (t / tiresome
            :domain (e / explain-01
                  :ARG0 (c / child)
                  :ARG1 (t2 / thing)
                  :ARG2 g
                  :time (a4 / always)
                  :mod (f / forever))))
```
21. So then I chose another profession , and learned to pilot airplanes . (lpp_1943.21)

```
(c2 / cause-01
  :ARG1 (a / and
          :op1 (c / choose-01
                 :ARG0 (i / i)
                 :ARG1 (p / profession
                         :mod (a2 / another)))
          :op2 (l / learn-01
                 :ARG0 i
                 :ARG1 (p2 / pilot-01
                         :ARG0 i
                         :ARG1 (a3 / airplane)))))
```
22. I have flown a little over all parts of the world ; and it is true that geography has been very useful to me . (lpp_1943.22)

```
(a / and
      :op1 (f / fly-01
            :ARG0 i
            :location (o / over
                  :op1 (p2 / part
                        :part-of (w / world))))
      :op2 (u / useful-05
            :ARG0 (i / i)
            :ARG1 (g / geography)
            :degree (v / very)))
```
23. At a glance I can distinguish China from Arizona . (lpp_1943.23)

```
(p / possible-01
      :ARG1 (d / distinguish-01
            :ARG0 (i / i)
            :ARG1 (c / country :wiki "China"
                  :name (n / name :op1 "China"))
            :ARG2 (s / state :wiki "Arizona"
                  :name (n2 / name :op1 "Arizona"))
            :manner (g / glance-01
                  :ARG0 i)))
```
24. If one gets lost in the night , such knowledge is valuable . (lpp_1943.24)

```
(v / value-02
      :ARG1 (k / knowledge
            :mod (s / such))
      :condition (g / get-03
            :ARG1 (o / one)
            :ARG2 (l / lost
                  :time (d / date-entity :dayperiod (n / night)))))
```
25. In the course of this life I have had a great many encounters with a great many people who have been concerned with matters of consequence . (lpp_1943.25)

```
(e / encounter-01
  :ARG0 (i / i)
  :ARG1 (p / person
          :quant (m2 / many
                   :mod (g2 / great))
          :ARG1-of (c / concern-01
                     :ARG0 (m3 / matter
                             :mod (c2 / consequence))))
  :quant (m / many
           :mod (g / great))
  :time (c3 / course
          :poss (l / life
                  :mod (t / this))))
```
26. I have lived a great deal among grown - ups . (lpp_1943.26)

```
(l / live-01
      :ARG0 (i / i)
      :mod (d / deal
            :mod (g2 / great))
      :location (a / among
            :op1 (g / grown-up)))
```
27. I have seen them intimately , close at hand . (lpp_1943.27)

```
(s / see-01
      :ARG0 (i / i)
      :ARG1 (t / they)
      :ARG1-of (c / close-10
            :ARG2 (a / at-hand))
      :ARG2-of (i2 / intimate-02
            :ARG1 i))
```
28. And that has n't much improved my opinion of them . (lpp_1943.28)

```
(a / and
      :op2 (i / improve-01 :polarity -
            :ARG0 (t / that)
            :ARG1 (t3 / thing
                  :ARG1-of (o2 / opine-01
                        :ARG0 (i2 / i)
                        :topic (t2 / they)))
            :degree (m2 / much)))
```
29. Whenever I met one of them who seemed to me at all clear - sighted , I tried the experiment of showing him my Drawing Number One , which I have always kept . (lpp_1943.29)

```
(t / try-01
      :ARG0 (i / i)
      :ARG1 (e / experiment-01
            :ARG1 (s / show-01
                  :ARG1 (p2 / picture :wiki - :name (n / name :op1 "Drawing" :op2 "Number" :op3 "One"))
                  :ARG2 p
                  :ARG1-of (k / keep-01
                        :ARG0 i
                        :time (a / always))))
      :time (m / meet-02
            :ARG0 i
            :ARG1 (p / person
                  :ARG1-of (i2 / include-91
                        :ARG2 (t3 / they))
                  :ARG0-of (s3 / see-01
                        :ARG1-of (c / clear-08)
                        :ARG1-of (s4 / seem-01
                              :ARG2 i)))
            :mod (a2 / any)))
```
30. I would try to find out , so , if this was a person of true understanding . (lpp_1943.30)

```
(t / try-01
      :ARG0 (i / i)
      :ARG1 (f / find-out-03
            :ARG0 i
            :ARG1 (u2 / understand-01 :mode interrogative
                  :ARG0 (p / person
                        :mod (t2 / this))
                  :ARG1-of (t3 / true-01))))
```
31. But , whoever it was , he , or she , would always say : " That is a hat . " (lpp_1943.31)

```
(c / contrast-01
  :ARG2 (s / say-01
          :ARG0 (o / or
                  :op1 (h / he)
                  :op2 (s2 / she))
          :ARG1 (h2 / hat
                  :domain (t / that))
          :time (a / always)))
```
32. Then I would never talk to that person about boa constrictors , or primeval forests , or stars . (lpp_1943.32)

```
(t / talk-01
  :ARG0 (i / i)
  :ARG1 (o / or
          :op1 (b / boa
                 :mod (c2 / constrictor))
          :op2 (f / forest
                 :mod (p2 / primeval))
          :op3 (s / star))
  :ARG2 (p / person
          :mod (t2 / that))
  :time (e / ever)
  :polarity -)
```
33. I would bring myself down to his level . (lpp_1943.33)

```
(b / bring-01
      :ARG0 (i / i)
      :ARG1 i
      :ARG2 (l / level
            :poss (h / he))
      :ARG3 (d / down))
```
34. I would talk to him about bridge , and golf , and politics , and neckties . (lpp_1943.34)

```
(t / talk-01
  :ARG0 (i / i)
  :ARG1 (a / and
          :op1 (b / bridge)
          :op2 (g / golf)
          :op3 (p / politics)
          :op4 (n2 / necktie))
  :ARG2 (h / he))
```
35. And the grown - up would be greatly pleased to have met such a sensible man . (lpp_1943.35)

```
(a / and
      :op2 (p / please-01
            :ARG0 (m / meet-02
                  :ARG0 g
                  :ARG1 (m2 / man
                        :ARG2-of (s / sense-02
                              :degree (s2 / such))))
            :ARG1 (g / grown-up)
            :degree (g2 / great)))
```
36. Chapter 2 . (lpp_1943.36)

```
(c / chapter
  :mod 2)
```
37. So I lived my life alone , without anyone that I could really talk to , until I had an accident with my plane in the Desert of Sahara , six years ago . (lpp_1943.37)

```
(c / cause-01
      :ARG1 (l / live-01
            :ARG0 (i / i
                  :ARG0-of (t3 / talk-01 :polarity -
                        :ARG2 (a5 / anyone)
                        :ARG1-of (r / real-04)))
            :ARG1 (l2 / life
                  :poss i)
            :manner (a / alone)
            :duration (u / until
                  :op1 (h / have-06
                        :ARG0 i
                        :ARG1 (a3 / accident
                              :mod (p / plane))
                        :location (d / desert :wiki "Sahara" :name (n / name :op1 "Desert" :op2 "of" :op3 "Sahara"))
                        :time (b / before
                              :op1 (n2 / now)
                              :quant (t2 / temporal-quantity :quant 6
                                    :unit (y / year)))))))
```
38. Something was broken in my engine . (lpp_1943.38)

```
(b / break-01
      :ARG1 (s / something
            :location (e / engine
                  :poss (i / i))))
```
39. And as I had with me neither a mechanic nor any passengers , I set myself to attempt the difficult repairs all alone . (lpp_1943.39)

```
(a / and
  :op2 (c / cause-01
         :ARG0 (h / have-03
                 :ARG0 i
                 :ARG1 (o / or
                         :op1 (m / mechanic)
                         :op2 (p / passenger))
                 :accompanier (i / i)
                 :polarity -)
         :ARG1 (a2 / attempt-01
                 :ARG0 i
                 :ARG1 (r / repair-01
                         :mod (d / difficult))
                 :mod (a3 / alone
                        :degree (a4 / all)))))
```
40. It was a question of life or death for me : I had scarcely enough drinking water to last a week . (lpp_1943.40)

```
(q / question-01
      :ARG0 i
      :ARG1 (o / or
            :op1 (l / live-01)
            :op2 (d / die-01))
      :ARG1-of (c / cause-01
            :ARG0 (h / have-03
                  :ARG0 (i / i)
                  :ARG1 (w / water
                        :purpose (d2 / drink-01
                              :ARG0 i)
                        :quant (e / enough
                              :mod (s / scarce))
                        :ARG1-of (l2 / last-03
                              :ARG2 (t / temporal-quantity :quant 1
                                    :unit (w2 / week))
                              :ARG3 i)))))
```
41. The first night , then , I went to sleep on the sand , a thousand miles from any human habitation . (lpp_1943.41)

```
(s / sleep-01
      :ARG0 (i / i)
      :location (s2 / sand)
      :time (d2 / date-entity
            :dayperiod (n / night)
            :ord (o / ordinal-entity :value 1))
      :location (r / relative-position
            :op1 (p / place
                  :ARG1-of (i2 / inhabit-01
                        :ARG0 (h / human))
                  :mod (a2 / any))
            :quant (d / distance-quantity :quant 1000
                  :unit (m / mile))
            :direction (a3 / away)))
```
42. I was more isolated than a shipwrecked sailor on a raft in the middle of the ocean . (lpp_1943.42)

```
(i / isolate-01
      :ARG1 (i2 / i)
      :degree (m / more)
      :compared-to (p / person
            :ARG0-of (s / sail-01)
            :ARG1-of (s2 / shipwreck-01)
            :location (r / raft
                  :location (o / ocean
                        :part (m2 / middle)))))
```
43. Thus you can imagine my amazement , at sunrise , when I was awakened by an odd little voice . (lpp_1943.43)

```
(c / cause-01
      :ARG1 (p / possible-01
            :ARG1 (i2 / imagine-01
                  :ARG0 (y / you)
                  :ARG1 (a / amaze-01
                        :ARG1 (i / i)
                        :time (s / sunrise
                              :time-of (w / wake-01
                                    :ARG0 (v / voice
                                          :mod (o / odd)
                                          :mod (l / little))
                                    :ARG1 i))))))
```
44. It said : " If you please -- draw me a sheep ! " (lpp_1943.44)

```
(s / say-01
      :ARG0 (i / it)
      :ARG1 (d / draw-01 :mode imperative :polite +
            :ARG0 (y2 / you)
            :ARG1 (s2 / sheep)
            :ARG2 (i2 / i)))
```
45. " What ! " (lpp_1943.45)

```
(s / string-entity :value "what")
```
46. " Draw me a sheep ! " (lpp_1943.46)

```
(d / draw-01
  :ARG0 (y / you)
  :ARG1 (s / sheep)
  :ARG2 (i / i)
  :mode imperative)
```
47. I jumped to my feet , completely thunderstruck . (lpp_1943.47)

```
(j / jump-03
      :ARG0 (i / i
            :mod (t / thunderstruck
                  :ARG1-of (c / complete-02)))
      :destination (f / foot
            :part-of i))
```
48. I blinked my eyes hard . (lpp_1943.48)

```
(b / blink-01
      :ARG0 (i / i)
      :ARG1 (e / eye
            :part-of i)
      :ARG1-of (h / hard-04))
```
49. I looked carefully all around me . (lpp_1943.49)

```
(l / look-01
      :ARG0 (i / i)
      :direction (a / around
            :op1 i
            :mod (a2 / all))
      :manner (c / careful))
```
50. And I saw a most extraordinary small person , who stood there examining me with great seriousness . (lpp_1943.50)

```
(a / and
      :op2 (s / see-01
            :ARG0 (i / i)
            :ARG1 (p / person
                  :mod (s2 / small)
                  :mod (e / extraordinary
                        :degree (m / most))
                  :ARG1-of (s3 / stand-01
                        :ARG2 (t / there))
                  :ARG0-of (e2 / examine-01
                        :ARG1 i
                        :ARG2-of (s4 / serious-01
                              :degree (g / great))))))
```
51. Here you may see the best portrait that , later , I was able to make of him . (lpp_1943.51)

```
(p / possible-01
      :ARG1 (s / see-01
            :ARG0 (y / you)
            :ARG1 (p2 / portrait
                  :ARG1-of (g / good-02
                        :degree (m / most))
                  :ARG1-of (m2 / make-01
                        :ARG0 (i / i)
                        :ARG1-of (p3 / possible-01)
                        :time (l / late
                              :degree (m3 / more)))
                  :topic (h / he))
            :location (h2 / here)))
```
52. But my drawing is certainly very much less charming than its model . (lpp_1943.52)

```
(c3 / contrast-01
      :ARG2 (c / charm-01
            :ARG0 (p / picture
                  :ARG1-of (d / draw-01
                        :ARG0 (i / i)))
            :quant (l / less
                  :degree (m / much
                        :degree (v / very)))
            :mod (c2 / certain)
            :compared-to (m2 / model
                  :poss p)))
```
53. That , however , is not my fault . (lpp_1943.53)

```
(c / contrast-01
  :ARG2 (f / fault-01
          :ARG1 (i / i)
          :ARG2 (t / that)
          :polarity -))
```
54. The grown - ups discouraged me in my painter 's career when I was six years old , and I never learned to draw anything , except boas from the outside and boas from the inside . (lpp_1943.54)

```
(d / discourage-01
      :ARG0 (g / grown-up)
      :ARG1 (i / i)
      :ARG2 (c / career
            :topic (p / person
                  :ARG0-of (p2 / paint-02))
            :poss i)
      :ARG0-of (c2 / cause-01
            :ARG1 (l / learn-01 :polarity -
                  :ARG0 i
                  :ARG1 (d2 / draw-01
                        :ARG0 i
                        :ARG1 (a2 / anything))
                  :time (e / ever)
                  :ARG2-of (e2 / except-01
                        :ARG1 (a3 / and
                              :op1 (b / boa
                                    :direction (f / from
                                          :op1 (o / outside)))
                              :op2 (b2 / boa
                                    :direction (f2 / from
                                          :op1 (i2 / inside)))))))
      :time (a / age-01
            :ARG1 i
            :ARG2 (t2 / temporal-quantity :quant 6
                  :unit (y / year))))
```
55. Now I stared at this sudden apparition with my eyes fairly starting out of my head in astonishment . (lpp_1943.55)

```
(s / stare-01
      :ARG0 (i / i)
      :ARG1 (t / thing
            :ARG1-of (a / appear-01
                  :manner (s2 / sudden))
            :mod (t2 / this))
      :time (n / now)
      :manner (s3 / start-03
            :ARG0 (e / eye
                  :part-of i)
            :ARG1-of (c / cause-01
                  :ARG0 (a2 / astonish-01
                        :ARG1 i))
            :degree (f / fair)
            :manner (o / out-06
                  :ARG1 e
                  :ARG2 (h / head
                        :part-of i))))
```
56. Remember , I had crashed in the desert a thousand miles from any inhabited region . (lpp_1943.56)

```
(r / remember-01
  :ARG0 (y / you)
  :ARG1 (c / crash-01
          :ARG1 (i / i)
          :location (d / desert)
          :location (r3 / relative-position
                      :op1 (r2 / region
                             :ARG1-of (i2 / inhabit-01)
                             :mod (a2 / any))
                      :quant (d2 / distance-quantity
                               :unit (m / mile)
                               :quant 1000)
                      :direction (a / away)))
  :mode imperative)
```
57. And yet my little man seemed neither to be straying uncertainly among the sands , nor to be fainting from fatigue or hunger or thirst or fear . (lpp_1943.57)

```
(c3 / contrast-01
  :ARG2 (s / seem-01
          :ARG1 (a / and
                  :op1 (s2 / stray-01
                         :ARG0 (m / man
                                 :mod (l / little)
                                 :poss (i / i))
                         :ARG1 (a3 / among
                                 :op1 (s3 / sand))
                         :manner (c / certain
                                   :polarity -)
                         :polarity -)
                  :op2 (f / faint-01
                         :ARG0 m
                         :ARG1-of (c2 / cause-01
                                    :ARG0 (o / or
                                            :op1 (f2 / fatigue-01)
                                            :op2 (h / hunger-01)
                                            :op3 (t / thirst-01)
                                            :op4 (f3 / fear-01)))
                         :polarity -))))
```
58. Nothing about him gave any suggestion of a child lost in the middle of the desert , a thousand miles from any human habitation . (lpp_1943.58)

```
(s / suggest-01
  :ARG0 (n / nothing
          :topic (h / he))
  :ARG1 (c / child
          :ARG1-of (l / lose-02
                     :location (d / desert
                                 :part (m / middle))
                     :location (r / relative-position
                                 :op1 (t / thing
                                        :ARG1-of (i / inhabit-01
                                                   :ARG0 (h2 / human))
                                        :mod (a3 / any))
                                 :quant (d2 / distance-quantity
                                          :unit (m2 / mile)
                                          :quant 1000)
                                 :direction (a2 / away)))))
```
59. When at last I was able to speak , I said to him : " But -- what are you doing here ? " (lpp_1943.59)

```
(s / say-01
      :ARG0 (i / i)
      :ARG1 (c / contrast-01
            :ARG2 (b2 / be-located-at-91 :mode interrogative
                  :ARG1 (y2 / you)
                  :ARG2 (h2 / here)
                  :ARG1-of (c2 / cause-01
                        :ARG0 (a / amr-unknown))))
      :ARG2 (h / he)
      :time (p / possible-01
            :ARG1 (s2 / speak-01
                  :ARG0 i
                  :time (a2 / at-last))))
```
60. And in answer he repeated , very slowly , as if he were speaking of a matter of great consequence : " If you please -- draw me a sheep ... " (lpp_1943.60)

```
(a / and
      :op2 (r / repeat-01
            :ARG0 (h / he)
            :ARG1 (d / draw-01 :mode imperative :polite +
                  :ARG0 (y2 / you)
                  :ARG1 (s3 / sheep)
                  :ARG2 (i / i))
            :purpose (a2 / answer-01
                  :ARG0 h)
            :ARG1-of (s / slow-05
                  :degree (v / very))
            :conj-as-if (s2 / speak-01
                  :ARG0 h
                  :ARG1 (m / matter
                        :mod (c / consequence
                              :mod (g / great))))))
```
61. When a mystery is too overpowering , one dare not disobey . (lpp_1943.61)

```
(d / dare-01
  :ARG0 (o / one)
  :ARG2 (d2 / disobey-01
          :ARG0 o)
  :polarity -
  :time (o2 / overpower-01
          :ARG0 (m / mystery)
          :degree (t2 / too)))
```
62. Absurd as it might seem to me , a thousand miles from any human habitation and in danger of death , I took out of my pocket a sheet of paper and my fountain - pen . (lpp_1943.62)

```
(t / take-01
      :ARG0 (i / i
            :location (r / relative-position
                  :op1 (p5 / place
                        :mod (a3 / any)
                        :ARG1-of (i2 / inhabit-01
                              :ARG0 (h / human)))
                  :quant (d / distance-quantity :quant 1000
                        :unit (m / mile))
                  :direction (a2 / away))
            :ARG1-of (e / endanger-01
                  :ARG0 (d2 / die-01
                        :ARG1 i)))
      :ARG1 (a / and
            :op1 (p / paper
                  :quant (s / sheet :quant 1))
            :op2 (p2 / pen
                  :mod (f / fountain)
                  :poss i))
      :ARG2 (p3 / pocket
            :poss i)
      :concession (p4 / possible-01
            :ARG1 (s2 / seem-01
                  :ARG1 (a4 / absurd)
                  :ARG2 i)))
```
63. But then I remembered how my studies had been concentrated on geography , history , arithmetic , and grammar , and I told the little chap ( a little crossly , too ) that I did not know how to draw . (lpp_1943.63)

```
(c4 / contrast-01
      :ARG2 (a / and
            :op1 (r / remember-01
                  :ARG0 (i / i)
                  :ARG1 (c / concentrate-01
                        :ARG1 (a2 / and
                              :op1 (g / geography)
                              :op2 (h / history)
                              :op3 (a3 / arithmetic)
                              :op4 (g2 / grammar))
                        :ARG2 (s / study-01
                              :ARG0 i))
                  :time (t / then))
            :op2 (t2 / tell-01
                  :ARG0 i
                  :ARG1 (k / know-03 :polarity -
                        :ARG0 i
                        :ARG1 (d / draw-01
                              :ARG0 i))
                  :ARG2 (c2 / chap
                        :mod (l / little))
                  :manner (c3 / cross
                        :mod (l2 / little)
                        :mod (a4 / also)))))
```
64. He answered me : " That does n't matter . (lpp_1943.64)

```
(a / answer-01
  :ARG0 (h / he)
  :ARG1 (i / i)
  :ARG2 (m2 / matter-01
          :ARG1 (t / that)
          :polarity -))
```
65. Draw me a sheep ... " (lpp_1943.65)

```
(d / draw-01
  :ARG0 (y / you)
  :ARG1 (s / sheep)
  :ARG2 (i / i)
  :mode imperative)
```
66. But I had never drawn a sheep . (lpp_1943.66)

```
(c / contrast-01
  :ARG2 (d / draw-01
          :ARG0 (i / i)
          :ARG1 (s / sheep)
          :time (e / ever)
          :polarity -))
```
67. So I drew for him one of the two pictures I had drawn so often . (lpp_1943.67)

```
(c / cause-01
  :ARG1 (d / draw-01
          :ARG0 (i / i)
          :ARG1 (p / picture
                  :quant 1
                  :ARG1-of (i2 / include-91
                             :ARG2 (p2 / picture
                                     :quant 2
                                     :ARG1-of (d2 / draw-01
                                                :ARG0 i
                                                :time (o / often
                                                        :degree (s / so))))))
          :ARG2 (h / he)))
```
68. It was that of the boa constrictor from the outside . (lpp_1943.68)

```
(b / boa
      :mod (c2 / constrictor)
      :direction (f / from
            :op1 (o / outside)))
```
69. And I was astounded to hear the little fellow greet it with , " No , no , no ! (lpp_1943.69)

```
(a / and
  :op2 (a2 / astound-01
         :ARG0 (h / hear-01
                 :ARG0 i
                 :ARG1 (g / greet-01
                         :ARG0 f
                         :ARG1 (i2 / it)
                         :ARG3 (a3 / and
                                 :op1 (n / no)
                                 :op2 (n2 / no)
                                 :op3 (n3 / no)))
                 :ARG2 (f / fellow
                         :mod (l / little)))
         :ARG1 (i / i)))
```
70. I do not want an elephant inside a boa constrictor . (lpp_1943.70)

```
(w / want-01
  :ARG0 (i / i)
  :ARG1 (e / elephant
          :location (i2 / inside
                      :op1 (b2 / boa
                             :mod (c2 / constrictor))))
  :polarity -)
```
71. A boa constrictor is a very dangerous creature , and an elephant is very cumbersome . (lpp_1943.71)

```
(a / and
  :op1 (c2 / creature
         :mod (d2 / dangerous)
         :domain (b / boa
                   :mod (c / constrictor)))
  :op2 (c3 / cumbersome
         :degree (v2 / very)
         :domain (e / elephant)))
```
72. Where I live , everything is very small . (lpp_1943.72)

```
(s / small
  :degree (v / very)
  :domain (e / everything)
  :location (l2 / live-01
              :ARG0 (i / i)))
```
73. What I need is a sheep . (lpp_1943.73)

```
(n / need-01
  :ARG0 (i / i)
  :ARG1 (s / sheep))
```
74. Draw me a sheep . " (lpp_1943.74)

```
(d / draw-01
  :ARG0 (y / you)
  :ARG1 (s / sheep)
  :ARG2 (i / i)
  :mode imperative)
```
75. So then I made a drawing . (lpp_1943.75)

```
(c / cause-01
  :ARG1 (d / draw-01
          :ARG0 (i / i)
          :time (t2 / then)))
```
76. He looked at it carefully , then he said : " No . (lpp_1943.76)

```
(a / and
  :op1 (l / look-01
         :ARG0 (h / he)
         :ARG1 (i / it)
         :manner (c / careful))
  :op2 (s / say-01
         :ARG0 h
         :ARG1 (n / no)
         :time (t / then)))
```
77. This sheep is already very sickly . (lpp_1943.77)

```
(s2 / sick-05
      :ARG1 (s / sheep
            :mod (t / this))
      :degree (v / very)
      :time (a / already))
```
78. Make me another . " (lpp_1943.78)

```
(m / make-01
  :ARG0 (y / you)
  :ARG1 (a / another)
  :ARG3 (i / i)
  :mode imperative)
```
79. So I made another drawing . (lpp_1943.79)

```
(c / cause-01
      :ARG1 (m / make-01
            :ARG0 (i / i)
            :ARG1 (p / picture
                  :ARG1-of (d / draw-01
                        :ARG0 i)
                  :mod (a / another))))
```
80. My friend smiled gently and indulgently . (lpp_1943.80)

```
(s / smile-01
      :ARG0 (p / person
            :ARG0-of (h / have-rel-role-91
                  :ARG1 (i / i)
                  :ARG2 (f / friend)))
      :manner (g / gentle)
      :manner (i2 / indulgent))
```
81. " You see yourself , " he said , " that this is not a sheep . (lpp_1943.81)

```
(s / say-01
  :ARG0 (h / he)
  :ARG1 (s2 / see-01
          :ARG0 (y / you)
          :ARG1 (s4 / sheep
                  :domain (t2 / this)
                  :polarity -)))
```
82. This is a ram . (lpp_1943.82)

```
(r2 / ram
  :domain (t2 / this))
```
83. It has horns . " (lpp_1943.83)

```
(h / have-03
      :ARG0 (i / it)
      :ARG1 (h2 / horn))
```
84. So then I did my drawing over once more . (lpp_1943.84)

```
(c / cause-01
      :ARG1 (d / do-02
            :ARG0 (i / i)
            :ARG1 (p / picture
                  :ARG1-of (d2 / draw-01
                        :ARG0 i))
            :mod (o / over)
            :mod (a / again :frequency 1)
            :time (t2 / then)))
```
85. But it was rejected too , just like the others . (lpp_1943.85)

```
(c / contrast-01
      :ARG1 (r / reject-01
            :ARG1 (i / it)
            :ARG1-of (r2 / resemble-01
                  :ARG2 (o / other))
            :mod (t / too)))
```
86. " This one is too old . (lpp_1943.86)

```
(o2 / old
  :degree (t2 / too)
  :domain (o / one
            :mod (t / this)))
```
87. I want a sheep that will live a long time . " (lpp_1943.87)

```
(w / want-01
      :ARG0 (i / i)
      :ARG1 (s / sheep
            :ARG0-of (l / live-01
                  :ARG1-of (l2 / long-03))))
```
88. By this time my patience was exhausted , because I was in a hurry to start taking my engine apart . (lpp_1943.88)

```
(e / exhaust-01
      :ARG1 (p / patient-01
            :ARG1 (i / i))
      :ARG1-of (c / cause-01
            :ARG0 (h / hurry-01
                  :ARG1 i
                  :ARG2 (s / start-01
                        :ARG0 i
                        :ARG1 (d / disassemble-01
                              :ARG0 i
                              :ARG1 (e2 / engine
                                    :poss i)))))
      :time (b / by
            :op1 (t / time
                  :mod (t2 / this))))
```
89. So I tossed off this drawing . (lpp_1943.89)

```
(c / cause-01
      :ARG1 (t / toss-out-02
            :ARG0 (i / i)
            :ARG1 (p / picture
                  :ARG1-of (d / draw-01
                        :ARG0 i)
                  :mod (t3 / this))
            :direction (o / off)))
```
90. And I threw out an explanation with it . (lpp_1943.90)

```
(a / and
  :op2 (e / explain-01
         :ARG0 (i / i)
         :ARG1 (i3 / it)))
```
91. " This is only his box . (lpp_1943.91)

```
(b / box
  :poss (h / he)
  :domain (t / this)
  :mod (o / only))
```
92. The sheep you asked for is inside . " (lpp_1943.92)

```
(b / be-located-at-91
      :ARG1 (s2 / sheep
            :ARG1-of (a / ask-01
                  :ARG0 (y / you)))
      :ARG2 (i2 / inside))
```
93. I was very surprised to see a light break over the face of my young judge : " That is exactly the way I wanted it ! (lpp_1943.93)

```
(a / and
      :op1 (s / surprise-01
            :ARG0 (s2 / see-01
                  :ARG0 i
                  :ARG1 (b / break-13
                        :ARG1 (l / light)
                        :location (o / over
                              :op1 (f / face
                                    :part-of (p / person
                                          :ARG0-of (j / judge-01)
                                          :poss i
                                          :mod (y / young))))))
            :ARG1 (i / i)
            :degree (v / very))
      :op2 (s3 / say-01
            :ARG1 (w / way
                  :mod (e / exact)
                  :domain (w2 / want-01
                        :ARG0 p
                        :ARG1 (i2 / it)))))
```
94. Do you think that this sheep will have to have a great deal of grass ? " (lpp_1943.94)

```
(t / think-01
  :ARG0 (y / you)
  :ARG1 (o / obligate-01
          :ARG2 (h / have-03
                  :ARG0 (s / sheep
                          :mod (t2 / this))
                  :ARG1 (g / grass
                          :quant (d / deal
                                   :mod (g2 / great)))))
  :mode interrogative)
```
95. " Why ? " (lpp_1943.95)

```
(c / cause-01
      :ARG0 (a / amr-unknown))
```
96. " Because where I live everything is very small ... " (lpp_1943.96)

```
(c / cause-01
  :ARG0 (s / small
          :degree (v / very)
          :domain (e / everything
                    :location (l / live-01
                                :ARG0 (i / i)))))
```
97. " There will surely be enough grass for him , " (lpp_1943.97)

```
(b / benefit-01
      :ARG0 (g3 / grass
            :mod (e3 / enough
                  :ARG1-of (s / sure-02)))
      :ARG1 (h2 / he))
```
98. I said . (lpp_1943.98)

```
(s / say-01
      :ARG0 (i / i))
```
99. " It is a very small sheep that I have given you . " (lpp_1943.99)

```
(g / give-01
      :ARG0 (i / i)
      :ARG1 (s / sheep
            :mod (s2 / small
                  :degree (v / very)))
      :ARG2 (y / you))
```
100. He bent his head over the drawing : " Not so small that -- Look ! (lpp_1943.100)

```
(a / and
      :op2 (b / bend-01
            :ARG1 (h2 / head
                  :location (o / over
                        :op1 (p / picture
                              :ARG1-of (d / draw-01)))
                  :part-of h3))
      :op2 (s / say-01
            :ARG0 (h3 / he)
            :ARG1 (l / look-01 :mode imperative
                  :ARG0 (y / you)
                  :ARG1 (s2 / small :polarity -
                        :degree (s3 / so)
                        :domain (t2 / that)))))
```
101. He has gone to sleep ... " (lpp_1943.101)

```
(s / sleep-01
      :ARG0 (h / he))
```
102. And that is how I made the acquaintance of the little prince . (lpp_1943.102)

```
(a / and
  :op2 (a2 / acquaint-01
         :ARG1 (i / i)
         :ARG2 (p / prince
                 :mod (l / little))
         :manner (t / that)))
```
103. Chapter 3 . (lpp_1943.103)

```
(c2 / chapter
  :mod 3)
```
104. It took me a long time to learn where he came from . (lpp_1943.104)

```
(t2 / take-10
      :ARG1 (t / temporal-quantity
            :ARG2-of (l / long-03
                  :ARG1 (l2 / learn-01
                        :ARG0 (i / i)
                        :ARG1 (p / place
                              :ARG3-of (c / come-01
                                    :ARG1 (h / he)))))))
```
105. The little prince , who asked me so many questions , never seemed to hear the ones I asked him . (lpp_1943.105)

```
(s / seem-01
      :ARG1 (h / hear-01 :polarity -
            :ARG0 (p / prince
                  :mod (l / little)
                  :ARG0-of (q / question-01
                        :ARG2 (i / i)
                        :quant (m / many
                              :degree (s2 / so))))
            :ARG1 (o / one
                  :ARG1-of (a2 / ask-01
                        :ARG0 i
                        :ARG2 p))
            :time (e2 / ever)))
```
106. It was from words dropped by chance that , little by little , everything was revealed to me . (lpp_1943.106)

```
(r / reveal-01
      :ARG0 (w / word
            :ARG1-of (d / drop-06
                  :ARG1-of (c / chance-02)))
      :ARG1 (e / everything)
      :ARG2 (i / i)
      :manner (l / little-by-little))
```
107. The first time he saw my airplane , for instance ( I shall not draw my airplane ; that would be much too complicated for me ) , he asked me : " What is that object ? " (lpp_1943.107)

```
(a / ask-01
      :ARG0 (h / he)
      :ARG1 (o / object
            :mod (t / that)
            :domain (a2 / amr-unknown))
      :ARG2 (i / i)
      :time (s / see-01
            :ARG0 h
            :ARG1 (a3 / airplane
                  :poss i
                  :ARG1-of (d / draw-01 :polarity -
                        :ARG0 i
                        :ARG1-of (c / cause-01
                              :ARG0 (c2 / complicate-01
                                    :ARG2 i
                                    :degree (t3 / too
                                          :degree (m / much))))))
            :ord (o2 / ordinal-entity :value 1)))
```
108. " That is not an object . (lpp_1943.108)

```
(o / object
  :domain (t / that)
  :polarity -)
```
109. It flies . (lpp_1943.109)

```
(f / fly-01
      :ARG1 (i / it))
```
110. It is an airplane . (lpp_1943.110)

```
(a / airplane
  :domain (i / it))
```
111. It is my airplane . " (lpp_1943.111)

```
(a2 / airplane
  :poss (i2 / i)
  :domain (i / it))
```
112. And I was proud to have him learn that I could fly . (lpp_1943.112)

```
(a / and
  :op2 (p / pride-01
         :ARG0 (i / i)
         :ARG2 (l / learn-01
                 :ARG0 (h2 / he)
                 :ARG1 (p2 / possible-01
                         :ARG1 (f / fly-01
                                   :ARG1 i)))))
```
113. He cried out , then : " What ! (lpp_1943.113)

```
(c / cry-out-03
      :ARG0 (h / he)
      :ARG1 (s / string-entity :value "what")
      :time (t / then))
```
114. You dropped down from the sky ? " (lpp_1943.114)

```
(d / drop-01
      :ARG1 (y / you)
      :ARG3 (s / sky)
      :direction (d2 / down)
      :mode interrogative)
```
115. " Yes , " (lpp_1943.115)

```
(y2 / yes)
```
116. I answered , modestly . (lpp_1943.116)

```
(a / answer-01
      :ARG0 (i / i)
      :manner (m / modest))
```
117. " Oh ! (lpp_1943.117)

```
(o / oh :mode expressive)
```
118. That is funny ! " (lpp_1943.118)

```
(f2 / funny
  :domain (t2 / that))
```
119. And the little prince broke into a lovely peal of laughter , which irritated me very much . (lpp_1943.119)

```
(a / and
      :op2 (b / break-in-17
            :ARG0 (p / prince
                  :mod (l / little))
            :ARG1 (l2 / laugh-01
                  :quant (p2 / peal
                        :mod (l3 / lovely)))
            :ARG0-of (i / irritate-01
                  :ARG1 (i2 / i)
                  :degree (m / much
                        :degree (v / very)))))
```
120. I like my misfortunes to be taken seriously . (lpp_1943.120)

```
(l / like-02
      :ARG0 (i / i)
      :ARG1 (t / take-04
            :ARG1 (m / misfortune
                  :poss i)
            :manner (s / serious-01)))
```
121. Then he added : " So you , too , come from the sky ! (lpp_1943.121)

```
(a / add-01
  :ARG0 (h / he)
  :ARG1 (c2 / cause-01
          :ARG1 (c / come-01
                  :ARG1 (y / you)
                  :ARG3 (s2 / sky)
                  :mod (t2 / too)))
  :time (t / then))
```
122. Which is your planet ? " (lpp_1943.122)

```
(p / planet
      :poss (y / you)
      :domain (a / amr-unknown))
```
123. At that moment I caught a gleam of light in the impenetrable mystery of his presence ; and I demanded , abruptly : " Do you come from another planet ? " (lpp_1943.123)

```
(a / and
      :op1 (c / catch-03
            :ARG0 (i / i)
            :ARG1 (g / gleam
                  :consist-of (l / light)
                  :location (m / mystery
                        :domain (p / present-02
                              :ARG1 (h / he))
                        :ARG1-of (p3 / penetrate-01
                              :ARG1-of (p2 / possible-01 :polarity -))))
            :time (m2 / moment
                  :mod (t / that)))
      :op2 (d / demand-01
            :ARG0 i
            :ARG1 (c2 / come-01 :mode interrogative
                  :ARG1 (y / you)
                  :ARG3 (p4 / planet
                        :mod (a3 / another)))
            :manner (a2 / abrupt)))
```
124. But he did not reply . (lpp_1943.124)

```
(c / contrast-01
  :ARG2 (r / reply-01
          :ARG0 (h / he)
          :polarity -))
```
125. He tossed his head gently , without taking his eyes from my plane : " It is true that on that you can n't have come from very far away ... " (lpp_1943.125)

```
(a / and
      :op1 (t / toss-01
            :ARG0 (h / he)
            :ARG1 (h2 / head
                  :part-of h)
            :manner (g / gentle)
            :manner (t2 / take-away-05 :polarity -
                  :ARG0 h
                  :ARG1 (e / eye
                        :part-of h)
                  :direction (p2 / plane
                        :poss (i / i))))
      :op2 (s / say-01
            :ARG0 h
            :ARG1 (p / possible-01 :polarity -
                  :ARG1 (c / come-01
                        :ARG1 (y / you)
                        :ARG3 (a2 / away
                              :extent (f / far
                                    :degree (v / very)))
                        :manner p2))))
```
126. And he sank into a reverie , which lasted a long time . (lpp_1943.126)

```
(a / and
      :op2 (s / sink-01
            :ARG0 (h / he)
            :ARG4 (r / reverie
                  :ARG1-of (l / long-03))))
```
127. Then , taking my sheep out of his pocket , he buried himself in the contemplation of his treasure . (lpp_1943.127)

```
(b / bury-01
  :ARG0 (h / he)
  :ARG1 h
  :ARG2 (c / contemplate-01
          :ARG0 h
          :ARG1 (t / treasure
                  :poss h))
  :time (t2 / take-out-11
          :ARG0 h
          :ARG1 (s / sheep
                  :source (p / pocket
                            :poss h)
                  :poss (i / i)))
  :time (t3 / then))
```
128. You can imagine how my curiosity was aroused by this half - confidence about the " other planets . " (lpp_1943.128)

```
(p / possible-01
      :ARG1 (i2 / imagine-01
            :ARG0 (y / you)
            :ARG1 (a / arouse-01
                  :ARG0 (c4 / confidence
                        :degree (h2 / half)
                        :topic (p3 / planet
                              :mod (o2 / other))
                        :poss (h / he))
                  :ARG1 (c / curious-01
                        :ARG1 (i / i)))))
```
129. I made a great effort , therefore , to find out more on this subject . (lpp_1943.129)

```
(c / cause-01
      :ARG1 (e / effort-01
            :ARG0 (i / i)
            :ARG1 (f / find-out-03
                  :ARG0 i
                  :ARG1 (i2 / information
                        :quant (m2 / more)
                        :topic (s / subject
                              :mod (t2 / this))))
            :mod (g / great)))
```
130. " My little man , where do you come from ? (lpp_1943.130)

```
(s / say-01
      :ARG1 (c / come-01
            :ARG1 (y / you)
            :ARG3 (a / amr-unknown))
      :ARG2 (m / man
            :mod (l / little)
            :poss (i / i)))
```
131. What is this ' where I live , ' of which you speak ? (lpp_1943.131)

```
(l / live-01
      :ARG0 (y / you)
      :location (p / place
            :ARG1-of (s / speak-01
                  :ARG0 y)
            :domain (a / amr-unknown)))
```
132. Where do you want to take your sheep ? " (lpp_1943.132)

```
(w / want-01
      :ARG0 (y / you)
      :ARG1 (t / take-01
            :ARG0 y
            :ARG1 (s / sheep
                  :poss y)
            :ARG3 (a / amr-unknown)))
```
133. After a reflective silence he answered : " The thing that is so good about the box you have given me is that at night he can use it as his house . " (lpp_1943.133)

```
(a / answer-01
      :ARG0 (h / he)
      :ARG1 (t / thing
            :ARG1-of (g / good-02
                  :degree (s2 / so))
            :topic (b / box
                  :ARG1-of (g2 / give-01
                        :ARG0 (y / you)
                        :ARG2 h))
            :domain (p / possible-01
                  :ARG1 (u / use-01
                        :ARG0 (h2 / he)
                        :ARG1 b
                        :ARG2 (h3 / house
                              :poss h2)
                        :time (d / date-entity :dayperiod (n / night)))))
      :time (a2 / after
            :op1 (s / silent
                  :mod (r / reflect-02))))
```
134. " That is so . (lpp_1943.134)

```
(s / so
  :domain (t / that))
```
135. And if you are good I will give you a string , too , so that you can tie him during the day , and a post to tie him to . " (lpp_1943.135)

```
(a / and
      :op2 (g / give-01
            :ARG0 (i / i)
            :ARG1 (a2 / and
                  :op1 (s / string
                        :ARG3-of (t / tie-01
                              :ARG0 y
                              :ARG1 (h / he)
                              :time (d / date-entity
                                    :dayperiod (d2 / day))))
                  :op2 (p2 / post
                        :purpose (t3 / tie-01
                              :ARG0 y
                              :ARG1 h)))
            :ARG2 (y / you)
            :condition (g2 / good-02
                  :ARG1 y)))
```
136. But the little prince seemed shocked by this offer : " Tie him ! (lpp_1943.136)

```
(c / contrast-01
      :ARG2 (s / seem-01
            :ARG1 (s2 / shock-01
                  :ARG0 (o / offer
                        :mod (t / this))
                  :ARG1 (p / prince
                        :mod (l / little)
                        :ARG0-of (s3 / say-01
                              :ARG1 (t2 / tie-01 :mode imperative
                                    :ARG0 p
                                    :ARG1 (h / he)))))))
```
137. What a queer idea ! " (lpp_1943.137)

```
(q / queer
      :domain (i / idea))
```
138. " But if you do n't tie him , " (lpp_1943.138)

```
(c / contrast-01
      :ARG2 (t / tie-01 :polarity -
            :ARG0 (y / you)
            :ARG1 (h / he)
            :condition-of (t2 / thing)))
```
139. I said , " he will wander off somewhere , and get lost . " (lpp_1943.139)

```
(s / say-01
  :ARG0 (i / i)
  :ARG1 (a / and
          :op1 (w / wander-01
                 :ARG0 (h / he)
                 :ARG1 (s2 / somewhere))
          :op2 (g / get-03
                 :ARG1 h
                 :ARG2 (l / lost))))
```
140. My friend broke into another peal of laughter : " But where do you think he would go ? " (lpp_1943.140)

```
(b / break-in-17
      :ARG0 (p2 / person
            :ARG0-of (h2 / have-rel-role-91
                  :ARG1 (i / i)
                  :ARG2 (f / friend))
            :ARG0-of (s / say-01
                  :ARG1 (c / contrast-01
                        :ARG2 (t / think-01
                              :ARG0 (y / you)
                              :ARG1 (g / go-02
                                    :ARG0 (h / he)
                                    :ARG4 (a2 / amr-unknown))))))
      :ARG1 (l / laugh-01
            :quant (p / peal
                  :mod (a / another))))
```
141. " Anywhere . (lpp_1943.141)

```
(a / anywhere)
```
142. Straight ahead of him . " (lpp_1943.142)

```
(a / ahead
      :ARG1-of (s / straight-04)
      :compared-to (h / he))
```
143. Then the little prince said , earnestly : " That does n't matter . (lpp_1943.143)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (m / matter-01 :polarity -
            :ARG1 (t2 / that))
      :manner (e / earnest-01)
      :time (t / then))
```
144. Where I live , everything is so small ! " (lpp_1943.144)

```
(s / small
      :degree (s2 / so)
      :domain (e / everything
            :location (l / live-01
                  :ARG0 (i / i))))
```
145. And , with perhaps a hint of sadness , he added : " Straight ahead of him , nobody can go very far ... " (lpp_1943.145)

```
(a / and
      :op2 (a2 / add-01
            :ARG0 (h / he)
            :ARG1 (g / go-02
                  :ARG0 (s2 / somebody :polarity -)
                  :ARG4 (f / far
                        :degree (v / very))
                  :direction (a3 / ahead
                        :ARG1-of (s3 / straight-04)
                        :compared-to s2))
            :manner (s / sad-02
                  :quant (h2 / hint)
                  :ARG1-of (p / possible-01))))
```
146. Chapter 4 . (lpp_1943.146)

```
(c / chapter
  :mod 4)
```
147. I had thus learned a second fact of great importance : this was that the planet the little prince came from was scarcely any larger than a house ! (lpp_1943.147)

```
(c2 / cause-01
      :ARG1 (l / learn-01
            :ARG0 (i / i)
            :ARG1 (f / fact
                  :ord (o / ordinal-entity :value 2)
                  :mod (i2 / important
                        :degree (g / great))
                  :domain (l2 / large
                        :degree (m / more
                              :mod (a / any
                                    :degree (s2 / scarce)))
                        :compared-to (h / house)
                        :domain (p / planet
                              :ARG3-of (c / come-01
                                    :ARG1 (p2 / prince
                                          :mod (l3 / little))))))))
```
148. But that did not really surprise me much . (lpp_1943.148)

```
(c / contrast-01
      :ARG2 (s / surprise-01 :polarity -
            :ARG0 (t / that)
            :ARG1 (i / i)
            :degree (m / much)
            :ARG1-of (r / real-04)))
```
149. I knew very well that in addition to the great planets -- such as the Earth , Jupiter , Mars , Venus -- to which we have given names , there are also hundreds of others , some of which are so small that one has a hard time seeing them through the telescope . (lpp_1943.149)

```
(k / know-01
      :ARG0 (i / i)
      :ARG1 (e / exist-01
            :ARG1 (a2 / and
                  :op1 (p / planet
                        :mod (g / great)
                        :example (p2 / planet :wiki "Earth" :name (n / name :op1 "Earth"))
                        :example (p3 / planet :wiki "Jupiter" :name (n2 / name :op1 "Jupiter"))
                        :example (p4 / planet :wiki "Mars" :name (n3 / name :op1 "Mars"))
                        :example (p5 / planet :wiki "Venus" :name (n4 / name :op1 "Venus"))
                        :ARG1-of (n5 / name-01
                              :ARG0 (w3 / we)))
                  :op2 (p7 / planet
                        :ARG2-of (i2 / include-91
                              :ARG1 (p6 / planet
                                    :mod (s2 / small
                                          :degree (s3 / so)
                                          :ARG0-of (c / cause-01
                                                :ARG1 (d / difficult
                                                      :domain (s4 / see-01
                                                            :ARG1 p6
                                                            :instrument (t / telescope)))))))
                        :mod (o / other)
                        :quant (m / multiple :op1 100)
                        :mod (a / also))))
      :mod (w / well
            :degree (v / very)))
```
150. When an astronomer discovers one of these he does not give it a name , but only a number . (lpp_1943.150)

```
(g / give-01
      :ARG0 (a / astronomer)
      :ARG1 (n2 / number)
      :ARG2 (t / thing :quant 1
            :ARG1-of (i / include-91
                  :ARG2 (t2 / this)))
      :mod (o2 / only)
      :time (d / discover-01
            :ARG0 a
            :ARG1 t)
      :ARG1-of (i2 / instead-of-91
            :ARG2 (n3 / name-01
                  :ARG0 a
                  :ARG1 t)))
```
151. He might call it , for example , " Asteroid 325 . " (lpp_1943.151)

```
(p / possible-01
      :ARG1 (c / call-01
            :ARG0 (h / he)
            :ARG1 (i / it)
            :ARG2 (n2 / name :op1 "Asteroid" :op2 325)
            :ARG0-of (e / exemplify-01)))
```
152. I have serious reason to believe that the planet from which the little prince came is the asteroid known as B-612 . (lpp_1943.152)

```
(c / cause-01
      :ARG0 (r / reason
            :ARG1-of (s / serious-02))
      :ARG1 (b / believe-01
            :ARG0 (i / i)
            :ARG1 (c2 / come-01
                  :ARG1 (p2 / prince
                        :mod (l / little))
                  :ARG3 (a / asteroid :wiki - :name (n4 / name :op1 "B-612")
                        :domain (p / planet)))))
```
153. This asteroid has only once been seen through the telescope . (lpp_1943.153)

```
(s / see-01
      :ARG1 (a / asteroid
            :mod (t / this))
      :instrument (t2 / telescope)
      :ARG1-of (h / have-frequency-91
            :ARG2 1
            :mod (o / only)))
```
154. That was by a Turkish astronomer , in 1909 . (lpp_1943.154)

```
(s / see-01
      :ARG0 (a / astronomer
            :mod (c / country :wiki "Turkey"
                  :name (n / name :op1 "Turkey")))
      :time (d / date-entity :year 1909))
```
155. On making his discovery , the astronomer had presented it to the International Astronomical Congress , in a great demonstration . (lpp_1943.155)

```
(p / present-01
      :ARG0 a
      :ARG1 (i / it)
      :ARG2 (o / organization :wiki "International_Astronautical_Congress" :name (n / name :op1 "International" :op2 "Astronomical" :op3 "Congress"))
      :manner (d2 / demonstrate-01
            :ARG0 a
            :mod (g / great))
      :time (d3 / discover-01
            :ARG0 (a / astronomer)))
```
156. But he was in Turkish costume , and so nobody would believe what he said . (lpp_1943.156)

```
(c4 / contrast-01
      :ARG2 (c / costume-01
            :ARG1 (h / he)
            :manner (c2 / country :wiki "Turkey"
                  :name (n / name :op1 "Turkey"))
            :ARG0-of (c3 / cause-01
                  :ARG1 (b2 / believe-01
                        :ARG0 (s / somebody :polarity -)
                        :ARG1 (t / thing
                              :ARG1-of (s2 / say-01
                                    :ARG0 h))))))
```
157. Grown - ups are like that ... (lpp_1943.157)

```
(r / resemble-01
      :ARG1 (g / grown-up)
      :ARG2 (t / that))
```
158. Fortunately , however , for the reputation of Asteroid B-612 , a Turkish dictator made a law that his subjects , under pain of death , should change to European costume . (lpp_1943.158)

```
(c5 / contrast-01
      :ARG2 (m / make-01
            :ARG0 (p3 / person
                  :ARG0-of (h / have-org-role-91
                        :ARG1 (c / country :wiki "Turkey" :name (n / name :op1 "Turkey"))
                        :ARG2 (d / dictator)))
            :ARG1 (l / law
                  :topic (c2 / change-01
                        :ARG0 (s / subject
                              :poss p3)
                        :ARG3 (c3 / costume
                              :mod (c4 / continent :wiki "Europe" :name (n2 / name :op1 "Europe")))
                        :manner (t / threaten-01
                              :ARG0 d
                              :ARG1 (p / penalize-01
                                    :ARG1 s
                                    :topic (d2 / die-01
                                          :ARG1 s))
                              :ARG2 s)))
            :ARG2-of (f / fortunate-01
                  :ARG1 (r / reputation
                        :poss (p2 / planet :wiki - :name (n3 / name :op1 "Asteroid" :op2 "B-612"))))))
```
159. So in 1920 the astronomer gave his demonstration all over again , dressed with impressive style and elegance . (lpp_1943.159)

```
(c / cause-01
      :ARG1 (d4 / demonstrate-01
            :ARG0 (a / astronomer
                  :ARG1-of (d2 / dress-01
                        :ARG2 (a4 / and
                              :op1 (s / style)
                              :op2 (e / elegance)
                              :ARG0-of (i / impress-01))))
            :time (d3 / date-entity :year 1920)
            :mod (a3 / again
                  :mod (a2 / all-over))))
```
160. And this time everybody accepted his report . (lpp_1943.160)

```
(a / and
  :op2 (a2 / accept-01
         :ARG0 (e / everybody)
         :ARG1 (t3 / thing
                 :ARG1-of (r / report-01
                            :ARG0 (h2 / he)))
         :time (t / time
                 :mod (t2 / this))))
```
161. If I have told you these details about the asteroid , and made a note of its number for you , it is on account of the grown - ups and their ways . (lpp_1943.161)

```
(a / account-01
  :ARG1 a3
  :ARG2 (a2 / and
          :op1 (g / grown-up)
          :op2 (w / way
                 :poss g))
  :condition (a3 / and
               :op1 (t / tell-01
                      :ARG0 (i / i)
                      :ARG1 (d / detail
                              :mod (t2 / this)
                              :topic (a4 / asteroid))
                      :ARG2 (y / you))
               :op2 (n3 / note-01
                      :ARG0 i
                      :ARG1 (n4 / number
                              :poss a4)
                      :ARG2 y)))
```
162. WHen you tell them that you have made a new friend , they never ask you any questions about essential matters . (lpp_1943.162)

```
(q2 / question-01 :polarity -
      :ARG0 (t2 / they)
      :ARG1 (m / matter
            :mod (e / essential))
      :ARG2 (y / you)
      :time (t3 / tell-01
            :ARG0 y
            :ARG1 (m2 / make-01
                  :ARG0 y
                  :ARG1 (h / have-rel-role-91
                        :ARG0 (p / person)
                        :ARG1 y
                        :ARG2 (f / friend)
                        :ARG1-of (n / new-01)))
            :ARG2 (t / they))
      :time (e2 / ever)
      :mod (a2 / any))
```
163. They never say to you , " What does his voice sound like ? (lpp_1943.163)

```
(s / say-01
  :ARG0 (t / they)
  :ARG1 (s2 / sound-01
          :ARG1 (v / voice
                  :poss (h / he))
          :ARG2 (a2 / amr-unknown))
  :ARG2 (y / you)
  :time (e / ever)
  :polarity -)
```
164. What games does he love best ? (lpp_1943.164)

```
(l / love-01
      :ARG0 (h / he)
      :ARG1 (a2 / amr-unknown
            :domain (g2 / game))
      :degree (g / good
            :degree (m / most)))
```
165. Does he collect butterflies ? " (lpp_1943.165)

```
(c / collect-01
      :ARG0 (h / he)
      :ARG1 (b / butterfly)
      :mode interrogative)
```
166. Instead , they demand : " How old is he ? (lpp_1943.166)

```
(d / demand-01
      :ARG0 (t / they)
      :ARG1 (a2 / age-01
            :ARG1 (h2 / he)
            :ARG2 (a3 / amr-unknown))
      :ARG1-of (i2 / instead-of-91))
```
167. How many brothers has he ? (lpp_1943.167)

```
(h / have-rel-role-91
      :ARG0 (p / person
            :quant (a / amr-unknown))
      :ARG1 (h2 / he)
      :ARG2 (b / brother))
```
168. How much does he weigh ? (lpp_1943.168)

```
(w / weigh-01
      :ARG1 (h / he)
      :ARG3 (a / amr-unknown))
```
169. How much money does his father make ? " (lpp_1943.169)

```
(m / make-05
      :ARG0 (p / person
            :ARG0-of (h2 / have-rel-role-91
                  :ARG1 (h / he)
                  :ARG2 (f / father)))
      :ARG1 (m2 / monetary-quantity
            :quant (a / amr-unknown)))
```
170. Only from these figures do they think they have learned anything about him . (lpp_1943.170)

```
(t / think-01
      :ARG0 (t2 / they)
      :ARG1 (l / learn-01
            :ARG0 t2
            :ARG1 (a / anything
                  :topic (h / he))
            :source (f / figure
                  :mod (t3 / this
                        :mod (o / only)))))
```
171. If you were to say to the grown - ups : " I saw a beautiful house made of rosy brick , with geraniums in the windows and doves on the roof , " they would not be able to get any idea of that house at all . (lpp_1943.171)

```
(p / possible-01 :polarity -
      :ARG1 (g / get-01
            :ARG0 g2
            :ARG1 (i / idea
                  :mod (a / any)
                  :mod (a2 / at
                        :mod (a3 / all))
                  :topic h2))
      :condition (s / say-01
            :ARG0 (y / you)
            :ARG1 (s2 / see-01
                  :ARG0 y
                  :ARG1 (h2 / house
                        :ARG1-of (m / make-01
                              :ARG2 (b / brick
                                    :mod (r / rosy)))
                        :accompanier (a4 / and
                              :op1 (g3 / geranium
                                    :location (w / window))
                              :op2 (d / dove
                                    :location (r2 / roof)))
                        :ARG1-of (b2 / beautiful-02)))
            :ARG2 (g2 / grown-up)))
```
172. You would have to say to them : " I saw a house that cost $ 20,000 . " (lpp_1943.172)

```
(o / obligate-01
  :ARG1 y
  :ARG2 (s / say-01
          :ARG0 (y / you)
          :ARG1 (s2 / see-01
                  :ARG0 y
                  :ARG1 (h / house
                          :ARG1-of (c / cost-01
                                     :ARG2 (m / monetary-quantity
                                             :unit (d / dollar)
                                             :quant 20000))))
          :ARG2 (t / they)))
```
173. Then they would exclaim : " Oh , what a pretty house that is ! " (lpp_1943.173)

```
(e / exclaim-01
  :ARG0 (t / they)
  :ARG1 (p2 / pretty
          :domain (h2 / house
                    :mod (t4 / that)))
  :time (t3 / then))
```
174. Just so , you might say to them : " The proof that the little prince existed is that he was charming , that he laughed , and that he was looking for a sheep . (lpp_1943.174)

```
(p / possible-01
      :ARG1 (s2 / say-01
            :ARG0 (y / you)
            :ARG1 (p2 / prove-01
                  :ARG0 (a / and
                        :op1 (c / charming
                              :domain (h / he))
                        :op2 (l / laugh-01
                              :ARG0 h)
                        :op3 (l2 / look-01
                              :ARG0 h
                              :ARG1 (s3 / sheep)))
                  :ARG1 (e / exist-01
                        :ARG1 (p3 / prince
                              :mod (l3 / little))))
            :ARG2 (t / they)
            :manner (j / just-so)))
```
175. If anybody wants a sheep , that is a proof that he exists . " (lpp_1943.175)

```
(p / prove-01
  :ARG0 (w / want-01
          :ARG0 (a / anybody)
          :ARG1 (s / sheep))
  :ARG1 (e / exist-01
          :ARG1 a))
```
176. And what good would it do to tell them that ? (lpp_1943.176)

```
(a / and
      :op2 (d / do-02
            :ARG0 (t / tell-01
                  :ARG1 (t3 / that)
                  :ARG2 (t2 / they))
            :ARG1 (g / good-04
                  :ARG2 t2
                  :quant (a2 / amr-unknown))))
```
177. They would shrug their shoulders , and treat you like a child . (lpp_1943.177)

```
(a / and
      :op1 (s / shrug-01
            :ARG0 (t / they)
            :ARG1 (s2 / shoulder
                  :poss t))
      :op2 (t2 / treat-01
            :ARG0 t
            :ARG1 (y / you)
            :ARG2 (c / child)))
```
178. But if you said to them : " The planet he came from is Asteroid B-612 , " then they would be convinced , and leave you in peace from their questions . (lpp_1943.178)

```
(c3 / contrast-01
      :ARG2 (a / and
            :op1 (c / convince-01
                  :ARG1 (t / they))
            :op2 (l / leave-14
                  :ARG0 t
                  :ARG1 (p2 / peace
                        :topic (q2 / question-01 :polarity -
                              :ARG0 t)
                        :domain y))
            :condition (s / say-01
                  :ARG0 (y / you)
                  :ARG1 (c2 / come-01
                        :ARG1 (h / he)
                        :ARG3 (p / planet :wiki - :name (n / name :op1 "Asteroid" :op2 "B-612")))
                  :ARG2 t)))
```
179. They are like that . (lpp_1943.179)

```
(r / resemble-01
      :ARG1 (t / they)
      :ARG2 (t2 / that))
```
180. One must not hold it against them . (lpp_1943.180)

```
(o / obligate-01
      :ARG1 (o2 / one)
      :ARG2 (h / hold-01 :polarity -
            :ARG0 o2
            :ARG1 (i / it)
            :ARG2 (a / against
                  :op1 (t / they))))
```
181. Children should always show great forbearance toward grown - up people . (lpp_1943.181)

```
(r / recommend-01
      :ARG1 (s / show-01
            :ARG0 (c / child)
            :ARG1 (f / forbearance
                  :mod (g / great))
            :ARG2 (g2 / grown-up)
            :time (a / always)))
```
182. But certainly , for us who understand life , figures are a matter of indifference . (lpp_1943.182)

```
(c2 / contrast-01
  :ARG2 (c / certain
          :domain (i2 / indifferent-01
                    :ARG1 (w2 / we
                            :ARG0-of (u / understand-01
                                       :ARG1 (l / life)))
                    :ARG2 (f2 / figure))))
```
183. I should have liked to begin this story in the fashion of the fairy - tales . (lpp_1943.183)

```
(l / like-02
  :ARG0 (i / i)
  :ARG1 (b / begin-01
          :ARG0 i
          :ARG1 (s / story
                  :mod (t / this))
          :manner (f / fashion
                    :mod (t2 / tale
                           :mod (f2 / fairy)))))
```
184. I should have like to say : " Once upon a time there was a little prince who lived on a planet that was scarcely any bigger than himself , and who had need of a sheep ... " (lpp_1943.184)

```
(l / like-02
      :ARG0 (i / i)
      :ARG1 (s / say-01
            :ARG0 i
            :ARG1 (p / prince
                  :mod (l2 / little)
                  :ARG0-of (l3 / live-01
                        :location (p2 / planet
                              :mod (b / big
                                    :degree (m / more
                                          :quant (s2 / scarce))
                                    :compared-to p)))
                  :ARG0-of (n / need-01
                        :ARG1 (s3 / sheep))
                  :time (o / once-upon-a-time))))
```
185. To those who understand life , that would have given a much greater air of truth to my story . (lpp_1943.185)

```
(g / give-01
  :ARG0 (t / that)
  :ARG1 (t3 / truth
          :quant (a / air
                   :mod (g2 / great
                          :degree (m / more
                                    :degree (m2 / much)))))
  :ARG2 (s / story
          :poss (i / i))
  :beneficiary (p / person
                 :ARG0-of (u / understand-01
                            :ARG1 (l / life))))
```
186. For I do not want any one to read my book carelessly . (lpp_1943.186)

```
(c / cause-01
      :ARG0 (w / want-01
            :ARG0 (i / i)
            :ARG1 (r / read-01
                  :ARG0 (a / anyone)
                  :ARG1 (b / book
                        :poss i)
                  :manner (c2 / careless))
            :polarity -))
```
187. I have suffered too much grief in setting down these memories . (lpp_1943.187)

```
(s / suffer-01
      :ARG0 (i / i)
      :ARG1 (g / grief
            :quant (m / much
                  :degree (t / too)))
      :time (s2 / set-down-09
            :ARG0 i
            :ARG1 (m2 / memory
                  :mod (t2 / this))))
```
188. Six years have already passed since my friend went away from me , with his sheep . (lpp_1943.188)

```
(g / go-02
      :ARG0 (p / person
            :ARG0-of (h / have-rel-role-91
                  :ARG1 (i / i)
                  :ARG2 (f / friend)))
      :direction (a / away
            :op1 i)
      :accompanier (s / sheep
            :poss p)
      :time (b / before
            :op1 (n / now)
            :quant (t / temporal-quantity :quant 6
                  :unit (y / year)))
      :time (a3 / already))
```
189. If I try to describe him here , it is to make sure that I shall not forget him . (lpp_1943.189)

```
(e / ensure-01
  :ARG1 (f / forget-01
          :ARG0 i
          :ARG1 (h3 / he)
          :polarity -)
  :condition (t / try-01
               :ARG0 (i / i)
               :ARG1 (d / describe-01
                       :ARG0 i
                       :ARG1 (h / he)
                       :location (h2 / here))))
```
190. To forget a friend is sad . (lpp_1943.190)

```
(s / sad-02
      :ARG0 (f3 / forget-01
            :ARG1 (p / person
                  :ARG0-of (h / have-rel-role-91
                        :ARG2 (f / friend)))))
```
191. Not every one has had a friend . (lpp_1943.191)

```
(h / have-03 :polarity -
      :ARG0 (e / everyone)
      :ARG1 (p / person
            :ARG0-of (h2 / have-rel-role-91
                  :ARG1 e
                  :ARG2 (f / friend))))
```
192. And if I forget him , I may become like the grown - ups who are no longer interested in anything but figures ... (lpp_1943.192)

```
(a / and
      :op2 (p / possible-01
            :ARG1 (r / resemble-01
                  :ARG1 (i / i)
                  :ARG2 (g / grown-up
                        :ARG1-of (i2 / interest-01 :polarity -
                              :ARG2 (a2 / anything
                                    :ARG2-of (e / except-01
                                          :ARG1 (f / figure))))))
            :condition (f2 / forget-01
                  :ARG0 i
                  :ARG1 (h / he))))
```
193. It is for that purpose , again , that I have bought a box of paints and some pencils . (lpp_1943.193)

```
(b / buy-01
  :ARG0 (i / i)
  :ARG1 (a / and
          :op1 (p / paint
                 :location (b2 / box))
          :op2 (p2 / pencil
                 :quant (s / some)))
  :purpose (t2 / that))
```
194. It is hard to take up drawing again at my age , when I have never made any pictures except those of the boa constrictor from the outside and the boa constrictor from the inside , since I was six . (lpp_1943.194)

```
(h / hard-02
      :ARG1 (t / take-up-31
            :ARG0 (i / i
                  :age (t4 / temporal-quantity
                        :duration-of (m / make-01 :polarity -
                              :ARG1 (p / picture
                                    :mod (a5 / any)
                                    :ARG2-of (e2 / except-01
                                          :ARG1 (a6 / and
                                                :op1 (p2 / picture
                                                      :topic (b / boa
                                                            :mod (c2 / constrictor)
                                                            :direction (f / from
                                                                  :op1 (o / outside))))
                                                :op2 (p3 / picture
                                                      :topic (b2 / boa
                                                            :mod (c3 / constrictor)
                                                            :direction (f2 / from
                                                                  :op1 (i2 / inside)))))))
                              :time (e / ever)
                              :time (s / since
                                    :op1 (a3 / age-01
                                          :ARG1 i
                                          :ARG2 (t6 / temporal-quantity :quant 6
                                                :unit (y2 / year)))))))
            :ARG1 (d / draw-01)
            :mod (a / again))
      :ARG1-of (c / cause-01))
```
195. I shall certainly try to make my portraits as true to life as possible . (lpp_1943.195)

```
(t / try-01
      :ARG0 (i / i)
      :ARG1 (m / make-02
            :ARG0 i
            :ARG1 (t2 / true-02
                  :ARG1 (p / portrait
                        :topic i)
                  :ARG2 (l / life)
                  :degree (m2 / most)
                  :compared-to (p2 / possible-01)))
      :mod (c / certain))
```
196. But I am not at all sure of success . (lpp_1943.196)

```
(c / contrast-01
      :ARG2 (s / sure-02 :polarity -
            :ARG0 (i / i)
            :degree (a / at
                  :op1 (a2 / all))
            :ARG1-of (s2 / succeed-01
                  :ARG0 i)))
```
197. One drawing goes along all right , and another has no resemblance to its subject . (lpp_1943.197)

```
(a / and
      :op1 (g / go-06
            :ARG1 (p2 / picture :quant 1
                  :ARG1-of (d / draw-01))
            :ARG2 (a2 / along)
            :mod (a3 / all-right))
      :op2 (r2 / resemble-01 :polarity -
            :ARG1 (p / picture
                  :ARG1-of (d2 / draw-01)
                  :mod (a4 / another))
            :ARG2 (s / subject
                  :poss p)))
```
198. I make some errors , too , in the little prince 's height : in one place he is too tall and in another too short . (lpp_1943.198)

```
(e / err-01
      :ARG0 (i / i)
      :topic (h / high-02
            :ARG1 (p / prince
                  :mod (l / little)))
      :mod (t / too)
      :example (a / and
            :op1 (t2 / tall
                  :domain p
                  :degree (t3 / too)
                  :location (p2 / place
                        :mod (o / one)))
            :op2 (s / short-07
                  :ARG1 p
                  :degree (t4 / too)
                  :location (p3 / place
                        :mod (a2 / another))))
      :mod (s2 / some))
```
199. And I feel some doubts about the color of his costume . (lpp_1943.199)

```
(a / and
  :op2 (f / feel-01
         :ARG0 (i / i)
         :ARG1 (d / doubt-01
                 :ARG0 i
                 :ARG1 (c / color
                         :poss (c2 / costume
                                 :poss (h / he)))
                 :quant (s / some))))
```
200. So I fumble along as best I can , now good , now bad , and I hope generally fair - to - middling . (lpp_1943.200)

```
(c / cause-01
      :ARG1 (f / fumble-01
            :ARG0 (i / i)
            :ARG1 (a / along)
            :manner (g / good-03
                  :degree (m / most)
                  :example (g2 / good-03
                        :time (n / now))
                  :example (b / bad-02
                        :time (n2 / now))
                  :example (f2 / fair-04
                        :ARG1-of (g3 / general-02)
                        :ARG1-of (h / hope-01
                              :ARG0 i)
                        :prep-to (m2 / middling))
                  :compared-to (p / possible-01))))
```
201. In certain more important details I shall make mistakes , also . (lpp_1943.201)

```
(m2 / mistake-02
      :ARG0 (i / i)
      :ARG1 (d / detail
            :mod (i2 / important
                  :degree (m3 / more))
            :mod (c / certain))
      :mod (a / also))
```
202. But that is something that will not be my fault . (lpp_1943.202)

```
(c / contrast-01
  :ARG2 (f2 / fault-01
          :ARG1 (i / i)
          :ARG2 (s2 / something
                  :mod (t2 / that))
          :polarity -))
```
203. My friend never explained anything to me . (lpp_1943.203)

```
(e / explain-01 :polarity -
      :ARG0 (p / person
            :ARG0-of (h / have-rel-role-91
                  :ARG1 i
                  :ARG2 (f / friend)))
      :ARG1 (a / anything)
      :ARG2 (i / i)
      :time (e2 / ever))
```
204. He thought , perhaps , that I was like himself . (lpp_1943.204)

```
(t / think-01
      :ARG0 (h / he)
      :ARG1 (r / resemble-01
            :ARG1 (i / i)
            :ARG2 h)
      :mod (p / perhaps))
```
205. But I , alas , do not know how to see sheep through the walls of boxes . (lpp_1943.205)

```
(c / contrast-01
      :ARG2 (k / know-01 :polarity -
            :ARG0 (i / i)
            :ARG1 (t2 / thing
                  :manner-of (s / see-01
                        :ARG1 (s2 / sheep)
                        :path (t / through
                              :op1 (w / wall
                                    :consist-of (b2 / box))))))
      :mod (a / alas))
```
206. Perhaps I am a little like the grown - ups . (lpp_1943.206)

```
(r / resemble-01
      :ARG1 (i / i)
      :ARG2 (g / grown-up)
      :mod (p / perhaps)
      :quant (l / little))
```
207. I have had to grow old . (lpp_1943.207)

```
(o / obligate-01
  :ARG1 (i / i)
  :ARG2 (g / grow-02
          :ARG1 i
          :ARG2 (o2 / old)))
```
208. Chapter 5 . (lpp_1943.208)

```
(c / chapter :mod 5)
```
209. As each day passed I would learn , in our talk , something about the little prince 's planet , his departure from it , his journey . (lpp_1943.209)

```
(l / learn-01
      :ARG0 (i / i)
      :ARG1 (a / and
            :op1 (s / something
                  :topic (p2 / planet
                        :poss (p3 / prince
                              :mod (l2 / little))))
            :op2 (d2 / depart-01
                  :ARG0 p3
                  :ARG1 p2)
            :op3 (j / journey-01
                  :ARG0 p3))
      :time (p / pass-03
            :ARG1 (d / day
                  :mod (e / each)))
      :source (t / talk-01
            :ARG0 (w / we)))
```
210. The information would come very slowly , as it might chance to fall from his thoughts . (lpp_1943.210)

```
(c / come-01
      :ARG1 (i / information)
      :ARG1-of (s / slow-05
            :degree (v / very))
      :time (f / fall-01
            :ARG1 i
            :ARG3 (t / thing
                  :ARG1-of (t2 / think-01
                        :ARG0 (h / he)))
            :ARG1-of (c2 / chance-01)))
```
211. It was in this way that I heard , on the third day , about the catastrophe of the baobabs . (lpp_1943.211)

```
(h / hear-01
      :ARG0 (i / i)
      :ARG1 (c / catastrophe
            :poss (b / baobab))
      :manner (t / this)
      :time (d / day
            :ord (o / ordinal-entity :value 3)))
```
212. This time , once more , I had the sheep to thank for it . (lpp_1943.212)

```
(o / obligate-01
      :ARG2 (t / thank-01
            :ARG0 (i / i)
            :ARG1 (s / sheep)
            :ARG2 (i2 / it))
      :time (t2 / time
            :mod (t3 / this))
      :mod (a / again :frequency 1))
```
213. For the little prince asked me abruptly -- as if seized by a grave doubt -- " It is true , is n't it , that sheep eat little bushes ? " (lpp_1943.213)

```
(a / ask-01
      :ARG0 (p / prince
            :mod (l2 / little))
      :ARG1 (t / true-01
            :ARG1 (e / eat-01
                  :ARG0 (s / sheep)
                  :ARG1 (b / bush
                        :mod (l / little)))
            :ARG1-of (r / request-confirmation-91
                  :ARG0 p
                  :ARG2 i2))
      :ARG2 (i2 / i)
      :manner (a2 / abrupt)
      :conj-as-if (s2 / seize-01
            :ARG0 (d / doubt-01
                  :ARG0 p
                  :mod (g / grave))
            :ARG1 p))
```
214. " Yes , that is true . " (lpp_1943.214)

```
(t / true-01
      :ARG1 (t2 / that))
```
215. " Ah ! (lpp_1943.215)

```
(a / ah :mode expressive)
```
216. I am glad ! " (lpp_1943.216)

```
(g / glad-02
      :ARG1 (i / i))
```
217. I did not understand why it was so important that sheep should eat little bushes . (lpp_1943.217)

```
(u / understand-01 :polarity -
      :ARG0 (i / i)
      :ARG1 (i2 / important
            :mod (s2 / so)
            :domain (r / recommend-01
                  :ARG1 (e / eat-01
                        :ARG0 (s / sheep)
                        :ARG1 (b / bush
                              :mod (l / little))))
            :ARG1-of (c / cause-01
                  :ARG0 (a / amr-unknown))))
```
218. But the little prince added : " Then it follows that they also eat baobabs ? " (lpp_1943.218)

```
(c / contrast-01
      :ARG1 (a / add-01
            :ARG0 (p / prince
                  :mod (l / little))
            :ARG1 (f / follow-05 :mode interrogative
                  :ARG1 (e / eat-01
                        :ARG0 (t / they)
                        :ARG1 (b / baobab)
                        :mod (a2 / also))
                  :ARG1-of (h / have-condition-91))))
```
219. I pointed out to the little prince that baobabs were not little bushes , but , on the contrary , trees as big as castles ; and that even if he took a whole herd of elephants away with him , the herd would not eat up one single baobab . (lpp_1943.219)

```
(p2 / point-out-02
      :ARG0 (i / i)
      :ARG1 (a / and
            :op1 (t2 / tree
                  :mod (b5 / big
                        :compared-to (c / castle)
                        :degree (e4 / equal))
                  :domain (b2 / baobab)
                  :ARG1-of (i2 / instead-of-91
                        :ARG2 (b3 / bush
                              :mod (l3 / little)
                              :domain b2)))
            :op2 (e / eat-up-02 :polarity -
                  :ARG0 h
                  :ARG1 (b / baobab :quant 1
                        :ARG1-of (s / single-02))
                  :concession (e3 / even-if
                        :op1 (t / take-01
                              :ARG0 p
                              :ARG1 (h / herd
                                    :consist-of (e2 / elephant)
                                    :mod (w / whole))
                              :ARG3 (a2 / away)))))
      :beneficiary (p / prince
            :mod (l2 / little)))
```
220. The idea of the herd of elephants made the little prince laugh . (lpp_1943.220)

```
(m / make-02
      :ARG0 (i / idea
            :topic (h / herd
                  :consist-of (e / elephant)))
      :ARG1 (l / laugh-01
            :ARG0 (p / prince
                  :mod (l2 / little))))
```
221. " We would have to put them one on top of the other , " he said . (lpp_1943.221)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (o / obligate-01
            :ARG2 (s2 / stack-01
                  :ARG0 (w / we)
                  :ARG1 (t / they))))
```
222. But he made a wise comment : " Before they grow so big , the baobabs start out by being little . " (lpp_1943.222)

```
(c2 / contrast-01
      :ARG2 (c / comment-01
            :ARG0 (h / he)
            :ARG1 (s / start-out-05
                  :ARG0 (b2 / baobab)
                  :ARG2 (l / little)
                  :time (b4 / before
                        :op1 (g / grow-02
                              :ARG1 b2
                              :ARG2 (b5 / big
                                    :degree (s2 / so)))))
            :manner (w / wise)))
```
223. " That is strictly correct , " (lpp_1943.223)

```
(c / correct-02
      :ARG1 (t / that)
      :mod (s / strict))
```
224. I said . (lpp_1943.224)

```
(s / say-01
  :ARG0 (i / i))
```
225. " But why do you want the sheep to eat the little baobabs ? " (lpp_1943.225)

```
(c / contrast-01
      :ARG2 (c2 / cause-01
            :ARG0 (a / amr-unknown)
            :ARG1 (w / want-01
                  :ARG0 (y / you)
                  :ARG1 (e / eat-01
                        :ARG0 (s / sheep)
                        :ARG1 (b / baobab
                              :mod (l / little))))))
```
226. He answered me at once , " Oh , come , come ! " , as if he were speaking of something that was self - evident . (lpp_1943.226)

```
(a / answer-01
      :ARG0 (h / he)
      :ARG1 (i2 / i)
      :ARG2 (c / come-on-25)
      :time (i / immediate)
      :conj-as-if (s / speak-01
            :ARG0 h
            :ARG1 (s2 / something
                  :ARG0-of (e / evidence-01
                        :ARG1 s2))))
```
227. And I was obliged to make a great mental effort to solve this problem , without any assistance . (lpp_1943.227)

```
(a / and
      :op1 (o / oblige-02
            :ARG2 (e / effort-01
                  :ARG0 (i / i)
                  :ARG1 (s / solve-01
                        :ARG0 i
                        :ARG1 (p / problem
                              :mod (t / this))
                        :ARG2-of (a2 / assist-01 :polarity -
                              :ARG1 i))
                  :manner (m2 / mental)
                  :mod (g / great))))
```
228. Indeed , as I learned , there were on the planet where the little prince lived -- as on all planets -- good plants and bad plants . (lpp_1943.228)

```
(b2 / be-located-at-91
      :ARG1 (a3 / and
            :op1 (p / plant
                  :ARG1-of (g / good-02))
            :op2 (p2 / plant
                  :ARG1-of (b / bad-07))
            :mod (i / indeed))
      :ARG2 (a / and
            :op1 (p3 / planet
                  :location-of (l / live-01
                        :ARG0 (p4 / prince
                              :mod (l2 / little))))
            :op2 (p5 / planet
                  :mod (a2 / all)))
      :ARG1-of (l3 / learn-01
            :ARG0 (i2 / i)))
```
229. In consequence , there were good seeds from good plants , and bad seeds from bad plants . (lpp_1943.229)

```
(a / and
      :op1 (s / seed
            :ARG1-of (g / good-02)
            :source (p / plant
                  :ARG1-of (g2 / good-02)))
      :op2 (s2 / seed
            :ARG1-of (b / bad-07)
            :source (p2 / plant
                  :ARG1-of (b2 / bad-07)))
      :ARG1-of (c2 / cause-01))
```
230. But seeds are invisible . (lpp_1943.230)

```
(c / contrast-01
      :ARG2 (p / possible-01 :polarity -
            :ARG1 (s2 / see-01
                  :ARG1 (s / seed))))
```
231. They sleep deep in the heart of the earth 's darkness , until some one among them is seized with the desire to awaken . (lpp_1943.231)

```
(s / sleep-01
      :ARG0 (t / they)
      :location (h / heart
            :ARG2-of (d / deep-02)
            :part-of (d2 / darkness
                  :poss (e / earth)))
      :time (u / until
            :op1 (s2 / seize-01
                  :ARG0 (d3 / desire-01
                        :ARG1 (w / wake-01
                              :ARG1 s))
                  :ARG1 (s3 / someone
                        :ARG1-of (i / include-91
                              :ARG2 t)))))
```
232. Then this little seed will stretch itself and begin -- timidly at first -- to push a charming little sprig inoffensively upward toward the sun . (lpp_1943.232)

```
(a / and
      :op1 (s / stretch-01
            :ARG0 (s2 / seed
                  :mod (l / little)
                  :mod (t2 / this))
            :ARG1 s2)
      :op2 (b / begin-01
            :ARG0 s2
            :ARG1 (p / push-01
                  :ARG0 s2
                  :ARG1 (s3 / sprig
                        :mod (l2 / little)
                        :ARG0-of (c / charm-01))
                  :ARG2 (u / upward
                        :direction (s4 / sun))
                  :manner (o / offensive :polarity -))
            :manner (t3 / timid
                  :time (a2 / at-first)))
      :time (t / then))
```
233. If it is only a sprout of radish or the sprig of a rose - bush , one would let it grow wherever it might wish . (lpp_1943.233)

```
(a / allow-01
      :ARG0 (o / one)
      :ARG1 (g / grow-01
            :ARG1 i
            :location (w2 / wish-01
                  :ARG0 i
                  :ARG1-of (p / possible-01)))
      :condition (o2 / or
            :op1 (s / sprout
                  :part-of (r / radish))
            :op2 (s2 / sprig
                  :part-of (b2 / bush
                        :mod (r2 / rose)))
            :mod (o3 / only)
            :domain (i / it)))
```
234. But when it is a bad plant , one must destroy it as soon as possible , the very first instant that one recognizes it . (lpp_1943.234)

```
(c / contrast-01
      :ARG2 (o / obligate-01
            :ARG2 (d / destroy-01
                  :ARG0 (o2 / one)
                  :ARG1 i2
                  :time (i / instant
                        :time-of (r / recognize-01
                              :ARG0 o2
                              :ARG1 i2)
                        :ord (o3 / ordinal-entity :value 1
                              :degree (v / very)))
                  :time (s / soon
                        :degree (m / most)
                        :compared-to (p2 / possible-01
                              :ARG1 d)))
            :condition (p / plant
                  :ARG1-of (b / bad-07)
                  :domain (i2 / it))))
```
235. Now there were some terrible seeds on the planet that was the home of the little prince ; and these were the seeds of the baobab . (lpp_1943.235)

```
(b2 / be-located-at-91
      :ARG1 (s / seed
            :ARG1-of (t / terrible-01)
            :quant (s2 / some)
            :poss (b / baobab))
      :ARG2 (p / planet
            :location-of (h / home
                  :poss (p2 / prince
                        :mod (l / little))))
      :time (n / now))
```
236. The soil of that planet was infested with them . (lpp_1943.236)

```
(i / infest-01
      :ARG1 (s / soil
            :poss (p / planet
                  :mod (t2 / that)))
      :ARG2 (t / they))
```
237. A baobab is something you will never , never be able to get rid of if you attend to it too late . (lpp_1943.237)

```
(p / possible-01 :polarity -
      :ARG1 (e / eliminate-01
            :ARG0 (y / you)
            :ARG1 (b / baobab)
            :time (e2 / ever))
      :condition (a / attend-02
            :ARG0 y
            :ARG1 b
            :time (l / late
                  :degree (t / too))))
```
238. It spreads over the entire planet . (lpp_1943.238)

```
(s / spread-01
  :ARG1 (i / it)
  :ARG2 (p / planet
          :mod (e / entire)))
```
239. It bores clear through it with its roots . (lpp_1943.239)

```
(b / bore-01
      :ARG0 (i / it)
      :ARG2 (t2 / through
            :op1 (i2 / it)
            :mod (c / clear-03))
      :ARG3 (r / root
            :poss i))
```
240. And if the planet is too small , and the baobabs are too many , they split it in pieces ... (lpp_1943.240)

```
(a / and
      :op1 (s / split-01
            :ARG0 b
            :ARG1 p2
            :ARG2 (p / piece)
            :condition (a2 / and
                  :op1 (s2 / small
                        :degree (t2 / too)
                        :domain (p2 / planet))
                  :op2 (b / baobab
                        :quant (m / many
                              :degree (t3 / too))))))
```
241. " It is a question of discipline , " the little prince said to me later on . (lpp_1943.241)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (q / question
            :topic (d / discipline)
            :domain (i / it))
      :ARG2 (i2 / i)
      :time (l2 / late
            :degree (m / more)))
```
242. " When you 've finished your own toilet in the morning , then it is time to attend to the toilet of your planet , just so , with the greatest care . (lpp_1943.242)

```
(a / attend-02
      :ARG0 (y2 / you)
      :ARG1 (t2 / toilet
            :poss (p / planet
                  :poss y)
            :ARG1-of (r / resemble-01
                  :ARG2 t))
      :manner (c / care-04
            :extent (g / great
                  :degree (m2 / most)))
      :time (f / finish-01
            :ARG0 (y / you)
            :ARG1 (t / toilet
                  :poss y)
            :time (d / date-entity :dayperiod (m / morning))))
```
243. You must see to it that you pull up regularly all the baobabs , at the very first moment when they can be distinguished from the rosebushes which they resemble so closely in their earliest youth . (lpp_1943.243)

```
(o2 / obligate-01
      :ARG1 (p / pull-01
            :ARG0 (y / you)
            :ARG1 (b / baobab
                  :mod (a / all))
            :ARG1-of (r / regular-02)
            :time (m / moment
                  :ord (o / ordinal-entity :value 1
                        :degree (v / very))
                  :time-of (p2 / possible-01
                        :ARG1 (d / distinguish-01
                              :ARG1 b
                              :ARG2 (r2 / rosebush
                                    :ARG2-of (r3 / resemble-01
                                          :ARG1 b
                                          :ARG1-of (c / close-10
                                                :degree (s / so))
                                          :time (e / early
                                                :op1 (y2 / youth
                                                      :poss b)
                                                :degree (m2 / most)))))))))
```
244. It is very tedious work , " the little prince added , " but very easy . " (lpp_1943.244)

```
(a / add-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (c / contrast-01
            :ARG1 (t / tedious
                  :degree (v / very)
                  :domain (w / work-01))
            :ARG2 (e / easy-05
                  :degree (v2 / very)
                  :ARG1 w)))
```
245. And one day he said to me : " You ought to make a beautiful drawing , so that the children where you live can see exactly how all this is . (lpp_1943.245)

```
(a / and
      :op1 (s / say-01
            :ARG0 (h / he)
            :ARG1 (r / recommend-01
                  :ARG0 h
                  :ARG1 (d3 / draw-01
                        :ARG0 i
                        :ARG1 (p2 / picture
                              :ARG1-of (b / beautiful-02))
                        :purpose (p / possible-01
                              :ARG1 (s2 / see-01
                                    :ARG0 (c / child
                                          :location (l / live-01
                                                :ARG0 i))
                                    :ARG1 (t / this
                                          :mod (a2 / all))
                                    :manner (e / exact))))
                  :ARG2 i)
            :ARG2 (i / i)
            :time (d / day
                  :mod (o / one))))
```
246. That would be very useful to them if they were to travel some day . (lpp_1943.246)

```
(u / useful-05
      :ARG0 (t2 / they)
      :ARG1 (t / that)
      :degree (v / very)
      :condition (t3 / travel-01
            :ARG0 t2
            :time (d / day
                  :mod (s / some))))
```
247. Sometimes , " he added , " there is no harm in putting off a piece of work until another day . (lpp_1943.247)

```
(a / add-01
      :ARG0 (h / he)
      :ARG1 (h2 / harm-01 :polarity -
            :ARG0 (p / put-off-06
                  :ARG1 (t / thing
                        :ARG1-of (w / work-01)
                        :quant (p3 / piece))
                  :ARG2 (d / day
                        :mod (a2 / another)))
            :time (s / sometimes)))
```
248. But when it is a matter of baobabs , that always means a catastrophe . (lpp_1943.248)

```
(c2 / contrast-01
      :ARG2 (m3 / mean-01
            :ARG1 (t / that)
            :ARG2 (c / catastrophe)
            :time (a / always)
            :condition (b / baobab)))
```
249. I knew a planet that was inhabited by a lazy man . (lpp_1943.249)

```
(k / know-02
      :ARG0 (i / i)
      :ARG1 (p / planet
            :ARG1-of (i2 / inhabit-01
                  :ARG0 (m / man
                        :mod (l / lazy)))))
```
250. He neglected three little bushes ... " (lpp_1943.250)

```
(n / neglect-01
  :ARG0 (h / he)
  :ARG1 (b / bush
          :mod (l / little)
          :quant 3))
```
251. So , as the little prince described it to me , I have made a drawing of that planet . (lpp_1943.251)

```
(d / draw-01
      :ARG0 (i / i)
      :ARG1 (p / planet
            :mod (t / that))
      :manner (d2 / describe-01
            :ARG0 (p2 / prince
                  :mod (l / little))
            :ARG1 p
            :beneficiary i)
      :ARG1-of (c / cause-01))
```
252. I do not much like to take the tone of a moralist . (lpp_1943.252)

```
(l / like-01 :polarity -
      :ARG0 (i / i)
      :ARG1 (t / take-01
            :ARG0 i
            :ARG1 (t2 / tone
                  :poss (m2 / moralist)))
      :degree (m / much))
```
253. But the danger of the baobabs is so little understood , and such considerable risks would be run by anyone who might get lost on an asteroid , that for once I am breaking through my reserve . (lpp_1943.253)

```
(c2 / contrast-01
      :ARG2 (c3 / cause-01
            :ARG0 (a / and
                  :op1 (u / understand-01
                        :ARG1 (d / danger
                              :poss (b2 / baobab))
                        :degree (l / little
                              :degree (s / so)))
                  :op2 (r / risk-01
                        :ARG0 (a2 / anyone
                              :ARG1-of (l2 / lose-02
                                    :location (a3 / asteroid)
                                    :ARG1-of (p / possible-01)))
                        :degree (c / considerable
                              :mod (s2 / such))))
            :ARG1 (b3 / break-away-14
                  :ARG0 (i / i)
                  :ARG1 (r3 / reserve
                        :poss i)
                  :mod (f / for-once))))
```
254. " Children , " (lpp_1943.254)

```
(c2 / child)
```
255. I say plainly , " watch out for the baobabs ! " (lpp_1943.255)

```
(s / say-01
      :ARG0 (i / i)
      :ARG1 (w / watch-out-02 :mode imperative
            :ARG0 (y / you)
            :ARG1 (b / baobab))
      :manner (p / plain))
```
256. My friends , like myself , have been skirting this danger for a long time , without ever knowing it ; and so it is for them that I have worked so hard over this drawing . (lpp_1943.256)

```
(c / cause-01
      :ARG0 (s / skirt-02
            :ARG0 (a / and
                  :op1 (p2 / person
                        :ARG0-of (h2 / have-rel-role-91
                              :ARG1 (i / i)
                              :ARG2 (f / friend)))
                  :op2 i)
            :ARG1 (d / danger
                  :mod (t / this))
            :ARG1-of (k / know-01 :polarity -
                  :ARG0 p2
                  :time (e / ever))
            :ARG1-of (l / long-03))
      :ARG1 (w / work-01
            :ARG0 i
            :ARG1 (p / picture
                  :ARG1-of (d2 / draw-01)
                  :mod (t3 / this))
            :ARG1-of (h / hard-02
                  :degree (s2 / so))
            :beneficiary p2))
```
257. The lesson which I pass on by this means is worth all the trouble it has cost me . (lpp_1943.257)

```
(w / worth-02
      :ARG1 (l / lesson
            :ARG1-of (p / pass-on-09
                  :ARG0 (i / i)
                  :manner (t2 / this)))
      :ARG2 (t / trouble
            :ARG2-of (c / cost-01
                  :ARG1 l
                  :ARG3 i)
            :mod (a / all)))
```
258. Perhaps you will ask me , " Why are there no other drawing in this book as magnificent and impressive as this drawing of the baobabs ? " (lpp_1943.258)

```
(p / possible-01
      :ARG1 (a / ask-01
            :ARG0 (y / you)
            :ARG1 (p2 / picture :polarity -
                  :ARG1-of (d / draw-01)
                  :mod (o / other)
                  :location (b / book
                        :mod (t / this))
                  :mod (m / magnificent
                        :degree (e / equal)
                        :compared-to (p3 / picture
                              :ARG1-of (d2 / draw-01)
                              :mod (t2 / this)
                              :topic (b2 / baobab)))
                  :ARG0-of (i / impress-01
                        :degree (e2 / equal)
                        :compared-to p3)
                  :ARG0-of (c / cause-01
                        :ARG1 (a2 / amr-unknown)))
            :ARG2 (i2 / i)))
```
259. The reply is simple . (lpp_1943.259)

```
(s / simple-02
      :ARG1 (t / thing
            :ARG2-of (r / reply-01)))
```
260. I have tried . (lpp_1943.260)

```
(t / try-01
  :ARG0 (i / i))
```
261. But with the others I have not been successful . (lpp_1943.261)

```
(c / contrast-01
      :ARG2 (s / succeed-01 :polarity -
            :ARG0 (i / i)
            :ARG1 (o / other)))
```
262. When I made the drawing of the baobabs I was carried beyond myself by the inspiring force of urgent necessity . (lpp_1943.262)

```
(c / carry-01
      :ARG0 (f / force-01
            :ARG0 (n / necessity
                  :mod (u / urgent))
            :ARG0-of (i2 / inspire-01))
      :ARG1 (i / i)
      :destination (b / beyond
            :op1 i)
      :time (d / draw-01
            :ARG0 i
            :ARG1 (b2 / baobab)))
```
263. Chapter 6 . (lpp_1943.263)

```
(c / chapter :mod 6)
```
264. Oh , little prince ! (lpp_1943.264)

```
(p / prince
      :mod (l / little))
```
265. Bit by bit I came to understand the secrets of your sad little life ... (lpp_1943.265)

```
(u / understand-01
      :ARG0 (i / i)
      :ARG1 (s / secret
            :poss (l / life
                  :poss (y / you)
                  :mod (l2 / little)
                  :ARG1-of (s2 / sad-02)))
      :manner (b / bit-by-bit))
```
266. For a long time you had found your only entertainment in the quiet pleasure of looking at the sunset . (lpp_1943.266)

```
(f / find-01
      :ARG0 (y / you)
      :ARG1 (e / entertain-01
            :ARG0 (l2 / look-01
                  :ARG0 y
                  :ARG1 (s / sunset)
                  :mod (p / pleasure
                        :ARG1-of (q / quiet-04)))
            :ARG1 y
            :mod (o / only))
      :ARG1-of (l / long-03))
```
267. I learned that new detail on the morning of the fourth day , when you said to me : " I am very fond of sunsets . (lpp_1943.267)

```
(l / learn-01
      :ARG0 (i / i)
      :ARG1 (d / detail
            :ARG1-of (n / new-01)
            :mod (t / that))
      :time (d3 / date-entity
            :dayperiod (m / morning)
            :mod (d2 / day
                  :ord (o / ordinal-entity :value 4)))
      :time (s / say-01
            :ARG0 (y / you)
            :ARG1 (l2 / like-01
                  :ARG0 y
                  :ARG1 (s2 / sunset)
                  :degree (v / very))
            :ARG2 i))
```
268. Come , let us go look at a sunset now . " (lpp_1943.268)

```
(a / and
      :op1 (c / come-01 :mode imperative
            :ARG1 (y / you))
      :op2 (g / go-05 :mode imperative
            :ARG0 w
            :ARG1 (l / look-01
                  :ARG0 (w / we)
                  :ARG1 (s / sunset)
                  :time (n / now))))
```
269. " But we must wait , " (lpp_1943.269)

```
(c / contrast-01
      :ARG2 (o / obligate-01
            :ARG2 (w2 / wait-01
                  :ARG1 (w / we))))
```
270. I said . (lpp_1943.270)

```
(s / say-01
  :ARG0 (i / i))
```
271. " Wait ? (lpp_1943.271)

```
(w / wait-01 :mode interrogative)
```
272. For what ? " (lpp_1943.272)

```
(w / wait-01
      :ARG2 (a / amr-unknown))
```
273. " For the sunset . (lpp_1943.273)

```
(w / wait-01
      :ARG2 (s / sunset))
```
274. We must wait until it is time . " (lpp_1943.274)

```
(o / obligate-01
      :ARG2 (w2 / wait-01
            :ARG1 (w / we)
            :duration (u / until
                  :op1 (t / time))))
```
275. At first you seemed to be very much surprised . (lpp_1943.275)

```
(s / seem-01
      :ARG1 (s2 / surprise-01
            :ARG1 (y / you)
            :degree (m / much
                  :degree (v / very)))
      :time (a / at-first))
```
276. And then you laughed to yourself . (lpp_1943.276)

```
(a / and
      :op1 (l / laugh-01
            :ARG0 (y / you)
            :ARG2 y
            :time (t / then)))
```
277. You said to me : " I am always thinking that I am at home ! " (lpp_1943.277)

```
(s / say-01
      :ARG0 (y / you)
      :ARG1 (t / think-01
            :ARG0 y
            :ARG1 (b / be-located-at-91
                  :ARG1 y
                  :ARG2 (h / home))
            :time (a / always))
      :ARG2 (i / i))
```
278. Just so . (lpp_1943.278)

```
(s / so
  :mod (j / just))
```
279. Everybody knows that when it is noon in the United States the sun is setting over France . (lpp_1943.279)

```
(k / know-01
      :ARG0 (e / everybody)
      :ARG1 (s / set-11
            :ARG1 (s2 / sun)
            :location (c2 / country :wiki "France"
                  :name (n3 / name :op1 "France"))
            :time (d / date-entity :time "12:00"
                  :location (c / country :wiki "United_States"
                        :name (n2 / name :op1 "United" :op2 "States")))))
```
280. If you could fly to France in one minute , you could go straight into the sunset , right from noon . (lpp_1943.280)

```
(p / possible-01
      :ARG1 (g / go-02
            :ARG0 y
            :ARG3 (d / date-entity :time "12:00")
            :ARG4 (s / sunset)
            :ARG1-of (s2 / straight-04))
      :condition (p2 / possible-01
            :ARG1 (f / fly-01
                  :ARG1 (y / you)
                  :duration (t / temporal-quantity :quant 1
                        :unit (m / minute))
                  :destination (c / country :wiki "France" :name (n / name :op1 "France")))))
```
281. Unfortunately , France is too far away for that . (lpp_1943.281)

```
(f / fortunate-01 :polarity -
      :ARG2 (b / be-located-at-91
            :ARG1 (c / country :wiki "France"
                  :name (n / name :op1 "France"))
            :ARG2 (a / away
                  :extent (f2 / far
                        :degree (t / too)))
            :purpose (t2 / that)))
```
282. But on your tiny planet , my little prince , all you need do is move your chair a few steps . (lpp_1943.282)

```
(s2 / say-01
      :ARG1 (c2 / contrast-01
            :ARG2 (o / obligate-01
                  :ARG2 (m / move-01
                        :ARG0 p2
                        :ARG1 (c / chair
                              :poss p2)
                        :extent (s / step
                              :quant (f / few))
                        :mod (o2 / only))
                  :location (p / planet
                        :mod (t / tiny)
                        :poss (p2 / prince
                              :mod (l / little)
                              :poss (i / i)))))
      :ARG2 p2)
```
283. You can see the day end and the twilight falling whenever you like ... (lpp_1943.283)

```
(p / possible-01
      :ARG1 (s / see-01
            :ARG0 (y / you)
            :ARG1 (a / and
                  :op1 (e / end-01
                        :ARG1 (d / day))
                  :op2 (f / fall-04
                        :ARG1 (t / twilight)))
            :time (l / like-02
                  :ARG0 y
                  :ARG1 s
                  :mod (a2 / any))))
```
284. " One day , " you said to me , " I saw the sunset forty - four times ! " (lpp_1943.284)

```
(s / say-01
      :ARG0 (y / you)
      :ARG1 (s2 / see-01 :frequency 44
            :ARG0 y
            :ARG1 (s3 / sunset)
            :time (d / day
                  :mod (o / one)))
      :ARG2 (i / i))
```
285. And a little later you added : " You know -- one loves the sunset , when one is so sad ... " (lpp_1943.285)

```
(a / and
      :op1 (a2 / add-01
            :ARG0 (y / you)
            :ARG1 (l3 / love-01
                  :ARG0 (o / one)
                  :ARG1 (s / sunset)
                  :time (s2 / sad-02
                        :ARG1 o
                        :mod (s3 / so)))
            :time (l / late
                  :degree (m / more
                        :quant (l2 / little)))))
```
286. " Were you so sad , then ? " (lpp_1943.286)

```
(s / sad-02 :mode interrogative
      :ARG1 (y / you)
      :time (t / then)
      :degree (s2 / so))
```
287. I asked , " on the day of the forty - four sunsets ? " (lpp_1943.287)

```
(a / ask-01
      :ARG0 (i / i)
      :ARG1 (b / be-temporally-at-91 :mode interrogative
            :ARG2 (d / day
                  :ARG0-of (h / have-03
                        :ARG1 (s / sunset :quant 44)))))
```
288. But the little prince made no reply . (lpp_1943.288)

```
(c / contrast-01
      :ARG2 (r / reply-01 :polarity -
            :ARG0 (p / prince
                  :mod (l / little))))
```
289. Chapter 7 . (lpp_1943.289)

```
(c / chapter :mod 7)
```
290. On the fifth day -- again , as always , it was thanks to the sheep -- the secret of the little prince 's life was revealed to me . (lpp_1943.290)

```
(r / reveal-01
      :ARG0 (s / sheep
            :ARG1-of (t / thank-01))
      :ARG1 (s2 / secret
            :poss (l / life
                  :poss (p / prince
                        :mod (l2 / little))))
      :ARG2 (i / i)
      :time (d / day
            :ord (o / ordinal-entity :value 5))
      :mod (a / again)
      :time (a2 / always))
```
291. Abruptly , without anything to lead up to it , and as if the question had been born of long and silent meditation on his problem , he demanded : " A sheep -- if it eats little bushes , does it eat flowers , too ? " (lpp_1943.291)

```
(d / demand-01
      :ARG0 (h / he)
      :ARG1 (e / eat-01 :mode interrogative
            :ARG0 (s / sheep)
            :ARG1 (f / flower
                  :mod (t / too))
            :condition (e2 / eat-01
                  :ARG0 s
                  :ARG1 (b / bush
                        :mod (l / little))))
      :manner (a / abrupt)
      :conj-as-if (b2 / bear-02
            :ARG0 (m / meditate-01
                  :ARG1 (p / problem
                        :poss h)
                  :ARG1-of (l3 / long-03)
                  :manner (s2 / silent))
            :ARG1 (t2 / thing
                  :ARG1-of (q / question-01)))
      :ARG2-of (l2 / lead-up-05 :polarity -
            :ARG1 (a2 / anything)))
```
292. " A sheep , " (lpp_1943.292)

```
(s / sheep)
```
293. I answered , " eats anything it finds in its reach . " (lpp_1943.293)

```
(a / answer-01
      :ARG0 (i / i)
      :ARG1 (e / eat-01
            :ARG1 (a2 / anything
                  :ARG1-of (f / find-01
                        :ARG0 (i2 / it)
                        :location (r / reach-03
                              :ARG0 i2)))))
```
294. " Even flowers that have thorns ? " (lpp_1943.294)

```
(f / flower :mode interrogative
      :mod (e / even)
      :ARG0-of (h / have-03
            :ARG1 (t / thorn)))
```
295. " Yes , even flowers that have thorns . " (lpp_1943.295)

```
(f / flower
      :mod (e / even)
      :ARG0-of (h / have-03
            :ARG1 (t / thorn)))
```
296. " Then the thorns -- what use are they ? " (lpp_1943.296)

```
(h / have-purpose-91
      :ARG1 (t / thorn)
      :ARG2 (a / amr-unknown)
      :ARG1-of (h2 / have-condition-91))
```
297. I did not know . (lpp_1943.297)

```
(k / know-01
  :ARG0 (i / i)
  :polarity -)
```
298. At that moment I was very busy trying to unscrew a bolt that had got stuck in my engine . (lpp_1943.298)

```
(t / try-01
      :ARG0 (i / i
            :ARG1-of (b2 / busy-01
                  :degree (v / very)))
      :ARG1 (u / unscrew-01
            :ARG0 i
            :ARG1 (b / bolt
                  :ARG1-of (s / stick-01
                        :ARG2 (e / engine
                              :poss i))))
      :time (m / moment
            :mod (t2 / that)))
```
299. I was very much worried , for it was becoming clear to me that the breakdown of my plane was extremely serious . (lpp_1943.299)

```
(c2 / cause-01
      :ARG0 (c / clear-06
            :ARG1 (s / serious-02
                  :ARG1 (b / break-down-12
                        :ARG1 (p / plane
                              :poss i))
                  :degree (e / extreme))
            :ARG2 (i / i))
      :ARG1 (w / worry-01
            :ARG1 i
            :quant (m / much
                  :degree (v / very))))
```
300. And I had so little drinking - water left that I had to fear for the worst . (lpp_1943.300)

```
(a / and
      :op1 (h / have-03
            :ARG0 (i / i)
            :ARG1 (w / water
                  :purpose (d / drink-01)
                  :mod (l / little
                        :degree (s / so))
                  :ARG1-of (l2 / leave-17))
            :ARG0-of (o / obligate-01
                  :ARG1 i
                  :ARG2 (f / fear-01
                        :ARG0 i
                        :ARG1 (b / bad-07
                              :degree (m / most))))))
```
301. " The thorns - - what use are they ? " (lpp_1943.301)

```
(u / use-01
  :ARG1 (t / thorn)
  :ARG2 (a / amr-unknown))
```
302. The little prince never let go of a question , once he had asked it . (lpp_1943.302)

```
(l / let-01 :polarity -
      :ARG0 (p / prince
            :mod (l2 / little))
      :ARG1 (g / go-01
            :ARG1 (t / thing
                  :ARG1-of (q / question-01
                        :ARG0 p)))
      :time (o / once
            :op1 (a / ask-01
                  :ARG0 p
                  :ARG1 q)))
```
303. As for me , I was upset over that bolt . (lpp_1943.303)

```
(u / upset-01
      :ARG0 (b / bolt
            :mod (t / that))
      :ARG1 (i / i))
```
304. And I answered with the first thing that came into my head : " The thorns are of no use at all . (lpp_1943.304)

```
(a / and
      :op1 (a2 / answer-01
            :ARG0 (i / i)
            :ARG2 (t / thing
                  :ord (o / ordinal-entity :value 1)
                  :ARG1-of (c / come-01
                        :ARG4 (h / head
                              :part-of i))
                  :domain (u / use-01 :polarity -
                        :ARG1 (t2 / thorn)
                        :ARG2 (a3 / anything)))))
```
305. Flowers have thorns just for spite ! " (lpp_1943.305)

```
(h / have-03
      :ARG0 (f / flower)
      :ARG1 (t / thorn)
      :purpose (s / spite)
      :mod (j / just))
```
306. " Oh ! " (lpp_1943.306)

```
(o / oh :mode expressive)
```
307. There was a moment of complete silence . (lpp_1943.307)

```
(m / moment
      :ARG1-of (c / compose-01
            :ARG2 (s / silent
                  :ARG1-of (c2 / complete-02))))
```
308. Then the little prince flashed back at me , with a kind of resentfulness : " I do n't believe you ! (lpp_1943.308)

```
(f / flash-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (b / believe-01 :polarity -
            :ARG0 p
            :ARG1 i)
      :ARG2 (i / i)
      :time (t / then)
      :manner (r / resent-01
            :ARG0 p
            :mod (k / kind))
      :direction (b2 / back))
```
309. Flowers are weak creatures . (lpp_1943.309)

```
(c / creature
      :ARG1-of (w / weak-02)
      :domain (f / flower))
```
310. They are naïve . (lpp_1943.310)

```
(n / naive
      :domain (t / they))
```
311. They reassure themselves as best they can . (lpp_1943.311)

```
(r / reassure-01
      :ARG0 (t / they)
      :ARG1 t
      :ARG2-of (g / good-03
            :ARG1 t
            :degree (m / most)
            :compared-to (p2 / possible-01
                  :ARG1 (r2 / reassure-01
                        :ARG0 t
                        :ARG1 t))))
```
312. They believe that their thorns are terrible weapons ... " (lpp_1943.312)

```
(b2 / believe-01
      :ARG0 (t / they)
      :ARG1 (w / weapon
            :domain (t2 / thorn
                  :poss t)
            :ARG1-of (t3 / terrible-01)))
```
313. I did not answer . (lpp_1943.313)

```
(a / answer-01
  :ARG0 (i / i)
  :polarity -)
```
314. At that instant I was saying to myself : " If this bolt still will n't turn , I am going to knock it out with the hammer . " (lpp_1943.314)

```
(s / say-01
      :ARG0 (i / i)
      :ARG1 (k / knock-out-03
            :ARG0 i
            :ARG1 b
            :ARG2 (h / hammer)
            :condition (t2 / turn-01 :polarity -
                  :ARG1 (b / bolt
                        :mod (t3 / this))
                  :mod (s2 / still)))
      :ARG2 i
      :time (i2 / instant
            :mod (t / that)))
```
315. Again the little prince disturbed my thoughts . (lpp_1943.315)

```
(d / disturb-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (t / think-01
            :ARG0 (i / i))
      :mod (a / again))
```
316. " And you actually believe that the flowers - - " (lpp_1943.316)

```
(a / and
      :op1 (b / believe-01
            :ARG0 (y / you)
            :ARG1 (d / do-02
                  :ARG0 (f / flower))
            :ARG1-of (a2 / actual-02)))
```
317. " Oh , no ! " (lpp_1943.317)

```
(n / no
      :mod (o / oh :mode expressive))
```
318. I cried . (lpp_1943.318)

```
(c / cry-01
  :ARG0 (i / i))
```
319. " No , no no ! (lpp_1943.319)

```
(n / no :quant 3)
```
320. I do n't believe anything . (lpp_1943.320)

```
(b2 / believe-01 :polarity -
      :ARG0 (i / i)
      :ARG1 (a2 / anything))
```
321. I answered you with the first thing that came into my head . (lpp_1943.321)

```
(a / answer-01
      :ARG0 (i / i)
      :ARG1 (y / you)
      :ARG2 (t / thing
            :ord (o / ordinal-entity :value 1)
            :ARG1-of (c / come-01
                  :ARG4 (h / head
                        :part-of i))))
```
322. Do n't you see - - I am very busy with matters of consequence ! " (lpp_1943.322)

```
(s / see-01 :polarity - :mode interrogative
      :ARG0 (y / you)
      :ARG1 (b / busy-01
            :ARG1 (i / i)
            :ARG2 (m / matter
                  :ARG0-of (h / have-03
                        :ARG1 (c3 / consequence)))
            :degree (v / very)))
```
323. He stared at me , thunderstruck . (lpp_1943.323)

```
(s / stare-01
      :ARG0 (h / he
            :mod (t / thunderstruck))
      :ARG1 (i / i))
```
324. " Matters of consequence ! " (lpp_1943.324)

```
(m / matter
      :ARG0-of (h / have-03
            :ARG1 (c / consequence)))
```
325. He looked at me there , with my hammer in my hand , my fingers black with engine - grease , bending down over an object which seemed to him extremely ugly ... (lpp_1943.325)

```
(l / look-01
      :ARG0 (h / he)
      :ARG1 (i / i
            :ARG0-of (b2 / bend-01
                  :destination (d / down)
                  :location (o / object
                        :mod (u / ugly
                              :mod (s / seem-01
                                    :ARG2 h)
                              :degree (e2 / extreme))))
            :ARG0-of (h4 / have-03
                  :ARG1 (h2 / hammer
                        :poss i)
                  :location (h3 / hand
                        :part-of i))
            :ARG0-of (h5 / have-03
                  :ARG1 (f / finger
                        :part-of i
                        :ARG1-of (b / black-04
                              :ARG0 (g / grease
                                    :mod (e / engine))))))
      :location (t / there))
```
326. " You talk just like the grown - ups ! " (lpp_1943.326)

```
(t2 / talk-01
      :ARG0 (y / you)
      :ARG1-of (r / resemble-01
            :ARG2 (g2 / grown-up)
            :mod (j2 / just)))
```
327. That made me a little ashamed . (lpp_1943.327)

```
(s / shame-01
      :ARG0 (t / that)
      :ARG1 (i / i)
      :degree (l / little))
```
328. But he went on , relentlessly : " You mix everything up together ... (lpp_1943.328)

```
(c / contrast-01
      :ARG2 (g / go-on-25
            :ARG0 (h / he)
            :ARG1 (m / mix-up-02
                  :ARG0 (y / you)
                  :ARG1 (e / everything)
                  :ARG3 (t / together))
            :manner (r / relentless)))
```
329. You confuse everything ... " (lpp_1943.329)

```
(c2 / confuse-01
      :ARG0 (y2 / you)
      :ARG2 (e2 / everything))
```
330. He was really very angry . (lpp_1943.330)

```
(a / angry
      :domain (h / he)
      :degree (v / very)
      :ARG1-of (r / real-04))
```
331. He tossed his golden curls in the breeze . (lpp_1943.331)

```
(t / toss-01
  :ARG0 (h / he)
  :ARG1 (c / curl
          :poss h
          :mod (g / golden))
  :location (b / breeze))
```
332. " I know a planet where there is a certain red - faced gentleman . (lpp_1943.332)

```
(k / know-02
      :ARG0 (i / i)
      :ARG1 (p / planet
            :location-of (g2 / gentleman
                  :mod (c / certain)
                  :part (f / face
                        :ARG1-of (r / red-02)))))
```
333. He has never smelled a flower . (lpp_1943.333)

```
(s / smell-01 :polarity -
      :ARG0 (h / he)
      :ARG1 (f / flower)
      :time (e / ever))
```
334. He has never looked at a star . (lpp_1943.334)

```
(l / look-01 :polarity -
      :ARG0 (h / he)
      :ARG1 (s / star)
      :time (e / ever))
```
335. He has never loved any one . (lpp_1943.335)

```
(l2 / love-01 :polarity -
      :ARG0 (h3 / he)
      :ARG1 (a2 / anyone)
      :time (e / ever))
```
336. He has never done anything in his life but add up figures . (lpp_1943.336)

```
(d / do-02 :polarity -
      :ARG0 (h / he)
      :ARG1 (a2 / anything)
      :time (l / live-01
            :ARG0 h)
      :time (e / ever)
      :ARG2-of (e2 / except-01
            :ARG1 (a / add-up-04
                  :ARG0 h
                  :ARG1 (f / figure))))
```
337. And all day he says over and over , just like you : ' I am busy with matters of consequence ! ' And that makes him swell up with pride . (lpp_1943.337)

```
(m2 / multi-sentence
      :snt1 (a / and
            :op1 (s / say-01
                  :ARG0 (h / he)
                  :ARG1 (b / busy-01
                        :ARG1 h
                        :ARG2 (m / matter
                              :ARG0-of (h3 / have-03
                                    :ARG1 (c2 / consequence))))
                  :time (d / day
                        :mod (a2 / all))
                  :frequency (o / over-and-over)
                  :manner (r / resemble-01
                        :ARG2 (y / you)
                        :mod (j / just))
                  :ARG0-of (c3 / cause-01)))
      :snt2 (a3 / and
            :op1 (m3 / make-02
                  :ARG0 (t / that)
                  :ARG1 (s2 / swell-01
                        :ARG0 t
                        :ARG1 h2
                        :manner (p / pride-01
                              :ARG0 (h2 / he)
                              :ARG2 t)))))
```
338. But he is not a man - - he is a mushroom ! " (lpp_1943.338)

```
(c / contrast-01
      :ARG2 (a / and
            :op1 (m / man :polarity -
                  :domain h)
            :op2 (m2 / mushroom
                  :domain (h / he))))
```
339. " A what ? " (lpp_1943.339)

```
(a / amr-unknown)
```
340. " A mushroom ! " (lpp_1943.340)

```
(m / mushroom)
```
341. The little prince was now white with rage . (lpp_1943.341)

```
(w / white-03
      :ARG1 (p / prince
            :mod (l / little))
      :time (n / now)
      :ARG1-of (c / cause-01
            :ARG0 (e / enrage-01
                  :ARG1 p)))
```
342. " The flowers have been growing thorns for millions of years . (lpp_1943.342)

```
(g / grow-03
      :ARG0 (f / flower)
      :ARG1 (t / thorn)
      :duration (m / multiple
            :op1 (t2 / temporal-quantity :quant 1000000
                  :unit (y / year))))
```
343. For millions of years the sheep have been eating them just the same . (lpp_1943.343)

```
(e / eat-01
      :ARG0 (s / sheep)
      :ARG1 (t / they)
      :duration (m / multiple
            :op1 (t2 / temporal-quantity :quant 1000000
                  :unit (y / year)))
      :ARG1-of (h / have-concession-91))
```
344. And is it not a matter of consequence to try to understand why the flowers go to so much trouble to grow thorns which are never of any use to them ? (lpp_1943.344)

```
(a / and
      :op1 (h / have-03 :polarity - :mode interrogative
            :ARG0 (t / try-01
                  :ARG1 (u / understand-01
                        :ARG1 (t4 / thing
                              :ARG0-of (c2 / cause-01
                                    :ARG1 (e / endure-01
                                          :ARG1 (f / flower)
                                          :ARG2 (t2 / trouble
                                                :purpose (g2 / grow-01
                                                      :ARG0 f
                                                      :ARG1 (t3 / thorn
                                                            :ARG1-of (u2 / use-01 :polarity -
                                                                  :ARG0 f
                                                                  :time (e2 / ever))))
                                                :quant (m / much
                                                      :degree (s / so))))))))
            :ARG1 (c / consequence)))
```
345. Is the warfare between the sheep and the flowers not important ? (lpp_1943.345)

```
(i2 / important :polarity - :mode interrogative
      :domain (w / war-01
            :ARG0 (s / sheep)
            :ARG1 (f / flower)))
```
346. Is this not of more consequence than a fat red - faced gentleman 's sums ? (lpp_1943.346)

```
(h / have-03 :mode interrogative :polarity -
      :ARG0 (t / this)
      :ARG1 (c / consequence
            :compared-to (s / sum
                  :poss (g / gentleman
                        :ARG1-of (f / fat-03)
                        :part (f2 / face
                              :ARG1-of (r / red-02))))
            :degree (m2 / more)))
```
347. And if I know - - I , myself - - one flower which is unique in the world , which grows nowhere but on my planet , but which one little sheep can destroy in a single bite some morning , without even noticing what he is doing - - Oh ! (lpp_1943.347)

```
(a / and
      :op1 (o / oh :mode expressive
            :condition (k / know-02
                  :ARG0 (i / i)
                  :ARG1 (f / flower :quant 1
                        :mod (u / unique
                              :location (w / world))
                        :ARG1-of (g / grow-01
                              :location (c / contrast-01
                                    :ARG0 (n / nowhere)
                                    :ARG1 (p / planet
                                          :poss i)))
                        :ARG1-of (d / destroy-01
                              :ARG0 (s / sheep :quant 1
                                    :mod (l / little)
                                    :ARG0-of (n2 / notice-01 :polarity -
                                          :ARG1 d))
                              :ARG2 (b / bite-01 :quant 1
                                    :ARG1-of (s3 / single-02))
                              :ARG2-of c2
                              :ARG1-of (p2 / possible-01)
                              :time (d2 / date-entity
                                    :dayperiod (m / morning)
                                    :mod (s2 / some))))
                  :ARG1-of (c2 / contrast-01))))
```
348. You think that is not important ! " (lpp_1943.348)

```
(t / think-01
      :ARG0 (y / you)
      :ARG1 (t2 / that
            :mod (i / important :polarity -)))
```
349. His face turned from white to red as he continued : " If some one loves a flower , of which just one single blossom grows in all the millions and millions of stars , it is enough to make him happy just to look at the stars . (lpp_1943.349)

```
(t / turn-02
      :ARG1 (f / face
            :part-of (h / he))
      :ARG2 (r / red-02
            :ARG1 f)
      :ARG3 (w / white-03
            :ARG1 f)
      :time (c / continue-02
            :ARG0 h
            :ARG1 (s3 / suffice-01
                  :ARG0 l
                  :ARG1 (m / make-02
                        :ARG0 l
                        :ARG1 (h2 / happy-01
                              :ARG1 s)
                        :ARG1-of (c2 / cause-01
                              :ARG0 (l2 / look-01
                                    :ARG0 s
                                    :ARG1 s2
                                    :mod (j2 / just))))
                  :condition (l / love-01
                        :ARG0 (s / someone)
                        :ARG1 (f2 / flower
                              :part (b / blossom :quant 1
                                    :mod (j / just)
                                    :ARG1-of (g / grow-01
                                          :location (s2 / star
                                                :mod (a2 / all)
                                                :quant (m2 / multiple :op1 1000000)))
                                    :ARG1-of (s4 / single-02)))))))
```
350. He can say to himself , ' Somewhere , my flower is there ... ' But if the sheep eats the flower , in one moment all his stars will be darkened ... (lpp_1943.350)

```
(p2 / possible-01
      :ARG1 (s / say-01
            :ARG0 (h / he)
            :ARG1 (c / contrast-01
                  :ARG1 (b / be-located-at-91
                        :ARG1 (f2 / flower
                              :poss h)
                        :ARG2 (t2 / there))
                  :ARG2 (d / darken-01
                        :ARG1 (s4 / star
                              :mod (a / all)
                              :poss h)
                        :condition (e2 / eat-01
                              :ARG0 (s3 / sheep)
                              :ARG1 f2)
                        :time (m / moment :quant 1)))
            :ARG2 h))
```
351. And you think that is not important ! " (lpp_1943.351)

```
(a2 / and
      :op1 (t / think-01
            :ARG0 (y / you)
            :ARG1 (i / important :polarity -
                  :domain (t2 / that))))
```
352. He could not say anything more . (lpp_1943.352)

```
(p / possible-01 :polarity -
      :ARG1 (s / say-01
            :ARG0 (h / he)
            :ARG1 (a / anything
                  :mod (m / more))))
```
353. His words were choked by sobbing . (lpp_1943.353)

```
(c / choke-up-04
      :ARG0 (s / sob-01)
      :ARG1 (w / word
            :poss (h / he)))
```
354. The night had fallen . (lpp_1943.354)

```
(f / fall-04
  :ARG1 (n / night))
```
355. I had let my tools drop from my hands . (lpp_1943.355)

```
(l / let-01
      :ARG0 (i / i)
      :ARG1 (d / drop-01
            :ARG1 (t / tool
                  :poss i)
            :ARG3 (h / hand
                  :part-of i)))
```
356. Of what moment now was my hammer , my bolt , or thirst , or death ? (lpp_1943.356)

```
(o / or
      :op1 (h / hammer
            :poss (i / i))
      :op2 (b / bolt
            :poss i)
      :op3 (t / thirst-01
            :ARG0 i)
      :op4 (d / die-01
            :ARG1 i)
      :time (m / moment
            :mod (a / amr-unknown)))
```
357. On one star , one planet , my planet , the Earth , there was a little prince to be comforted . (lpp_1943.357)

```
(b / be-located-at-91
      :ARG1 (p / prince
            :mod (l / little)
            :ARG1-of (c / comfort-01
                  :ARG2-of (o / obligate-01)))
      :ARG2 (a / and
            :op1 (s / star :quant 1)
            :op2 (p2 / planet :quant 1)
            :op3 (p4 / planet :wiki "Earth"
                  :name (n / name :op1 "Earth")
                  :poss (i / i))))
```
358. I took him in my arms , and rocked him . (lpp_1943.358)

```
(a / and
      :op1 (t / take-01
            :ARG0 (i / i)
            :ARG1 (h / he)
            :ARG3 (a2 / arm
                  :part-of i))
      :op2 (r / rock-01
            :ARG0 i
            :ARG1 h))
```
359. I said to him : " The flower that you love is not in danger . (lpp_1943.359)

```
(s / say-01
      :ARG0 (i / i)
      :ARG1 (e / endanger-01 :polarity -
            :ARG1 (f / flower
                  :ARG1-of (l / love-01
                        :ARG0 h)))
      :ARG2 (h / he))
```
360. I will draw you a muzzle for your sheep . (lpp_1943.360)

```
(d / draw-01
      :ARG0 (i / i)
      :ARG1 (t / thing
            :ARG2-of (m / muzzle-01
                  :ARG1 (s / sheep
                        :poss y)))
      :ARG2 (y / you))
```
361. I will draw you a railing to put around your flower . (lpp_1943.361)

```
(d2 / draw-01
      :ARG0 (i / i)
      :ARG1 (r / railing
            :ARG1-of (p / put-01
                  :ARG2 (a / around
                        :op1 (f / flower
                              :poss y))))
      :ARG2 (y / you))
```
362. I will - - " (lpp_1943.362)

```
(d / do-02
      :ARG0 (i / i))
```
363. I did not know what to say to him . (lpp_1943.363)

```
(k / know-01 :polarity -
      :ARG0 (i / i)
      :ARG1 (t / thing
            :ARG1-of (s / say-01
                  :ARG0 i
                  :ARG2 (h / he))))
```
364. I felt awkward and blundering . (lpp_1943.364)

```
(f / feel-01
      :ARG0 (i / i)
      :ARG1 (a / and
            :op1 (a2 / awkward)
            :op2 (b / blunder-01
                  :ARG0 i)))
```
365. I did not know how I could reach him , where I could overtake him and go on hand in hand with him once more . (lpp_1943.365)

```
(k / know-01 :polarity -
      :ARG0 (i / i)
      :ARG1 (a2 / and
            :op1 (m / manner
                  :manner-of (r / reach-02
                        :ARG0 i
                        :ARG1 (h / he)
                        :ARG1-of (p / possible-01)))
            :op2 (l / location
                  :location-of (o / overtake-01
                        :ARG0 i
                        :ARG1 h
                        :ARG1-of (p2 / possible-01))
                  :location-of (g / go-on-15
                        :ARG1 i
                        :mod (a3 / again :frequency 1)
                        :manner (a / accompany-01
                              :ARG0 h
                              :ARG1 i
                              :manner (h2 / hand-in-hand))))))
```
366. It is such a secret place , the land of tears . (lpp_1943.366)

```
(p / place
      :mod (s / secret
            :degree (s2 / such))
      :domain (l / land
            :location-of (t / tear)))
```
367. Chapter 8 . (lpp_1943.367)

```
(c / chapter :mod 8)
```
368. I soon learned to know this flower better . (lpp_1943.368)

```
(l / learn-01
      :ARG0 (i / i)
      :ARG1 (k / know-02
            :ARG0 i
            :ARG1 (f / flower
                  :mod (t / this))
            :ARG2-of (g / good-03
                  :ARG1 i
                  :degree (m / more)))
      :time (s / soon))
```
369. On the little prince 's planet the flowers had always been very simple . (lpp_1943.369)

```
(s / simple-02
      :ARG1 (f / flower)
      :degree (v / very)
      :time (a / always)
      :location (p / planet
            :poss (p2 / prince
                  :mod (l / little))))
```
370. They had only one ring of petals ; they took up no room at all ; they were a trouble to nobody . (lpp_1943.370)

```
(m / multi-sentence
      :snt1 (h / have-03
            :ARG0 (t / they)
            :ARG1 (r / ring :quant 1
                  :mod (o / only)
                  :consist-of (p / petal)))
      :snt2 (t2 / take-up-13 :polarity -
            :ARG0 t
            :ARG1 (r2 / room)
            :degree (a / at-all))
      :snt3 (t3 / trouble-01 :polarity -
            :ARG0 t
            :ARG1 (a2 / anybody)))
```
371. One morning they would appear in the grass , and by night they would have faded peacefully away . (lpp_1943.371)

```
(a / and
      :op1 (a2 / appear-01
            :ARG1 (t / they)
            :time (d / date-entity
                  :dayperiod (m / morning)
                  :mod (o / one))
            :location (g / grass))
      :op2 (f / fade-01
            :ARG1 t
            :manner (p / peaceful)
            :time (b / by
                  :op1 (n / night))))
```
372. But one day , from a seed blown from no one knew where , a new flower had come up ; and the little prince had watched very closely over this small sprout which was not like any other small sprouts on his planet . (lpp_1943.372)

```
(a / and
      :op1 (c / contrast-01
            :ARG2 (c2 / come-up-13
                  :ARG1 (f / flower
                        :ARG1-of (n / new-01)
                        :source (s / seed
                              :ARG1-of (b / blow-01
                                    :source (a2 / amr-unknown))))
                  :time (d / day
                        :mod (o / one))))
      :op2 (w / watch-over-03
            :ARG0 (p / prince
                  :mod (l / little))
            :ARG1 (s2 / sprout
                  :mod (s3 / small)
                  :mod (t / this)
                  :ARG1-of (r / resemble-01 :polarity -
                        :ARG2 (s4 / sprout
                              :mod (s5 / small)
                              :mod (o2 / other
                                    :mod (a3 / any))
                              :location (p2 / planet
                                    :poss p))))
            :ARG1-of (c3 / close-10
                  :degree (v / very))))
```
373. It might , you see , have been a new kind of baobab . (lpp_1943.373)

```
(p / possible-01
      :ARG1 (b2 / baobab
            :mod (k / kind
                  :ARG1-of (n / new-01))
            :domain (i / it)))
```
374. The shrub soon stopped growing , and began to get ready to produce a flower . (lpp_1943.374)

```
(a / and
      :op1 (s / stop-01
            :ARG0 (s2 / shrub)
            :ARG1 (g / grow-01
                  :ARG1 s2)
            :time (s3 / soon))
      :op2 (b / begin-01
            :ARG0 s2
            :ARG1 (r / ready-01
                  :ARG0 s2
                  :ARG1 s2
                  :ARG2 (p / produce-01
                        :ARG0 s2
                        :ARG1 (f / flower)))))
```
375. The little prince , who was present at the first appearance of a huge bud , felt at once that some sort of miraculous apparition must emerge from it . (lpp_1943.375)

```
(f / feel-01
      :ARG0 (p / prince
            :mod (l / little)
            :ARG1-of (p2 / present-02
                  :ARG2 (a / appear-01
                        :ARG1 (b / bud
                              :mod (h / huge))
                        :ord (o2 / ordinal-entity :value 1))))
      :ARG1 (o / obligate-01
            :ARG2 (e / emerge-01
                  :ARG0 (t / thing
                        :ARG1-of (a4 / appear-01
                              :manner (m / miraculous))
                        :mod (s / sort))
                  :ARG1 b))
      :time (a2 / at-once))
```
376. But the flower was not satisfied to complete the preparations for her beauty in the shelter of her green chamber . (lpp_1943.376)

```
(c / contrast-01
      :ARG1 (s / satisfy-01 :polarity -
            :ARG0 (c2 / complete-01
                  :ARG0 f
                  :ARG1 (p / prepare-02
                        :ARG0 f
                        :ARG1 (b / beautiful-02
                              :ARG1 f))
                  :location (c3 / chamber
                        :ARG1-of (g / green-02)
                        :poss f
                        :ARG2-of (s2 / shelter-01)))
            :ARG1 (f / flower)))
```
377. She chose her colours with the greatest care . (lpp_1943.377)

```
(c / choose-01
      :ARG0 (s / she)
      :ARG1 (c2 / color
            :poss s)
      :manner (c3 / care-04
            :degree (g / great
                  :degree (m / most))))
```
378. She adjusted her petals one by one . (lpp_1943.378)

```
(a / adjust-01
  :ARG0 (s / she)
  :ARG1 (p / petal
          :poss s)
  :manner (o / one-by-one))
```
379. She did not wish to go out into the world all rumpled , like the field poppies . (lpp_1943.379)

```
(w / wish-01 :polarity -
      :ARG0 (s / she
            :ARG1-of (r / rumple-02
                  :mod (a / all))
            :ARG1-of (r2 / resemble-01
                  :ARG2 (p / poppy
                        :mod (f / field))))
      :ARG1 (g / go-out-17
            :ARG0 s
            :destination (w2 / world)))
```
380. It was only in the full radiance of her beauty that she wished to appear . (lpp_1943.380)

```
(w / wish-01
      :ARG0 (s / she)
      :ARG1 (a / appear-01
            :ARG1 s
            :manner (r / radiate-01
                  :ARG0 s
                  :ARG1 (b / beautiful-02
                        :ARG1 s)
                  :degree (f2 / full)
                  :mod (o / only))))
```
381. Oh , yes ! (lpp_1943.381)

```
(y / yes)
```
382. She was a coquettish creature ! (lpp_1943.382)

```
(r / resemble-01
      :ARG1 (s / she)
      :ARG2 (c / creature
            :mod (c2 / coquet)))
```
383. And her mysterious adornment lasted for days and days . (lpp_1943.383)

```
(a / and
      :op1 (l / last-01
            :ARG1 (t / thing
                  :ARG2-of (a2 / adorn-01
                        :ARG1 (s / she)
                        :mod (m / mysterious)))
            :ARG2 (m2 / multiple
                  :op1 (t2 / temporal-quantity :quant 1
                        :unit (d / day)))))
```
384. Then one morning , exactly at sunrise , she suddenly showed herself . (lpp_1943.384)

```
(s / show-01
      :ARG0 (s2 / she)
      :ARG1 s2
      :manner (s3 / sudden)
      :time (d / date-entity
            :dayperiod (m / morning)
            :mod (o / one))
      :time (s4 / sunrise
            :mod (e / exact))
      :time (t / then))
```
385. And , after working with all this painstaking precision , she yawned and said : " Ah ! (lpp_1943.385)

```
(a / and
      :op1 (y / yawn-01
            :ARG0 (s2 / she))
      :op2 (s / say-01
            :ARG0 s2
            :ARG1 (a2 / ah :mode expressive))
      :time (a3 / after
            :op1 (w / work-01
                  :ARG0 s2
                  :manner (p / precise
                        :degree (p2 / painstaking)
                        :mod (t / this)
                        :mod (a4 / all)))))
```
386. I am scarcely awake . (lpp_1943.386)

```
(a / awake-03
      :ARG1 (i / i)
      :degree (s / scarce))
```
387. I beg that you will excuse me . (lpp_1943.387)

```
(b2 / beg-01
      :ARG0 (i / i)
      :ARG1 (y2 / you)
      :ARG2 (e2 / excuse-01
            :ARG0 y2
            :ARG1 i))
```
388. My petals are still all disarranged ... " (lpp_1943.388)

```
(a3 / arrange-01 :polarity -
      :ARG1 (p2 / petal
            :part-of (i / i)
            :mod (a4 / all))
      :mod (s4 / still))
```
389. But the little prince could not restrain his admiration : " Oh ! (lpp_1943.389)

```
(c / contrast-01
      :ARG2 (p2 / possible-01 :polarity -
            :ARG1 (r / restrain-01
                  :ARG0 (p / prince
                        :mod (l / little)
                        :ARG0-of (s / say-01
                              :ARG1 (o / oh :mode "expressive")))
                  :ARG1 (a / admire-01
                        :ARG0 p))))
```
390. How beautiful you are ! " (lpp_1943.390)

```
(b / beautiful-02
      :ARG1 (y / you)
      :degree (s / so))
```
391. " Am I not ? " the flower responded , sweetly . (lpp_1943.391)

```
(r / respond-01
      :ARG0 (f / flower)
      :ARG1 (b / beautiful-02 :polarity - :mode interrogative
            :ARG1 f)
      :manner (s / sweet-03))
```
392. " And I was born at the same moment as the sun ... " (lpp_1943.392)

```
(a / and
      :op2 (b / bear-02
            :ARG1 (i / i)
            :time (m / moment
                  :ARG1-of (s / same-01
                        :ARG2 (s2 / sun)))))
```
393. The little prince could guess easily enough that she was not any too modest - - but how moving - - and exciting - - she was ! (lpp_1943.393)

```
(p / possible-01
      :ARG1 (g / guess-01
            :ARG0 (p2 / prince
                  :mod (l / little))
            :ARG1 (c / contrast-01
                  :ARG1 (m / modest :polarity -
                        :domain (s / she)
                        :degree (t / too))
                  :ARG2 (a2 / and
                        :op1 (m2 / move-05
                              :ARG0 s
                              :degree (s2 / so))
                        :op2 (e3 / excite-01
                              :ARG0 s
                              :degree (s3 / so))))
            :ARG1-of (e / easy-05
                  :mod (e2 / enough))))
```
394. " I think it is time for breakfast , " she added an instant later . (lpp_1943.394)

```
(a / add-01
      :ARG0 (s / she)
      :ARG1 (t / think-01
            :ARG0 s
            :ARG1 (t2 / time
                  :purpose (b / breakfast-01)))
      :time (l / late
            :degree (m / more
                  :quant (i / instant))))
```
395. " If you would have the kindness to think of my needs - - " (lpp_1943.395)

```
(t / think-01 :mode imperative
      :ARG0 (y / you)
      :ARG1 (t2 / thing
            :ARG1-of (n / need-01
                  :ARG0 (i / i)))
      :ARG1-of (k2 / kind-01
            :ARG0 y
            :ARG2 i))
```
396. And the little prince , completely abashed , went to look for a sprinkling - can of fresh water . (lpp_1943.396)

```
(a / and
      :op1 (g / go-05
            :ARG0 (p / prince
                  :mod (l2 / little)
                  :ARG1-of (a2 / abash-01
                        :ARG1-of (c3 / complete-02)))
            :ARG1 (l / look-01
                  :ARG0 p
                  :ARG1 (c / can
                        :ARG0-of (s / sprinkle-01)
                        :ARG0-of (c2 / contain-01
                              :ARG1 (w / water
                                    :ARG1-of (f / fresh-04)))))))
```
397. So , he tended the flower . (lpp_1943.397)

```
(t / tend-01
      :ARG0 (h / he)
      :ARG1 (f / flower)
      :ARG1-of (c / cause-01))
```
398. So , too , she began very quickly to torment him with her vanity - - which was , if the truth be known , a little difficult to deal with . (lpp_1943.398)

```
(b / begin-01
      :ARG0 (s / she)
      :ARG1 (t2 / torment-01
            :ARG0 s
            :ARG1 (h / he)
            :ARG2 (v2 / vanity
                  :poss s
                  :ARG2-of (d3 / deal-01
                        :ARG0 h
                        :mod (d / difficult
                              :degree (l / little))
                        :condition (k / know-01
                              :ARG1 (t3 / truth)))))
      :mod (t / too)
      :ARG1-of (q / quick-02
            :degree (v / very)))
```
399. One day , for instance , when she was speaking of her four thorns , she said to the little prince : " Let the tigers come with their claws ! " (lpp_1943.399)

```
(s / say-01
      :ARG0 (s2 / she)
      :ARG1 (c / come-01 :mode imperative
            :ARG1 (t / tiger)
            :accompanier (c2 / claw
                  :part-of t))
      :ARG2 (p / prince
            :mod (l / little))
      :time (d / day
            :mod (o / one))
      :ARG0-of (e / exemplify-01)
      :time (s3 / speak-01
            :ARG0 s2
            :ARG1 (t2 / thorn :quant 4
                  :part-of s2)))
```
400. " There are no tigers on my planet , " the little prince objected . (lpp_1943.400)

```
(o / object-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (t / tiger :polarity -
            :location (p2 / planet
                  :poss p)))
```
401. " And , anyway , tigers do not eat weeds . " (lpp_1943.401)

```
(a / and
      :op2 (e / eat-01 :polarity -
            :ARG0 (t / tiger)
            :ARG1 (w / weed)
            :mod (a2 / anyway)))
```
402. " I am not a weed , " the flower replied , sweetly . (lpp_1943.402)

```
(r / reply-01
      :ARG0 (f / flower)
      :ARG2 (w / weed :polarity -
            :domain f)
      :manner (s / sweet-03))
```
403. " Please excuse me ... " (lpp_1943.403)

```
(e / excuse-01 :mode imperative :polite +
      :ARG0 (y / you)
      :ARG1 (i / i))
```
404. " I am not at all afraid of tigers , " she went on , " but I have a horror of drafts . (lpp_1943.404)

```
(g / go-on-25
      :ARG0 (s / she)
      :ARG1 (c / contrast-01
            :ARG1 (f / fear-01 :polarity -
                  :ARG0 s
                  :ARG1 (t / tiger)
                  :degree (a / at-all))
            :ARG2 (a2 / abhor-01
                  :ARG0 s
                  :ARG1 (d / draft))))
```
405. I suppose you would n't have a screen for me ? " (lpp_1943.405)

```
(s / suppose-01
      :ARG0 (i / i)
      :ARG1 (h / have-03 :polarity - :mode interrogative
            :ARG0 (y / you)
            :ARG1 (s2 / screen)
            :beneficiary i))
```
406. " A horror of drafts - - that is bad luck , for a plant , " remarked the little prince , and added to himself , " This flower is a very complex creature ... " (lpp_1943.406)

```
(a / and
      :op1 (r / remark-01
            :ARG0 (p / prince
                  :mod (l / little))
            :ARG1 (l2 / luck
                  :ARG1-of (b / bad-07)
                  :beneficiary (p2 / plant)
                  :domain (a3 / abhor-01
                        :ARG1 (d / draft))))
      :op2 (a2 / add-01
            :ARG0 p
            :ARG1 (c3 / creature
                  :mod (c2 / complex
                        :degree (v / very))
                  :domain (f / flower
                        :mod (t / this)))
            :beneficiary p))
```
407. " At night I want you to put me under a glass globe . (lpp_1943.407)

```
(w / want-01
      :ARG0 (i / i)
      :ARG1 (p / put-01
            :ARG0 (y / you)
            :ARG1 i
            :ARG2 (u / under
                  :op1 (g / globe
                        :consist-of (g2 / glass)))
            :time (d / date-entity :dayperiod (n / night))))
```
408. It is very cold where you live . (lpp_1943.408)

```
(c / cold-01
      :degree (v / very)
      :location (l / live-01
            :ARG0 (y / you)))
```
409. In the place I came from - - " (lpp_1943.409)

```
(l / location
      :ARG3-of (c / come-01
            :ARG1 (i / i)))
```
410. But she interrupted herself at that point . (lpp_1943.410)

```
(c / contrast-01
      :ARG2 (i / interrupt-01
            :ARG0 (s / she)
            :ARG1 s
            :time (p / point
                  :mod (t / that))))
```
411. She had come in the form of a seed . (lpp_1943.411)

```
(c / come-01
      :ARG1 (s / she)
      :time-of (s2 / seed
            :domain s))
```
412. She could not have known anything of any other worlds . (lpp_1943.412)

```
(p / possible-01
  :polarity -
  :ARG1 (k / know-01
            :ARG0 (s / she)
            :ARG1 (a / anything
                    :topic (w / world
                             :mod (o / other
                                    :mod (a2 / any))))))
```
413. Embarassed over having let herself be caught on the verge of such a naïve untruth , she coughed two or three times , in order to put the little prince in the wrong . (lpp_1943.413)

```
(c / cough-01
      :ARG0 (s / she
            :ARG1-of (e / embarrass-01
                  :ARG0 (l2 / let-01
                        :ARG0 s
                        :ARG1 (c2 / catch-03
                              :ARG1 s
                              :ARG2 (v / verge-01
                                    :ARG1 (t / truth :polarity -
                                          :mod (n / naive
                                                :degree (s2 / such))))))))
      :purpose (p / put-03
            :ARG0 s
            :ARG1 (p2 / prince
                  :mod (l / little))
            :ARG2 (w / wrong-04
                  :ARG1 p2))
      :frequency (o / or :op1 2 :op2 3))
```
414. " The screen ? " (lpp_1943.414)

```
(s / screen :mode interrogative)
```
415. " I was just going to look for it when you spoke to me ... " (lpp_1943.415)

```
(l3 / look-01
      :ARG0 (i / i)
      :ARG1 (i2 / it)
      :time (s3 / speak-01
            :ARG0 (y2 / you)
            :ARG2 i))
```
416. Then she forced her cough a little more so that he should suffer from remorse just the same . (lpp_1943.416)

```
(f / force-02
      :ARG0 (s / she)
      :ARG1 (c / cough-01
            :ARG0 s)
      :time (t / then)
      :degree (m / more
            :degree (l / little))
      :purpose (s2 / suffer-01
            :ARG0 (h / he)
            :ARG1 (r / remorse)
            :ARG1-of (h2 / have-concession-91)))
```
417. So the little prince , in spite of all the good will that was inseparable from his love , had soon come to doubt her . (lpp_1943.417)

```
(c / come-04
      :ARG1 (p / prince
            :mod (l / little))
      :ARG2 (d / doubt-01
            :ARG0 p
            :ARG1 (s3 / she))
      :time (s / soon)
      :ARG1-of (c2 / cause-01)
      :concession (w / will
            :ARG1-of (g / good-02)
            :mod (a / all)
            :ARG1-of (s2 / separate-01
                  :ARG2 (l2 / love-01
                        :ARG0 p)
                  :ARG1-of (p2 / possible-01 :polarity -))))
```
418. He had taken seriously words which were without importance , and it made him very unhappy . (lpp_1943.418)

```
(s / serious-01
      :ARG1 (h / he)
      :ARG2 (w / word-01
            :mod (i / important :polarity -))
      :ARG0-of (m / make-02
            :ARG1 (h2 / happy-01 :polarity -
                  :ARG1 h
                  :degree (v / very))))
```
419. " I ought not to have listened to her , " he confided to me one day . " (lpp_1943.419)

```
(c / confide-01
  :ARG0 (h / he)
  :ARG1 (r / recommend-01
          :ARG1 (l / listen-01
                  :ARG0 h
                  :ARG1 (s / she)
                  :polarity -)
          :ARG2 h)
  :ARG2 (i / i)
  :time (d / day
          :mod (o / one)))
```
420. One never ought to listen to the flowers . (lpp_1943.420)

```
(r / recommend-01
      :ARG1 (l / listen-01 :polarity -
            :ARG0 (o2 / one)
            :ARG1 (f / flower)
            :time (e / ever)))
```
421. One should simply look at them and breathe their fragrance . (lpp_1943.421)

```
(r / recommend-01
      :ARG1 (a / and
            :op1 (l / look-01
                  :ARG0 (o2 / one)
                  :ARG1 (t / they)
                  :manner (s / simple))
            :op2 (b / breathe-01
                  :ARG0 o2
                  :ARG1 (f / fragrance
                        :poss t))))
```
422. Mine perfumed all my planet . (lpp_1943.422)

```
(p / perfume-01
      :ARG0 (t / thing
            :poss (i / i))
      :ARG1 (p2 / planet
            :mod (a / all)
            :poss i))
```
423. But I did not know how to take pleasure in all her grace . (lpp_1943.423)

```
(c / contrast-01
      :ARG2 (k / know-01 :polarity -
            :ARG0 (i / i)
            :manner (p2 / please-01
                  :ARG0 (g / grace
                        :poss (s / she)
                        :mod (a / all))
                  :ARG1 i)))
```
424. This tale of claws , which disturbed me so much , should only have filled my heart with tenderness and pity . " (lpp_1943.424)

```
(r2 / recommend-01
      :ARG1 (f / fill-01
            :ARG0 (t2 / tale
                  :topic (c / claws)
                  :ARG0-of (d / disturb-01
                        :ARG1 (i / i)
                        :degree (m / much
                              :degree (s / so)))
                  :mod (t3 / this))
            :ARG1 (h / heart
                  :part-of i)
            :ARG2 (a / and
                  :op1 (t / tender)
                  :op2 (p / pity-01))
            :mod (o / only)))
```
425. And he continued his confidences : " The fact is that I did not know how to understand anything ! (lpp_1943.425)

```
(a / and
      :op1 (c / continue-02
            :ARG0 (h / he)
            :ARG1 (c2 / confide-01
                  :ARG0 h
                  :ARG1 (k / know-01 :polarity -
                        :ARG0 h
                        :ARG1 (t / thing
                              :manner-of (u / understand-01
                                    :ARG0 h
                                    :ARG1 (a2 / anything)))))))
```
426. I ought to have judged by deeds and not by words . (lpp_1943.426)

```
(r2 / recommend-01
      :ARG1 (a2 / and
            :op1 (j / judge-01
                  :ARG0 (i / i)
                  :ARG3 (d / do-02))
            :op2 (j2 / judge-01 :polarity -
                  :ARG0 i
                  :ARG3 (w / word))))
```
427. She cast her fragrance and her radiance over me . (lpp_1943.427)

```
(c / cast-01
      :ARG0 (s / she)
      :ARG1 (a / and
            :op1 (f / fragrance
                  :poss s)
            :op2 (t / thing
                  :ARG1-of (r / radiate-01
                        :ARG0 s)))
      :ARG2 (i / i))
```
428. I ought never to have run away from her ... (lpp_1943.428)

```
(r / recommend-01
      :ARG1 (r2 / run-02 :polarity -
            :ARG0 (i / i)
            :time (e / ever)
            :direction (a2 / away
                  :op1 (s / she))))
```
429. I ought to have guessed all the affection that lay behind her poor little strategems . (lpp_1943.429)

```
(r / recommend-01
      :ARG1 (g / guess-01
            :ARG0 (i / i)
            :ARG1 (a / affection
                  :mod (a2 / all)
                  :ARG1-of (l / lie-07
                        :ARG2 (b / behind
                              :op1 (s / strategem
                                    :mod (l2 / little)
                                    :mod (p / poor)
                                    :poss (s2 / she)))))))
```
430. Flowers are so inconsistent ! (lpp_1943.430)

```
(c / consistent-01 :polarity -
      :ARG1 (f / flower)
      :degree (s / so))
```
431. But I was too young to know how to love her ... " (lpp_1943.431)

```
(c / contrast-01
      :ARG2 (y / young
            :degree (t / too)
            :domain (i / i)
            :compared-to (k / know-01
                  :ARG0 i
                  :ARG1 (m / manner
                        :manner-of (l / love-01
                              :ARG0 i
                              :ARG1 (s / she))))))
```
432. Chapter 9 . (lpp_1943.432)

```
(c / chapter :mod 9)
```
433. I believe that for his escape he took advantage of the migration of a flock of wild birds . (lpp_1943.433)

```
(b / believe-01
  :ARG0 (i / i)
  :ARG1 (t / take-01
          :ARG0 (h / he)
          :ARG1 (a / advantage)
          :ARG2 (m / migrate-01
                  :ARG0 (f / flock-02
                          :ARG0 (b2 / bird
                                  :mod (w / wild))))
          :purpose (e / escape-01
                     :ARG0 h)))
```
434. On the morning of his departure he put his planet in perfect order . (lpp_1943.434)

```
(o / order-03
      :ARG0 (h / he)
      :ARG1 (p2 / planet
            :poss h)
      :ARG1-of (p / perfect-02)
      :time (d2 / date-entity
            :dayperiod (m / morning)
            :time-of (d / depart-01
                  :ARG0 h)))
```
435. He carefully cleaned out his active volcanoes . (lpp_1943.435)

```
(c / clean-out-03
      :ARG0 (h / he)
      :ARG1 (v / volcano
            :poss h
            :ARG0-of (a / activity-06))
      :manner (c2 / careful))
```
436. He possessed two active volcanoes ; and they were very convenient for heating his breakfast in the morning . (lpp_1943.436)

```
(a / and
      :op1 (p / possess-01
            :ARG0 (h / he)
            :ARG1 (v / volcano :quant 2
                  :ARG0-of (a2 / activity-06)))
      :op2 (c / convenient
            :degree (v2 / very)
            :purpose (h2 / heat-01
                  :ARG1 (f / food
                        :ARG1-of (b2 / breakfast-01
                              :ARG0 h))
                  :ARG2 v
                  :time (d / date-entity :dayperiod (m / morning)))
            :domain v))
```
437. He also had one volcano that was extinct . (lpp_1943.437)

```
(h / have-03
  :ARG0 (h2 / he)
  :ARG1 (v / volcano
          :mod (e / extinct)
          :quant 1)
  :mod (a / also))
```
438. But , as he said , " One never knows ! " (lpp_1943.438)

```
(c / contrast-01
      :ARG2 (s / say-01
            :ARG0 (h / he)
            :ARG1 (k / know-01 :polarity -
                  :ARG0 (o / one))))
```
439. So he cleaned out the extinct volcano , too . (lpp_1943.439)

```
(c / clean-out-03
      :ARG0 (h / he)
      :ARG1 (v / volcano
            :mod (e / extinct))
      :mod (t / too))
```
440. If they are well cleaned out , volcanoes burn slowly and steadily , without any eruptions . (lpp_1943.440)

```
(b / burn-01
      :ARG1 (v / volcano
            :ARG1-of (e2 / erupt-01 :polarity -))
      :condition (c / clean-out-03
            :ARG1 v
            :degree (w / well))
      :manner (s3 / steady)
      :ARG1-of (s / slow-05))
```
441. Volcanic eruptions are like fires in a chimney . (lpp_1943.441)

```
(e / erupt-01
      :ARG1 (v / volcano)
      :ARG1-of (r / resemble-01
            :ARG2 (f / fire
                  :location (c / chimney))))
```
442. On our earth we are obviously much too small to clean out our volcanoes . (lpp_1943.442)

```
(s / small
      :degree (t2 / too
            :degree (m / much))
      :compared-to (c / clean-out-03
            :ARG0 w
            :ARG1 (v / volcano
                  :poss w))
      :domain (w / we)
      :location (e / earth
            :poss w)
      :ARG1-of (o / obvious-01))
```
443. That is why they bring no end of trouble upon us . (lpp_1943.443)

```
(c / cause-01
      :ARG0 (t3 / that)
      :ARG1 (t2 / trouble-01
            :ARG0 (t4 / they)
            :ARG1 (w / we)
            :quant (e / end :polarity -)))
```
444. The little prince also pulled up , with a certain sense of dejection , the last little shoots of the baobabs . (lpp_1943.444)

```
(p / pull-01
      :ARG0 (p2 / prince
            :mod (l / little)
            :ARG0-of (s2 / sense-01
                  :ARG1 (d2 / deject-01)
                  :mod (c / certain)))
      :ARG1 (s / shoot
            :part-of (b / baobab)
            :mod (l2 / little)
            :ord (o / ordinal-entity :value "-1"))
      :mod (a / also)
      :direction (u / up))
```
445. He believed that he would never want to return . (lpp_1943.445)

```
(b / believe-01
      :ARG0 (h / he)
      :ARG1 (w / want-01 :polarity -
            :ARG0 h
            :ARG1 (r / return-01
                  :ARG1 h)
            :time (e / ever)))
```
446. But on this last morning all these familiar tasks seemed very precious to him . (lpp_1943.446)

```
(c / contrast-01
      :ARG2 (s / seem-01
            :ARG1 (p / precious
                  :degree (v / very)
                  :domain (t2 / task
                        :mod (a2 / all)
                        :mod (f / familiar)))
            :ARG2 (h / he)
            :time (d / date-entity
                  :dayperiod (m / morning)
                  :mod (t / this)
                  :ord (o / ordinal-entity :value "-1"))))
```
447. And when he watered the flower for the last time , and prepared to place her under the shelter of her glass globe , he realised that he was very close to tears . (lpp_1943.447)

```
(r / realize-01
      :ARG0 (h / he)
      :ARG1 (c / close-10
            :ARG1 h
            :ARG2 (t / tear-03
                  :ARG1 h)
            :degree (v / very))
      :time (a / and
            :op1 (w / water-01
                  :ARG0 h
                  :ARG1 (f / flower-01)
                  :ord (o / ordinal-entity :value "-1"))
            :op2 (p / prepare-02
                  :ARG0 h
                  :ARG1 h
                  :ARG2 (p2 / place-01
                        :ARG0 h
                        :ARG1 f
                        :ARG2 (u2 / under
                              :op1 (g / globe
                                    :consist-of (g2 / glass)
                                    :poss f
                                    :ARG2-of (s2 / shelter-01
                                          :ARG0 h
                                          :ARG1 f)))))))
```
448. " Goodbye , " he said to the flower . (lpp_1943.448)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (g / goodbye)
      :ARG2 (f / flower))
```
449. But she made no answer . (lpp_1943.449)

```
(c / contrast-01
      :ARG2 (a2 / answer-01 :polarity -
            :ARG0 (s / she)))
```
450. " Goodbye , " he said again . (lpp_1943.450)

```
(s / say-01
  :ARG0 (h / he)
  :ARG1 (g / goodbye)
  :mod (a / again))
```
451. The flower coughed . (lpp_1943.451)

```
(c / cough-01
      :ARG0 (f / flower))
```
452. But it was not because she had a cold . (lpp_1943.452)

```
(c2 / contrast-01
      :ARG2 (c3 / cause-01 :polarity -
            :ARG0 (h / have-03
                  :ARG0 (s / she)
                  :ARG1 (c / cold))
            :ARG1 (i / it)))
```
453. " I have been silly , " she said to him , at last . (lpp_1943.453)

```
(s / say-01
      :ARG0 (s2 / she)
      :ARG1 (s4 / silly
            :domain s2)
      :ARG2 (h / he)
      :time (a / at-last))
```
454. " I ask your forgiveness . (lpp_1943.454)

```
(a / ask-02
      :ARG0 (i / i)
      :ARG1 (f / forgive-01
            :ARG0 y
            :ARG1 i)
      :ARG2 (y / you))
```
455. Try to be happy ... " (lpp_1943.455)

```
(t / try-01 :mode imperative
      :ARG0 (y / you)
      :ARG1 (h / happy-01
            :ARG1 y))
```
456. He was surprised by this absence of reproaches . (lpp_1943.456)

```
(s / surprise-01
      :ARG0 (a / absent-01
            :ARG1 (r / reproach-01))
      :ARG1 (h / he))
```
457. He stood there all bewildered , the glass globe held arrested in mid - air . (lpp_1943.457)

```
(s / stand-01
      :ARG1 (h / he
            :ARG1-of (b / bewilder-01
                  :degree (a / all))
            :ARG0-of (h2 / hold-01
                  :ARG1 (g / globe
                        :consist-of (g2 / glass)
                        :ARG1-of (a2 / arrest-02
                              :location (m / midair)))))
      :ARG2 (t / there))
```
458. He did not understand this quiet sweetness . (lpp_1943.458)

```
(u / understand-01 :polarity -
      :ARG0 (h / he)
      :ARG1 (s / sweet-05
            :ARG1 (t / this)
            :ARG1-of (q / quiet-04)))
```
459. " Of course I love you , " the flower said to him . (lpp_1943.459)

```
(s / say-01
  :ARG0 (f / flower-01)
  :ARG1 (l / love-01
          :ARG0 f
          :ARG1 h
          :mod (o / of-course))
  :ARG2 (h / he))
```
460. " It is my fault that you have not known it all the while . (lpp_1943.460)

```
(f / fault-01
      :ARG1 (i3 / i)
      :ARG2 (k / know-01 :polarity -
            :ARG0 (y / you)
            :ARG1 (i2 / it)
            :time (w / while-away-01
                  :duration (a / all))))
```
461. That is of no importance . (lpp_1943.461)

```
(i / important :polarity -
      :domain (t / that))
```
462. But you - - you have been just as foolish as I . (lpp_1943.462)

```
(c / contrast-01
      :ARG2 (f / foolish
            :domain (y / you)
            :degree (e / equal)
            :compared-to (i / i)))
```
463. Try to be happy ... let the glass globe be . (lpp_1943.463)

```
(a / and
      :op1 (t / try-01 :mode imperative
            :ARG0 (y / you)
            :ARG1 (h / happy-01
                  :ARG1 y))
      :op2 (l / leave-14 :mode imperative
            :ARG0 y
            :ARG1 (a2 / alone
                  :domain (g / globe
                        :consist-of (g2 / glass)))))
```
464. I do n't want it any more . " (lpp_1943.464)

```
(w / want-01
  :ARG0 (i / i)
  :ARG1 (i2 / it)
  :polarity -
  :time (a / anymore))
```
465. " But the wind - - " (lpp_1943.465)

```
(c / contrast-01
  :ARG2 (w / wind))
```
466. " My cold is not so bad as all that ... the cool night air will do me good . (lpp_1943.466)

```
(a / and
      :op1 (b / bad-05 :polarity -
            :ARG1 (c3 / cold
                  :poss (i / i))
            :compared-to (t / that
                  :mod (a2 / all)))
      :op2 (g / good-04
            :ARG1 (a3 / air
                  :ARG1-of (c / cool-06)
                  :mod (n / night))
            :ARG2 i))
```
467. I am a flower . " (lpp_1943.467)

```
(f / flower
      :domain (i / i))
```
468. " But the animals - - " (lpp_1943.468)

```
(c / contrast-01
  :ARG2 (a / animal))
```
469. " Well , I must endure the presence of two or three caterpillars if I wish to become acquainted with the butterflies . (lpp_1943.469)

```
(h / have-concession-91
      :ARG2 (o / obligate-01
            :ARG1 i
            :ARG2 (e / endure-01
                  :ARG1 (i / i)
                  :ARG2 (p / present-02
                        :ARG1 (c / caterpillar
                              :quant (o2 / or :op1 2 :op2 3)))
                  :condition (w / wish-01
                        :ARG0 i
                        :ARG1 (a / acquaint-01
                              :ARG1 i
                              :ARG2 (b2 / butterfly))))))
```
470. It seems that they are very beautiful . (lpp_1943.470)

```
(s / seem-01
      :ARG1 (b / beautiful-02
            :ARG1 (t2 / they)
            :degree (v2 / very)))
```
471. And if not the butterflies - - and the caterpillars - - who will call upon me ? (lpp_1943.471)

```
(c / call-on-05
      :ARG0 (a / amr-unknown)
      :ARG1 (i / i)
      :condition (c3 / call-on-05 :polarity -
            :ARG0 (a2 / and
                  :op1 (b / butterfly)
                  :op2 (c2 / caterpillar))
            :ARG1 i))
```
472. You will be far away ... as for the large animals - - I am not at all afraid of any of them . (lpp_1943.472)

```
(a / and
      :op1 (a2 / away
            :extent (f / far)
            :location-of (y / you))
      :op2 (f2 / fear-01 :polarity -
            :ARG0 (i / i)
            :ARG1 (a3 / animal
                  :mod (l / large)
                  :quant (a4 / any))
            :degree (a5 / at-all)))
```
473. I have my claws . " (lpp_1943.473)

```
(h / have-03
      :ARG0 (i / i)
      :ARG1 (c / claw
            :part-of i))
```
474. And , naïvely , she showed her four thorns . (lpp_1943.474)

```
(s / show-01
      :ARG0 (s2 / she)
      :ARG1 (t / thorn :quant 4
            :part-of s2)
      :manner (n / naive))
```
475. Then she added : " Do n't linger like this . (lpp_1943.475)

```
(a / add-01
      :ARG0 (s / she)
      :ARG1 (l / linger-01 :polarity - :mode imperative
            :ARG1 (y / you)
            :compared-to (t3 / this))
      :time (t / then))
```
476. You have decided to go away . (lpp_1943.476)

```
(d / decide-01
      :ARG0 (y / you)
      :ARG1 (g / go-02
            :ARG0 y
            :direction (a / away)))
```
477. Now go ! " (lpp_1943.477)

```
(g / go-02 :mode imperative
      :ARG0 (y / you)
      :time (n / now))
```
478. For she did not want him to see her crying . (lpp_1943.478)

```
(w / want-01 :polarity -
      :ARG0 (s / she)
      :ARG1 (s2 / see-01
            :ARG0 (h / he)
            :ARG1 (c / cry-02
                  :ARG0 s)))
```
479. She was such a proud flower ... (lpp_1943.479)

```
(p / pride-01
      :ARG0 (f2 / flower
            :domain (s / she))
      :degree (s2 / such))
```
480. Chapter 10 . (lpp_1943.480)

```
(c / chapter :mod 10)
```
481. He found himself in the neighborhood of the asteroids 325 , 326 , 327 , 328 , 329 , and 330 . (lpp_1943.481)

```
(f / find-out-03
      :ARG0 (h / he)
      :ARG1 (b / be-located-at-91
            :ARG1 h
            :ARG2 (n / neighborhood
                  :location-of (a3 / and
                        :op1 (a4 / asteroid :wiki -
                              :name (n2 / name :op1 325))
                        :op2 (a5 / asteroid :wiki -
                              :name (n3 / name :op1 326))
                        :op3 (a6 / asteroid :wiki -
                              :name (n4 / name :op1 327))
                        :op4 (a7 / asteroid :wiki -
                              :name (n5 / name :op1 328))
                        :op5 (a8 / asteroid :wiki -
                              :name (n6 / name :op1 329))
                        :op6 (a9 / asteroid :wiki -
                              :name (n7 / name :op1 330))))))
```
482. He began , therefore , by visiting them , in order to add to his knowledge . (lpp_1943.482)

```
(b / begin-01
      :ARG0 (h / he)
      :ARG2 (v / visit-01
            :ARG0 h
            :ARG1 (t2 / they))
      :mod (t / therefore)
      :purpose (a / add-02
            :ARG0 v
            :ARG2 (k / knowledge
                  :poss h)))
```
483. The first of them was inhabited by a king . (lpp_1943.483)

```
(i / inhabit-01
      :ARG0 (k / king)
      :ARG1 (t2 / thing
            :ord (o / ordinal-entity :value 1)
            :ARG1-of (i2 / include-91
                  :ARG2 (t / they))))
```
484. Clad in royal purple and ermine , he was seated upon a throne which was at the same time both simple and majestic . (lpp_1943.484)

```
(s / seat-01
      :ARG1 (h / he
            :ARG1-of (c / clad-01
                  :ARG2 (a / and
                        :op1 (p / purple-02
                              :mod (r / royal))
                        :op2 (e / ermine))))
      :ARG2 (t / throne
            :ARG1-of (s2 / simple-02)
            :mod (m / majesty)))
```
485. " Ah ! (lpp_1943.485)

```
(a2 / ah :mode expressive)
```
486. Here is a subject , " exclaimed the king , when he saw the little prince coming . (lpp_1943.486)

```
(e / exclaim-01
      :ARG0 (k / king)
      :ARG1 (h2 / here
            :location-of (s / subject))
      :time (s2 / see-01
            :ARG0 k
            :ARG1 (p / prince
                  :mod (l / little)
                  :ARG1-of (c / come-01))))
```
487. And the little prince asked himself : " How could he recognize me when he had never seen me before ? " (lpp_1943.487)

```
(a / ask-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (p2 / possible-01
            :ARG1 (r / recognize-02
                  :ARG0 (h / he)
                  :ARG1 p
                  :condition (s / see-01 :polarity -
                        :ARG0 h
                        :ARG1 p
                        :time (b / before)
                        :time (e / ever)))
            :manner (a2 / amr-unknown))
      :ARG2 p)
```
488. He did not know how the world is simplified for kings . (lpp_1943.488)

```
(k / know-01
  :ARG0 (h / he)
  :ARG1 (s / simplify-01
          :ARG1 (w / world)
          :beneficiary (k2 / king))
  :polarity -)
```
489. To them , all men are subjects . (lpp_1943.489)

```
(o / opine-01
      :ARG0 (t2 / they)
      :ARG1 (s2 / subject
            :domain (m2 / man
                  :mod (a2 / all))))
```
490. " Approach , so that I may see you better , " said the king , who felt consumingly proud of being at last a king over somebody . (lpp_1943.490)

```
(s / say-01
      :ARG0 (k / king
            :ARG0-of (p / pride-01
                  :ARG2 (r / reign-01
                        :ARG0 k
                        :ARG1 (s3 / somebody)
                        :time (a2 / at-last))))
      :ARG1 (a / approach-01 :mode imperative
            :ARG1 y
            :purpose (s2 / see-01
                  :ARG0 k
                  :ARG1 (y / you)
                  :manner (w / well
                        :degree (m / more)))))
```
491. The little prince looked everywhere to find a place to sit down ; but the entire planet was crammed and obstructed by the king 's magnificent ermine robe . (lpp_1943.491)

```
(a / and
      :op1 (c / cram-01
            :ARG1 (r2 / robe
                  :mod (e2 / ermine)
                  :mod (m / magnificent)
                  :poss (k / king))
            :ARG2 (p3 / planet
                  :extent (e3 / entire)))
      :op2 (o / obstruct-01
            :ARG0 r2
            :ARG1 p3)
      :concession (l / look-01
            :ARG0 (p / prince
                  :mod (l2 / little))
            :ARG1 (p2 / place
                  :purpose (s / sit-down-02
                        :ARG1 p))
            :location (e / everywhere)))
```
492. So he remained standing upright , and , since he was tired , he yawned . (lpp_1943.492)

```
(a / and
  :op1 (r / remain-01
         :ARG1 (h / he)
         :ARG3 (s / stand-01
                 :ARG1 h
                 :manner (u / upright)))
  :op2 (y / yawn-01
         :ARG0 h
         :ARG1-of (c / cause-01
                    :ARG0 (t / tire-01
                            :ARG1 h))))
```
493. " It is contrary to etiquette to yawn in the presence of a king , " the monarch said to him . (lpp_1943.493)

```
(s / say-01
      :ARG0 (m / monarch)
      :ARG1 (c / contrary-01
            :ARG1 (y / yawn-01
                  :location (k / king))
            :ARG2 (e / etiquette))
      :ARG2 (h / he))
```
494. " I forbid you to do so . " (lpp_1943.494)

```
(f / forbid-01
      :ARG0 (i / i)
      :ARG1 (d / do-02
            :ARG0 y
            :ARG1 (s / so))
      :ARG2 (y / you))
```
495. " I can n't help it . (lpp_1943.495)

```
(p / possible-01 :polarity -
      :ARG1 (h / help-02
            :ARG0 (i / i)
            :ARG1 (i2 / it)))
```
496. I can n't stop myself , " replied the little prince , thoroughly embarrassed . (lpp_1943.496)

```
(r / reply-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG2 (p2 / possible-01 :polarity -
            :ARG1 (s / stop-01
                  :ARG0 p
                  :ARG1 p))
      :manner (e / embarrass-01
            :ARG1 p
            :degree (t / thorough)))
```
497. " I have come on a long journey , and I have had no sleep ... " (lpp_1943.497)

```
(a / and
      :op1 (c / come-01
            :ARG1 (i / i)
            :ARG2 (j / journey-01
                  :ARG0 i
                  :ARG1-of (l / long-03)))
      :op2 (s / sleep-01 :polarity -
            :ARG0 i))
```
498. " Ah , then , " the king said . (lpp_1943.498)

```
(s / say-01
      :ARG0 (k / king)
      :ARG1 (a / ah :mode expressive
            :mod (t / then)))
```
499. " I order you to yawn . (lpp_1943.499)

```
(o / order-01
      :ARG0 (i / i)
      :ARG1 (y / you)
      :ARG2 (y2 / yawn-01
            :ARG0 y))
```
500. It is years since I have seen anyone yawning . (lpp_1943.500)

```
(p / pass-03
      :ARG1 (y3 / year)
      :time (s3 / since
            :op1 (s / see-01
                  :ARG0 (i / i)
                  :ARG1 (a / anyone
                        :ARG0-of (y / yawn-01)))))
```
501. Yawns , to me , are objects of curiosity . (lpp_1943.501)

```
(c2 / curious-01
      :ARG0 (y2 / yawn-01)
      :ARG1 (i / i))
```
502. Come , now ! (lpp_1943.502)

```
(c / come-01
  :ARG1 (y / you)
  :time (n / now)
  :mode imperative)
```
503. Yawn again ! (lpp_1943.503)

```
(y / yawn-01 :mode imperative
      :ARG0 (y2 / you)
      :mod (a / again))
```
504. It is an order . " (lpp_1943.504)

```
(o2 / order-01
      :ARG2 (i2 / it))
```
505. " That frightens me ... (lpp_1943.505)

```
(f / frighten-01
  :ARG0 (t / that)
  :ARG1 (i / i))
```
506. I can not , any more ... " murmured the little prince , now completely abashed . (lpp_1943.506)

```
(m / murmur-01
      :ARG0 (p / prince
            :mod (l / little)
            :ARG1-of (a2 / abash-01
                  :ARG1-of (c / complete-02)
                  :time (n / now)))
      :ARG1 (p2 / possible-01 :polarity -
            :time (a / anymore)))
```
507. " Hum ! (lpp_1943.507)

```
(h / hum :mode expressive)
```
508. Hum ! " replied the king . (lpp_1943.508)

```
(r / reply-01
      :ARG0 (k / king)
      :ARG2 (h / hum :mode expressive))
```
509. " Then I - - I order you sometimes to yawn and sometimes to - - " (lpp_1943.509)

```
(o / order-01
      :ARG0 (i / i)
      :ARG1 (y / you)
      :ARG2 (a / and
            :op1 (y2 / yawn-01
                  :ARG0 y
                  :frequency (s / sometimes))
            :op2 (d / do-02
                  :frequency (s2 / sometimes)))
      :mod (t2 / then))
```
510. He sputtered a little , and seemed vexed . (lpp_1943.510)

```
(a / and
  :op1 (s / sputter-01
         :ARG0 (h / he)
         :degree (l / little))
  :op2 (s2 / seem-01
         :ARG1 (v / vex-01
                 :ARG1 h)))
```
511. For what the king fundamentally insisted upon was that his authority should be respected . (lpp_1943.511)

```
(i / insist-01
  :ARG0 (k / king)
  :ARG1 (r / respect-01
          :ARG1 (a / authority
                  :poss k))
  :mod (f / fundamental))
```
512. He tolerated no disobedience . (lpp_1943.512)

```
(t / tolerate-01
  :ARG0 (h / he)
  :ARG1 (d / disobey-01
          :ARG1 h)
  :polarity -)
```
513. He was an absolute monarch . (lpp_1943.513)

```
(m / monarch
      :mod (a / absolute)
      :domain (h2 / he))
```
514. But , because he was a very good man , he made his orders reasonable . (lpp_1943.514)

```
(h3 / have-concession-91
      :ARG1 (m / make-02
            :ARG0 (h / he)
            :ARG1 (r / reasonable-02
                  :ARG1 (t / thing
                        :ARG2-of (o / order-01)))
            :ARG1-of (c2 / cause-01
                  :ARG0 (m2 / man
                        :ARG1-of (g / good-02
                              :degree (v / very))
                        :domain (h2 / he)))))
```
515. " If I ordered a general , " he would say , by way of example , " if I ordered a general to change himself into a sea bird , and if the general did not obey me , that would not be the fault of the general . (lpp_1943.515)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (o / order-01
            :ARG0 h
            :ARG1 (p / person
                  :ARG0-of (h2 / have-org-role-91
                        :ARG2 (g / general)))
            :ARG2 (c / change-01
                  :ARG0 p
                  :ARG1 p
                  :ARG2 (b / bird
                        :mod (s2 / sea)))
            :ARG1-of (o2 / obey-01 :polarity -
                  :ARG0 p)
            :condition-of (f / fault-01 :polarity -
                  :ARG1 p))
      :ARG0-of (e / exemplify-01))
```
516. It would be my fault . " (lpp_1943.516)

```
(f / fault-01
      :ARG1 (i2 / i))
```
517. " May I sit down ? " came now a timid inquiry from the little prince . (lpp_1943.517)

```
(i / inquire-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (p2 / permit-01 :mode interrogative
            :ARG1 (s / sit-down-02
                  :ARG1 p))
      :manner (t / timid)
      :time (n / now))
```
518. " I order you to do so , " the king answered him , and majestically gathered in a fold of his ermine mantle . (lpp_1943.518)

```
(a / and
      :op1 (a2 / answer-01
            :ARG0 (k / king)
            :ARG1 (h / he)
            :ARG2 (o / order-01
                  :ARG0 k
                  :ARG1 h
                  :ARG2 (d / do-02
                        :ARG1 (s / so))))
      :op2 (g / gather-01
            :ARG0 k
            :ARG1 (f / fold
                  :part-of (m3 / mantle
                        :consist-of (e2 / ermine)))
            :manner (m / majesty)))
```
519. But the little prince was wondering ... (lpp_1943.519)

```
(w / wonder-01
  :ARG0 (p / prince
          :mod (l / little)))
```
520. The planet was tiny . (lpp_1943.520)

```
(t / tiny
  :domain (p / planet))
```
521. Over what could this king really rule ? (lpp_1943.521)

```
(p / possible-01
      :ARG1 (r / rule-03
            :ARG0 (k / king)
            :ARG1 (a / amr-unknown)
            :ARG1-of (r2 / real-04)))
```
522. " Sire , " he said to him , " I beg that you will excuse my asking you a question - - " (lpp_1943.522)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (b / beg-01
            :ARG0 h
            :ARG1 p
            :ARG2 (e / excuse-01
                  :ARG0 p
                  :ARG1 h
                  :ARG2 (a / ask-01
                        :ARG0 h
                        :ARG2 p)))
      :ARG2 (p / person
            :ARG1-of (t / title-01
                  :ARG2 (s2 / sire))))
```
523. " I order you to ask me a question , " the king hastened to assure him . (lpp_1943.523)

```
(h / hasten-01
      :ARG0 (k / king)
      :ARG1 (a / assure-01
            :ARG0 k
            :ARG1 (h2 / he)
            :ARG2 (o / order-01
                  :ARG0 k
                  :ARG1 h2
                  :ARG2 (a2 / ask-01
                        :ARG0 h2
                        :ARG2 k))))
```
524. " Sire - - over what do you rule ? " (lpp_1943.524)

```
(s / say-01
      :ARG1 (r / rule-03
            :ARG0 p
            :ARG1 (a / amr-unknown))
      :ARG2 (p / person
            :ARG1-of (t / title-01
                  :ARG2 (s2 / sire))))
```
525. " Over everything , " said the king , with magnificent simplicity . (lpp_1943.525)

```
(s / say-01
      :ARG0 (k / king)
      :ARG1 (e / everything)
      :ARG1-of (s2 / simple-02
            :mod (m / magnificence)))
```
526. " Over everything ? " (lpp_1943.526)

```
(o / over :mode interrogative
      :op1 (e / everything))
```
527. The king made a gesture , which took in his planet , the other planets , and all the stars . (lpp_1943.527)

```
(g / gesture-01
      :ARG0 (k / king)
      :ARG0-of (t / take-in-23
            :ARG1 (a / and
                  :op1 (p / planet
                        :poss k)
                  :op2 (p2 / planet
                        :mod (o / other))
                  :op3 (s / star
                        :mod (a2 / all)))))
```
528. " Over all that ? " asked the little prince . (lpp_1943.528)

```
(a / ask-01 :mode interrogative
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (o / over
            :op1 (t / that
                  :mod (a3 / all))))
```
529. " Over all that , " the king answered . (lpp_1943.529)

```
(a / answer-01
  :ARG0 (k / king)
  :ARG2 (o / over
          :op1 (t / that
                 :mod (a2 / all))))
```
530. For his rule was not only absolute : it was also universal . (lpp_1943.530)

```
(a3 / and
      :op1 (a4 / absolute
            :domain (r / rule-03
                  :ARG0 (h / he)))
      :op2 (u2 / universal
            :domain r))
```
531. " And the stars obey you ? " (lpp_1943.531)

```
(o / obey-01
  :ARG0 (s / star)
  :ARG1 (y / you)
  :mode interrogative)
```
532. " Certainly they do , " the king said . (lpp_1943.532)

```
(s / say-01
  :ARG0 (k / king)
  :ARG1 (d / do-02
          :ARG0 (t / they)
          :mod (c / certain)))
```
533. " They obey instantly . (lpp_1943.533)

```
(o / obey-01
  :ARG0 (t / they)
  :manner (i / instant))
```
534. I do not permit insubordination . " (lpp_1943.534)

```
(p / permit-01 :polarity -
      :ARG0 (i / i)
      :ARG1 (i2 / insubordinate-00))
```
535. Such power was a thing for the little prince to marvel at . (lpp_1943.535)

```
(m / marvel-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (p2 / power
            :degree (s / such)))
```
536. If he had been master of such complete authority , he would have been able to watch the sunset , not forty - four times in one day , but seventy - two , or even a hundred , or even two hundred times , without ever having to move his chair . (lpp_1943.536)

```
(p / possible-01
      :ARG1 (w / watch-01
            :ARG0 (h / he)
            :ARG1 (s / sunset
                  :ARG1-of (h3 / have-frequency-91 :polarity -
                        :ARG2 44
                        :range (t5 / temporal-quantity :quant 1
                              :unit (y / year)))
                  :ARG1-of (h4 / have-frequency-91
                        :ARG2 (o / or :op1 72 :op2 100 :op3 200)
                        :range t5))
            :manner (m2 / move-01 :polarity -
                  :ARG0 h
                  :ARG1 (c2 / chair
                        :poss h)
                  :time (e3 / ever)))
      :condition (m / master
            :domain (h2 / he)
            :poss-of (a / authority
                  :ARG1-of (c / complete-02)
                  :mod (s2 / such))))
```
537. And because he felt a bit sad as he remembered his little planet which he had forsaken , he plucked up his courage to ask the king a favor : " I should like to see a sunset ... do me that kindness ... (lpp_1943.537)

```
(p / pluck-01
      :ARG0 (h / he)
      :ARG1 (c / courage
            :poss h)
      :mod (u / up)
      :ARG1-of (c2 / cause-01
            :ARG0 (f / feel-01
                  :ARG0 h
                  :ARG1 (s3 / sad-02
                        :ARG1 h
                        :degree (b / bit))
                  :ARG1-of (c3 / cause-01
                        :ARG0 (r / remember-01
                              :ARG0 h
                              :ARG1 (p2 / planet
                                    :poss h
                                    :mod (l2 / little)
                                    :ARG1-of (f2 / forsake-01
                                          :ARG0 h))))))
      :ARG0-of (c4 / cause-01
            :ARG1 (a / ask-02
                  :ARG0 h
                  :ARG1 (a2 / and
                        :op1 (l / like-02
                              :ARG0 (i / i)
                              :ARG1 (s / see-01
                                    :ARG0 i
                                    :ARG1 (s2 / sunset)))
                        :op2 (d / do-02 :mode imperative
                              :ARG0 k
                              :ARG1 (t / thing
                                    :ARG1-of (k2 / kind-01
                                          :ARG0 k
                                          :ARG2 h))
                              :ARG2 h))
                  :ARG2 (k / king))))
```
538. Order the sun to set ... " (lpp_1943.538)

```
(o / order-01 :mode imperative
      :ARG0 (y / you)
      :ARG1 (s / sun)
      :ARG2 (s2 / set-11
            :ARG1 s))
```
539. " If I ordered a general to fly from one flower to another like a butterfly , or to write a tragic drama , or to change himself into a sea bird , and if the general did not carry out the order that he had received , which one of us would be in the wrong ? " the king demanded . (lpp_1943.539)

```
(d / demand-01
      :ARG0 (k / king)
      :ARG1 (w / wrong-04
            :ARG1 (a / amr-unknown
                  :ARG1-of (i2 / include-91
                        :ARG2 (w3 / we)))
            :condition (a2 / and
                  :op1 (o3 / order-01
                        :ARG0 k
                        :ARG1 (p / person
                              :ARG0-of (h / have-org-role-91
                                    :ARG2 (g / general)))
                        :ARG2 (o4 / or
                              :op1 (f / fly-01
                                    :ARG1 p
                                    :destination (a3 / another)
                                    :source (t / thing
                                          :ARG1-of (f2 / flower-01 :quant 1))
                                    :manner (b / butterfly))
                              :op2 (w2 / write-01
                                    :ARG0 p
                                    :ARG1 (d2 / drama
                                          :mod (t2 / tragedy)))
                              :op3 (c2 / change-01
                                    :ARG0 p
                                    :ARG1 p
                                    :ARG2 (b2 / bird
                                          :mod (s / sea)))))
                  :op2 (c / carry-out-03 :polarity -
                        :ARG0 p
                        :ARG1 (t3 / thing
                              :ARG2-of (o2 / order-01)
                              :ARG1-of (r / receive-01
                                    :ARG0 p
                                    :ARG2 k))))))
```
540. " The general , or myself ? " (lpp_1943.540)

```
(o / or :mode interrogative
      :op1 (p / person
            :ARG0-of (h / have-org-role-91
                  :ARG2 (g / general)))
      :op2 (i / i))
```
541. " You , " said the little prince firmly . (lpp_1943.541)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (y / you)
      :ARG1-of (f / firm-03))
```
542. " Exactly . (lpp_1943.542)

```
(e / exact)
```
543. One much require from each one the duty which each one can perform , " the king went on . (lpp_1943.543)

```
(g / go-on-25
      :ARG0 (k / king)
      :ARG1 (o / obligate-01
            :ARG1 (o2 / one)
            :ARG2 (r / require-01
                  :ARG0 o2
                  :ARG1 (d / duty
                        :ARG1-of (p / perform-02
                              :ARG0 o3
                              :ARG1-of (p2 / possible-01)))
                  :ARG2 (o3 / one
                        :mod (e / each)))))
```
544. " Accepted authority rests first of all on reason . (lpp_1943.544)

```
(r / rest-02
      :ARG1 (a / authority
            :ARG1-of (a2 / accept-01))
      :ARG2 (r2 / reason-01)
      :mod (f / first-of-all))
```
545. If you ordered your people to go and throw themselves into the sea , they would rise up in revolution . (lpp_1943.545)

```
(r / rise-up-03
      :ARG0 (p / person
            :poss y
            :ARG0-of (r2 / revolution-03))
      :ARG1 y
      :condition (o / order-01
            :ARG0 (y / you)
            :ARG1 p
            :ARG2 (t / throw-01
                  :ARG0 p
                  :ARG1 p
                  :ARG2 (s / sea))))
```
546. I have the right to require obedience because my orders are reasonable . " (lpp_1943.546)

```
(r / right-05
      :ARG1 i
      :ARG2 (r2 / require-01
            :ARG0 (i / i)
            :ARG1 (o / obey-01
                  :ARG1 i))
      :ARG1-of (c / cause-01
            :ARG0 (r3 / reasonable-02
                  :ARG1 (t / thing
                        :ARG2-of (o2 / order-01)))))
```
547. " Then my sunset ? " the little prince reminded him : for he never forgot a question once he had asked it . (lpp_1943.547)

```
(r / remind-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (s / sunset :mode interrogative
            :poss p)
      :ARG2 (h / he)
      :ARG1-of (c / cause-01
            :ARG0 (f / forget-01 :polarity -
                  :ARG0 p
                  :ARG1 (t / thing
                        :ARG1-of (q / question-01))
                  :condition (a / ask-01
                        :ARG0 p
                        :ARG1 t)
                  :time (e / ever))))
```
548. " You shall have your sunset . (lpp_1943.548)

```
(h / have-03
  :ARG0 (y / you)
  :ARG1 (s / sunset
          :poss y))
```
549. I shall command it . (lpp_1943.549)

```
(c / command-02
  :ARG0 (i / i)
  :ARG2 (i2 / it))
```
550. But , according to my science of government , I shall wait until conditions are favorable . " (lpp_1943.550)

```
(c3 / contrast-01
      :ARG2 (w / wait-01
            :ARG1 (i / i)
            :ARG2 (c / condition
                  :mod (f2 / favorable))
            :ARG1-of (c2 / cause-01
                  :ARG0 (s2 / science
                        :domain (g / government-organization
                              :ARG0-of (g2 / govern-01))
                        :poss i))))
```
551. " When will that be ? " inquired the little prince . (lpp_1943.551)

```
(i / inquire-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (b2 / be-temporally-at-91
            :ARG1 (t / that)
            :ARG2 (a / amr-unknown)))
```
552. " Hum ! (lpp_1943.552)

```
(h / hum :mode expressive)
```
553. Hum ! " replied the king ; and before saying anything else he consulted a bulky almanac . (lpp_1943.553)

```
(a / and
      :op1 (r / reply-01
            :ARG0 (k / king)
            :ARG2 (h / hum :mode expressive))
      :op2 (c / consult-01
            :ARG0 k
            :ARG1 (a2 / almanac
                  :ARG1-of (b / bulky-02))
            :time (b2 / before
                  :op1 (s / say-01
                        :ARG0 k
                        :ARG1 (a3 / anything
                              :mod (e / else))))))
```
554. " Hum ! (lpp_1943.554)

```
(h / hum :mode expressive)
```
555. Hum ! (lpp_1943.555)

```
(h / hum :mode expressive)
```
556. That will be about - - about - - that will be this evening about twenty minutes to eight . (lpp_1943.556)

```
(b / be-temporally-at-91
      :ARG1 (t3 / that)
      :ARG2 (a / about
            :op1 (d / date-entity :time "19:40"
                  :dayperiod (e / evening)
                  :mod (t / today))))
```
557. And you will see how well I am obeyed . " (lpp_1943.557)

```
(s / see-01
      :ARG0 (y / you)
      :ARG1 (o / obey-01
            :ARG1 (i / i)
            :manner (w / well
                  :degree (a / amr-unknown))))
```
558. The little prince yawned . (lpp_1943.558)

```
(y / yawn-01
  :ARG0 (p / prince
          :mod (l / little)))
```
559. He was regretting his lost sunset . (lpp_1943.559)

```
(r / regret-01
      :ARG0 (h / he)
      :ARG1 (l / lose-02
            :ARG0 h
            :ARG1 (s / sunset)))
```
560. And then , too , he was already beginning to be a little bored . (lpp_1943.560)

```
(a2 / and
      :op2 (b / begin-01
            :ARG1 (b4 / bore-02
                  :ARG1 (h2 / he)
                  :degree (l / little))
            :time (a / already)))
```
561. " I have nothing more to do here , " he said to the king . (lpp_1943.561)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (r / remain-01 :polarity -
            :ARG1 (t / thing
                  :ARG1-of (d2 / do-02))
            :location (h2 / here))
      :ARG2 (k / king))
```
562. " So I shall set out on my way again . " (lpp_1943.562)

```
(c / cause-01
      :ARG1 (s / set-out-07
            :ARG0 (i / i)
            :ARG1 (w / way
                  :poss i)
            :mod (a / again)))
```
563. " Do not go , " said the king , who was very proud of having a subject . (lpp_1943.563)

```
(s / say-01
      :ARG0 (k / king
            :ARG0-of (p / pride-01
                  :ARG2 (h / have-03
                        :ARG0 k
                        :ARG1 (s2 / subject))
                  :degree (v / very)))
      :ARG1 (g / go-02 :polarity - :mode imperative
            :ARG0 (y / you)))
```
564. " Do not go . (lpp_1943.564)

```
(g / go-02 :polarity - :mode imperative
      :ARG0 (y / you))
```
565. I will make you a Minister ! " (lpp_1943.565)

```
(m / make-02
      :ARG0 (i / i)
      :ARG1 (h / have-org-role-91
            :ARG0 (y / you)
            :ARG2 (m2 / minister)))
```
566. " Minister of what ? " (lpp_1943.566)

```
(m / minister
      :topic (a / amr-unknown))
```
567. " Minster of - - of Justice ! " (lpp_1943.567)

```
(m / minister
      :topic (j / justice))
```
568. " But there is nobody here to judge ! " (lpp_1943.568)

```
(n / nobody
      :location (h / here)
      :ARG1-of (j / judge-01))
```
569. " We do not know that , " the king said to him . (lpp_1943.569)

```
(s / say-01
  :ARG0 (k / king)
  :ARG1 (k2 / know-01
          :ARG0 (w / we)
          :ARG1 (t / that)
          :polarity -)
  :ARG2 (h / he))
```
570. " I have not yet made a complete tour of my kingdom . (lpp_1943.570)

```
(t / tour-01 :polarity -
      :ARG0 (i / i)
      :ARG1 (k / kingdom
            :poss i)
      :ARG1-of (c / complete-02))
```
571. I am very old . (lpp_1943.571)

```
(o2 / old
      :domain (i / i)
      :degree (v / very))
```
572. There is no room here for a carriage . (lpp_1943.572)

```
(r / room
  :polarity -
  :purpose (c / carriage)
  :location (h / here))
```
573. And it tires me to walk . " (lpp_1943.573)

```
(t / tire-01
  :ARG0 (w / walk-01
          :ARG0 (i / i))
  :ARG1 i)
```
574. " Oh , but I have looked already ! " said the little prince , turning around to give one more glance to the other side of the planet . (lpp_1943.574)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little)
            :ARG0-of (t / turn-01
                  :ARG1 p
                  :purpose (g / glance-01 :quant 1
                        :ARG0 p
                        :ARG1 (s2 / side
                              :mod (o / other)
                              :part-of (p2 / planet))
                        :mod (m / more))))
      :ARG1 (c / contrast-01
            :ARG2 (l2 / look-01
                  :ARG0 p
                  :time (a2 / already))))
```
575. On that side , as on this , there was nobody at all ... (lpp_1943.575)

```
(n2 / nobody
  :location (s / side
              :mod (t / that)
              :ARG1-of (s2 / same-01
                         :ARG2 (t2 / this)))
  :mod (a / at-all))
```
576. " Then you shall judge yourself , " the king answered . (lpp_1943.576)

```
(a / answer-01
      :ARG0 (k / king)
      :ARG2 (h / have-condition-91
            :ARG1 (j / judge-01
                  :ARG0 (y / you)
                  :ARG1 y)))
```
577. " that is the most difficult thing of all . (lpp_1943.577)

```
(t / thing
      :domain (t2 / that)
      :mod (d / difficult
            :degree (m / most)
            :compared-to (a / all)))
```
578. It is much more difficult to judge oneself than to judge others . (lpp_1943.578)

```
(d / difficult
      :degree (m / more
            :degree (m2 / much))
      :domain (j / judge-01
            :ARG0 (o2 / one)
            :ARG1 o2)
      :compared-to (j2 / judge-01
            :ARG1 (o / other)))
```
579. If you succeed in judging yourself rightly , then you are indeed a man of true wisdom . " (lpp_1943.579)

```
(w2 / wise
      :domain (y / you)
      :condition (s / succeed-01
            :ARG0 y
            :ARG1 (j / judge-01
                  :ARG0 y
                  :ARG1 y
                  :ARG1-of (r / right-02)))
      :ARG1-of (t / true-01))
```
580. " Yes , " said the little prince , " but I can judge myself anywhere . (lpp_1943.580)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (y / yes
          :concession (p2 / possible-01
                        :ARG1 (j / judge-01
                                  :ARG0 p
                                  :ARG1 p
                                  :location (a / anywhere)))))
```
581. I do not need to live on this planet . (lpp_1943.581)

```
(n / need-01
  :ARG0 (i / i)
  :ARG1 (l / live-01
          :ARG0 i
          :location (p / planet
                      :mod (t / this)))
  :polarity -)
```
582. " Hum ! (lpp_1943.582)

```
(h / hum :mode expressive)
```
583. Hum ! " said the king . (lpp_1943.583)

```
(s / say-01
      :ARG0 (k / king)
      :ARG1 (h / hum :mode expressive))
```
584. " I have good reason to believe that somewhere on my planet there is an old rat . (lpp_1943.584)

```
(h2 / have-03
      :ARG0 (i / i)
      :ARG1 (r3 / reason
            :ARG1-of (g / good-02)
            :ARG0-of (c / cause-01
                  :ARG1 (b3 / believe-01
                        :ARG0 i
                        :ARG1 (r2 / rat
                              :location (s / somewhere
                                    :location (p / planet
                                          :poss i))
                              :mod (o / old))))))
```
585. I hear him at night . (lpp_1943.585)

```
(h / hear-01
  :ARG0 (i / i)
  :ARG1 (h2 / he)
  :time (d / date-entity :dayperiod (n / night)))
```
586. You can judge this old rat . (lpp_1943.586)

```
(p / possible-01
      :ARG1 (j / judge-01
            :ARG0 (y / you)
            :ARG1 (r / rat
                  :mod (o / old)
                  :mod (t / this))))
```
587. From time to time you will condemn him to death . (lpp_1943.587)

```
(c / condemn-01
  :ARG0 (y / you)
  :ARG1 (h / he)
  :ARG3 (d / die-01
          :ARG1 h)
  :frequency (t / time-to-time))
```
588. Thus his life will depend on your justice . (lpp_1943.588)

```
(d / depend-01
      :ARG0 (l / live-01
            :ARG0 (h / he))
      :ARG1 (j / justice
            :poss (y / you)))
```
589. But you will pardon him on each occasion ; for he must be treated thriftily . (lpp_1943.589)

```
(p / pardon-01
      :ARG0 (y / you)
      :ARG1 (h / he)
      :frequency (o2 / occasion-02
            :quant (e / each))
      :ARG1-of (c / cause-01
            :ARG0 (o / obligate-01
                  :ARG2 (t / treat-04
                        :ARG1 h
                        :manner (t2 / thrift)))))
```
590. He is the only one we have . " (lpp_1943.590)

```
(o / one
      :mod (o2 / only)
      :domain (h2 / he)
      :ARG1-of (h / have-03
            :ARG0 (w / we)))
```
591. " I , " replied the little prince , " do not like to condemn anyone to death . (lpp_1943.591)

```
(r / reply-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (l2 / like-01 :polarity -
            :ARG0 p
            :ARG1 (c / condemn-01
                  :ARG0 p
                  :ARG1 (a / anyone)
                  :ARG3 (d / die-01
                        :ARG1 a))))
```
592. And now I think I will go on my way . " (lpp_1943.592)

```
(t / think-01
      :ARG0 (i / i)
      :ARG1 (g / go-02
            :ARG0 i
            :ARG1 (w / way
                  :poss i))
      :time (n / now))
```
593. " No , " said the king . (lpp_1943.593)

```
(s / say-01
      :ARG0 (k / king)
      :ARG1 (n / no))
```
594. But the little prince , having now completed his preparations for departure , had no wish to grieve the old monarch . (lpp_1943.594)

```
(w / wish-01 :polarity -
      :ARG0 (p / prince
            :mod (l / little)
            :ARG0-of (c / complete-01
                  :ARG1 (p2 / prepare-02
                        :ARG0 p
                        :ARG2 (d / depart-01
                              :ARG0 p))
                  :time (n / now)))
      :ARG1 (g / grieve-01
            :ARG0 p
            :ARG1 (m / monarch
                  :mod (o / old))))
```
595. " If Your Majesty wishes to be promptly obeyed , " he said , " he should be able to give me a reasonable order . (lpp_1943.595)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (p / possible-01
            :ARG1 (o / order-01
                  :ARG0 (p2 / person
                        :ARG1-of (t2 / title-01
                              :ARG2 (m / majesty
                                    :poss p2)))
                  :ARG1 h
                  :ARG2 (t / thing
                        :ARG1-of (r / reasonable-02)))
            :condition (w / wish-01
                  :ARG0 p2
                  :ARG1 (o2 / obey-01
                        :ARG1 p2
                        :manner (p3 / prompt)))))
```
596. He should be able , for example , to order me to be gone by the end of one minute . (lpp_1943.596)

```
(e2 / exemplify-01
      :ARG0 (p / possible-01
            :ARG1 (o / order-01
                  :ARG0 (h / he)
                  :ARG1 (i / i)
                  :ARG2 (g / go-02
                        :ARG0 i
                        :time (b / by
                              :op1 (e / end-01
                                    :ARG1 (t / temporal-quantity :quant 1
                                          :unit (m / minute))))))))
```
597. It seems to me that conditions are favorable ... " (lpp_1943.597)

```
(s / seem-01
      :ARG1 (f / favorable
            :domain (c / condition))
      :ARG2 (i2 / i))
```
598. As the king made no answer , the little prince hesitated a moment . (lpp_1943.598)

```
(h / hesitate-01
      :ARG0 (p / prince
            :mod (l / little))
      :duration (m / moment)
      :ARG1-of (c / cause-01
            :ARG0 (a / answer-01 :polarity -
                  :ARG0 (k / king))))
```
599. Then , with a sigh , he took his leave . (lpp_1943.599)

```
(t / take-01
      :ARG0 (h / he
            :ARG0-of (s / sigh-02))
      :ARG1 (l / leave-11
            :ARG0 h)
      :time (t2 / then))
```
600. " I made you my Ambassador , " the king called out , hastily . (lpp_1943.600)

```
(c / call-07
      :ARG0 (k / king)
      :ARG1 (m / make-02
            :ARG0 k
            :ARG1 (h2 / have-org-role-91
                  :ARG0 (y / you)
                  :ARG1 k
                  :ARG2 (a / ambassador)))
      :manner (h / hasty))
```
601. He had a magnificent air of authority . (lpp_1943.601)

```
(h / have-03
      :ARG0 (h2 / he)
      :ARG1 (a / air
            :mod (m / magnificence)
            :domain (a2 / authority)))
```
602. " The grown - ups are very strange , " the little prince said to himself , as he continued on his journey . (lpp_1943.602)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (s2 / strange
            :degree (v / very)
            :domain (g / grown-up))
      :ARG2 p
      :time (c / continue-01
            :ARG0 p
            :ARG1 (j / journey-01
                  :ARG0 p)))
```
603. Chapter 11 . (lpp_1943.603)

```
(c / chapter :mod 11)
```
604. The second planet was inhabited by a conceited man . (lpp_1943.604)

```
(i / inhabit-01
  :ARG0 (m / man
          :mod (c / conceit))
  :ARG1 (p / planet
          :ord (o / ordinal-entity :value 2)))
```
605. " Ah ! (lpp_1943.605)

```
(a / ah :mode expressive)
```
606. Ah ! (lpp_1943.606)

```
(a / ah :mode expressive)
```
607. I am about to receive a visit from an admirer ! " he exclaimed from afar , when he first saw the little prince coming . (lpp_1943.607)

```
(e / exclaim-01
      :ARG0 (h / he)
      :ARG1 (v / visit-01
            :ARG0 h
            :ARG1 (p / person
                  :ARG0-of (a / admire-01
                        :ARG1 h))
            :time (a3 / about-to))
      :time (s / see-01
            :ARG0 h
            :ARG1 (c / come-01
                  :ARG1 (p2 / prince
                        :mod (l / little)))
            :ord (o / ordinal-entity :value 1))
      :direction (f2 / from
            :op1 (a2 / afar)))
```
608. For , to conceited men , all other men are admirers . (lpp_1943.608)

```
(o2 / opine-01
      :ARG0 (m2 / man
            :mod (c / conceit))
      :ARG1 (p2 / person
            :ARG0-of (a3 / admire-01)
            :domain (m / man
                  :mod (o / other)
                  :mod (a / all))))
```
609. " Good morning , " said the little prince . (lpp_1943.609)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (m / morning
            :ARG1-of (g / good-02)))
```
610. " That is a queer hat you are wearing . " (lpp_1943.610)

```
(h2 / hat
      :mod (q2 / queer)
      :domain (t2 / that)
      :ARG1-of (w2 / wear-01))
```
611. " It is a hat for salutes , " the conceited man replied . (lpp_1943.611)

```
(r / reply-01
      :ARG0 (m / man
            :mod (c / conceit))
      :ARG1 (h2 / hat
            :purpose (s / salute-01
                  :instrument h2)
            :domain (i / it)))
```
612. " It is to raise in salute when people acclaim me . (lpp_1943.612)

```
(h / have-purpose-91
      :ARG1 (i / it)
      :ARG2 (r / raise-01
            :ARG1 i
            :subevent-of (s / salute-01
                  :time (a / acclaim-01
                        :ARG0 (p / person)
                        :ARG1 (i2 / i))
                  :instrument i)))
```
613. Unfortunately , nobody at all ever passes this way . " (lpp_1943.613)

```
(p / pass-03
      :ARG1 (n / nobody
            :degree (a / at-all))
      :path (w / way
            :mod (t / this))
      :ARG2-of (f / fortunate-01 :polarity -)
      :time (e / ever))
```
614. " Yes ? " said the little prince , who did not understand what the conceited man was talking about . (lpp_1943.614)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little)
          :ARG0-of (u / understand-01
                     :ARG1 (a / amr-unknown
                             :ARG1-of (t / talk-01
                                        :ARG0 (m / man
                                                :mod (c / conceit))))
                     :polarity -))
  :ARG1 (y / yes
          :mode interrogative))
```
615. " Clap your hands , one against the other , " the conceited man now directed him . (lpp_1943.615)

```
(d / direct-01
      :ARG0 (m / man
            :mod (c / conceit))
      :ARG1 (h / he)
      :ARG2 (c2 / clap-01 :mode imperative
            :ARG0 h
            :ARG1 (h2 / hand
                  :part-of h)
            :manner (c3 / clap-01
                  :ARG0 h
                  :ARG1 (h3 / hand :quant 1
                        :part-of h)
                  :ARG2 (h4 / hand
                        :part-of h
                        :ARG1-of (d2 / differ-02
                              :ARG2 h3))))
      :time (n / now))
```
616. The little prince clapped his hands . (lpp_1943.616)

```
(c / clap-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (h / hand
          :part-of p))
```
617. The conceited man raised his hat in a modest salute . (lpp_1943.617)

```
(r / raise-01
      :ARG0 (m / man
            :mod (c / conceit))
      :ARG1 (h / hat
            :poss m)
      :subevent-of (s / salute-01
            :ARG0 m
            :manner (m2 / modest)
            :instrument h))
```
618. " This is more entertaining than the visit to the king , " the little prince said to himself . (lpp_1943.618)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (e / entertain-01
            :ARG0 (t / this)
            :degree (m / more)
            :compared-to (v / visit-01
                  :ARG1 (k / king)))
      :ARG2 p)
```
619. And he began again to clap his hands , one against the other . (lpp_1943.619)

```
(b / begin-01
      :ARG0 (h / he)
      :ARG1 (c / clap-01
            :ARG0 h
            :ARG1 (h2 / hand
                  :part-of h)
            :manner (c2 / clap-01
                  :ARG0 h
                  :ARG1 (h3 / hand :quant 1
                        :part-of h)
                  :ARG2 (h4 / hand
                        :part-of h
                        :ARG1-of (d / differ-02
                              :ARG2 h3))))
      :mod (a / again))
```
620. The conceited man against raised his hat in salute . (lpp_1943.620)

```
(r / raise-01
      :ARG0 (m / man
            :mod (c / conceit))
      :ARG1 (h2 / hat)
      :mod (a / again)
      :subevent-of (s / salute-01
            :ARG0 m
            :instrument h2))
```
621. After five minutes of this exercise the little prince grew tired of the game 's monotony . (lpp_1943.621)

```
(t / tire-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (m / monotony
            :poss (g2 / game))
      :time (a / after
            :op1 (e / exercise
                  :duration (t2 / temporal-quantity :quant 5
                        :unit (m2 / minute)))))
```
622. " And what should one do to make the hat come down ? " he asked . (lpp_1943.622)

```
(a / ask-01
      :ARG0 (h / he)
      :ARG1 (d / do-02
            :ARG0 (o / one)
            :ARG1 (a2 / amr-unknown)
            :ARG2 (m / make-02
                  :ARG0 o
                  :ARG1 (c / come-01
                        :ARG1 (h3 / hat)
                        :direction (d3 / down)))))
```
623. But the conceited man did not hear him . (lpp_1943.623)

```
(h / hear-01
  :ARG0 (m / man
          :mod (c / conceit))
  :ARG2 (h2 / he)
  :polarity -)
```
624. Conceited people never hear anything but praise . (lpp_1943.624)

```
(h / hear-01 :polarity -
      :ARG0 (p / person
            :mod (c / conceit))
      :ARG1 (a / anything
            :concession (p2 / praise-01))
      :time (e / ever))
```
625. " Do you really admire me very much ? " he demanded of the little prince . (lpp_1943.625)

```
(d / demand-01
      :ARG0 (h / he)
      :ARG1 (a / admire-01 :mode interrogative
            :ARG0 p
            :ARG1 h
            :degree (m / much
                  :degree (v / very))
            :ARG1-of (r / real-04))
      :ARG2 (p / prince
            :mod (l / little)))
```
626. " What does that mean - - ' admire ' ? " (lpp_1943.626)

```
(m / mean-01
      :ARG1 (a / admire-01)
      :ARG2 (a2 / amr-unknown))
```
627. " To admire mean that you regard me as the handsomest , the best - dressed , the richest , and the most intelligent man on this planet . " (lpp_1943.627)

```
(m / mean-01
      :ARG1 (a / admire-01)
      :ARG2 (r / regard-01
            :ARG0 (y / you)
            :ARG1 (i / i)
            :ARG2 (m6 / man
                  :mod (h / handsome
                        :degree (m2 / most))
                  :ARG1-of (d / dress-01
                        :manner (w / well
                              :degree (m3 / most)))
                  :mod (r2 / rich
                        :degree (m4 / most))
                  :ARG1-of (i2 / intelligent-01
                        :degree (m5 / most))
                  :location (p2 / planet
                        :mod (t / this)))))
```
628. " But you are the only man on your planet ! " (lpp_1943.628)

```
(c / contrast-01
      :ARG2 (m / man
            :quant (o / only
                  :location (p / planet
                        :poss y))
            :domain (y / you)))
```
629. " Do me this kindness . (lpp_1943.629)

```
(k2 / kind-01 :mode imperative
      :ARG0 (y / you)
      :ARG1 (t / this)
      :ARG2 (i / i))
```
630. Admire me just the same . " (lpp_1943.630)

```
(a / admire-01 :mode imperative
      :ARG0 (y / you)
      :ARG1 (i / i)
      :manner (s / same-01
            :degree (j / just)))
```
631. " I admire you , " said the little prince , shrugging his shoulders slightly , " but what is there in that to interest you so much ? " (lpp_1943.631)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little)
            :ARG0-of (s2 / shrug-01
                  :ARG1 (s3 / shoulder
                        :part-of p)
                  :degree (s4 / slight)))
      :ARG1 (c2 / contrast-01
            :ARG1 (a / admire-01
                  :ARG0 (i / i)
                  :ARG1 (y / you))
            :ARG2 (i2 / interest-01
                  :ARG0 a
                  :ARG1 y
                  :degree (m / much
                        :degree (s6 / so))
                  :ARG1-of (c / cause-01
                        :ARG0 (a2 / amr-unknown)))))
```
632. And the little prince went away . (lpp_1943.632)

```
(a / and
      :op2 (g / go-02
            :ARG0 (p / prince
                  :mod (l / little))
            :direction (a2 / away)))
```
633. " The grown - ups are certainly very odd , " he said to himself , as he continued on his journey . (lpp_1943.633)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (o / odd
            :degree (v / very)
            :mod (c2 / certain)
            :domain (g / grown-up))
      :ARG2 h
      :time (c / continue-01
            :ARG0 h
            :ARG1 (j / journey-01
                  :ARG0 h)))
```
634. Chapter 12 . (lpp_1943.634)

```
(c / chapter
  :mod 12)
```
635. The next planet was inhabited by a tippler . (lpp_1943.635)

```
(i / inhabit-01
      :ARG0 (p / person
            :ARG0-of (t / tipple-01))
      :ARG1 (p2 / planet
            :mod (n / next)))
```
636. This was a very short visit , but it plunged the little prince into deep dejection . (lpp_1943.636)

```
(h / have-concession-91
      :ARG1 (d / deject-01
            :ARG0 v
            :ARG1 (p2 / prince
                  :mod (l / little))
            :ARG1-of (d2 / deep-02))
      :ARG2 (v / visit-01
            :ARG1-of (s / short-07
                  :degree (v2 / very))
            :domain (t / this)))
```
637. " What are you doing there ? " he said to the tippler , whom he found settled down in silence before a collection of empty bottles and also a collection of full bottles . (lpp_1943.637)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (d / do-02
            :ARG0 p
            :ARG1 (a / amr-unknown)
            :location (t / there))
      :ARG2 (p / person
            :ARG0-of (t2 / tipple-01)
            :ARG1-of (f / find-01
                  :ARG0 h)
            :ARG1-of (s2 / settle-down-04
                  :manner (s3 / silent)
                  :location (b / before
                        :op1 (a2 / and
                              :op1 (b2 / bottle
                                    :ARG1-of (e / empty-02)
                                    :ARG1-of (c / collect-01))
                              :op2 (b3 / bottle
                                    :mod (f2 / full)
                                    :ARG1-of (c2 / collect-01)))))))
```
638. " I am drinking , " replied the tippler , with a lugubrious air . (lpp_1943.638)

```
(r / reply-01
      :ARG0 (p / person
            :ARG0-of (t / tipple-01))
      :ARG2 (d / drink-01
            :ARG0 p)
      :manner (l / lugubrious))
```
639. " Why are you drinking ? " demanded the little prince . (lpp_1943.639)

```
(d / demand-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (c / cause-01
          :ARG0 (a / amr-unknown)
          :ARG1 (d2 / drink-01
                  :ARG0 (y / you))))
```
640. " So that I may forget , " replied the tippler . (lpp_1943.640)

```
(r / reply-01
  :ARG0 (p / person
          :ARG0-of (t / tipple-01))
  :ARG2 (c / cause-01
          :ARG0 (p2 / possible-01
                  :ARG1 (f / forget-01
                            :ARG0 p))))
```
641. " Forget what ? " inquired the little prince , who already was sorry for him . (lpp_1943.641)

```
(i / inquire-01
      :ARG0 (p / prince
            :mod (l / little)
            :ARG1-of (s / sorry-01
                  :ARG2 (h / he)
                  :time (a2 / already)))
      :ARG1 (f / forget-01
            :ARG0 h
            :ARG1 (a / amr-unknown))
      :ARG2 h)
```
642. " Forget that I am ashamed , " the tippler confessed , hanging his head . (lpp_1943.642)

```
(c / confess-01
  :ARG0 (p / person
          :ARG0-of (t / tipple-01)
          :ARG0-of (h / hang-01
                     :ARG1 (h2 / head
                             :part-of p)))
  :ARG1 (f / forget-01
          :ARG0 p
          :ARG1 (s / shame-01
                  :ARG1 p)))
```
643. " Ashamed of what ? " insisted the little prince , who wanted to help him . (lpp_1943.643)

```
(i / insist-01
      :ARG0 (p / prince
            :mod (l / little)
            :ARG0-of (w / want-01
                  :ARG1 (h / help-01
                        :ARG0 p
                        :ARG1 (h2 / he))))
      :ARG1 (a / amr-unknown
            :ARG0-of (s / shame-01)))
```
644. " Ashamed of drinking ! " (lpp_1943.644)

```
(s / shame-01
  :ARG0 (d / drink-01))
```
645. The tippler brought his speech to an end , and shut himself up in an impregnable silence . (lpp_1943.645)

```
(a / and
      :op1 (e / end-01
            :ARG0 (p / person
                  :ARG0-of (t / tipple-01))
            :ARG1 (s / speak-01
                  :ARG0 p))
      :op2 (s2 / shut-up-06
            :ARG0 p
            :ARG1 p
            :manner (s3 / silent
                  :mod (p2 / pregnable :polarity -)
                  :domain p)))
```
646. And the little prince went away , puzzled . (lpp_1943.646)

```
(a / and
      :op2 (g / go-02
            :ARG0 (p / prince
                  :mod (l / little)
                  :ARG1-of (p2 / puzzle-01))
            :direction (a2 / away)))
```
647. " The grown - ups are certainly very , very odd , " he said to himself , as he continued on his journey . (lpp_1943.647)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (o / odd
            :degree (v / very
                  :degree (v2 / very))
            :domain (g / grown-up)
            :mod (c / certain))
      :ARG2 h
      :time (c2 / continue-01
            :ARG0 h
            :ARG1 (j / journey-01
                  :ARG0 h)))
```
648. Chapter 13 . (lpp_1943.648)

```
(c / chapter
  :mod 13)
```
649. The fourth planet belonged to a businessman . (lpp_1943.649)

```
(b / belong-01
      :ARG0 (p / planet
            :ord (o / ordinal-entity :value 4))
      :ARG1 (b3 / businessman))
```
650. This man was so much occupied that he did not even raise his head at the little prince 's arrival . (lpp_1943.650)

```
(o / occupy-01
  :ARG1 (m / man
          :mod (t / this))
  :degree (m2 / much
            :degree (s / so))
  :ARG0-of (c / cause-01
             :ARG1 (r / raise-01
                     :ARG0 m
                     :ARG1 (h / head
                             :part-of m)
                     :polarity -
                     :time (a / arrive-01
                             :ARG1 (p / prince
                                     :mod (l / little))))))
```
651. " Good morning , " the little prince said to him . (lpp_1943.651)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (m / morning
            :ARG1-of (g / good-02))
      :ARG2 (h / he))
```
652. " Your cigarette has gone out . " (lpp_1943.652)

```
(g / go-out-18
  :ARG1 (c / cigarette
          :poss (y / you)))
```
653. " Three and two make five . (lpp_1943.653)

```
(e / equal-01
      :ARG1 (s / sum-of :op1 3 :op2 2)
      :ARG2 5)
```
654. Five and seven make twelve . (lpp_1943.654)

```
(e / equal-01
      :ARG1 (s / sum-of :op1 5 :op2 7)
      :ARG2 12)
```
655. Twelve and three make fifteen . (lpp_1943.655)

```
(e / equal-01
      :ARG1 (s / sum-of :op1 12 :op2 3)
      :ARG2 15)
```
656. Good morning . (lpp_1943.656)

```
(m / morning
      :ARG1-of (g / good-02))
```
657. FIfteen and seven make twenty - two . (lpp_1943.657)

```
(e / equal-01
  :ARG1 (s / sum-of
          :op1 15
          :op2 7)
  :ARG2 22)
```
658. Twenty - two and six make twenty - eight . (lpp_1943.658)

```
(e / equal-01
  :ARG1 (s / sum-of
          :op1 22
          :op2 6)
  :ARG2 28)
```
659. I have n't time to light it again . (lpp_1943.659)

```
(h / have-03
  :ARG0 (i / i)
  :ARG1 (t / time
          :purpose (l / light-04
                     :ARG0 i
                     :ARG1 (i2 / it)
                     :mod (a / again)))
  :polarity -)
```
660. Twenty - six and five make thirty - one . (lpp_1943.660)

```
(e / equal-01
  :ARG1 (s / sum-of
          :op1 26
          :op2 5)
  :ARG2 31)
```
661. Phew ! (lpp_1943.661)

```
(p / phew :mode expressive)
```
662. Then that makes five - hundred - and - one - million , six - hundred - twenty - two - thousand , seven - hundred - thirty - one . " (lpp_1943.662)

```
(e / equal-01
      :ARG1 501622731
      :ARG2 (t / that))
```
663. " Five hundred million what ? " asked the little prince . (lpp_1943.663)

```
(a / ask-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (a2 / amr-unknown
          :quant 500000000))
```
664. " Eh ? (lpp_1943.664)

```
(e / eh :mode expressive :mode interrogative)
```
665. Are you still there ? (lpp_1943.665)

```
(b / be-located-at-91
  :ARG1 (y / you)
  :ARG2 (t / there)
  :mode interrogative
  :mod (s / still))
```
666. Five - hundred - and - one million - - I can n't stop ... (lpp_1943.666)

```
(a / and
  :op1 501000000
  :op2 (p / possible-01
         :ARG1 (s / stop-01
                   :ARG0 (i / i))
         :polarity -))
```
667. I have so much to do ! (lpp_1943.667)

```
(o / obligate-01
  :ARG1 (i / i)
  :ARG2 (d / do-02
          :ARG1 (m / much
                  :degree (s / so))))
```
668. I am concerned with matters of consequence . (lpp_1943.668)

```
(c / concern-01
  :ARG0 (m / matter
          :mod (c2 / consequence))
  :ARG1 (i / i))
```
669. I do n't amuse myself with balderdash . (lpp_1943.669)

```
(a / amuse-01
  :ARG0 (i / i)
  :ARG1 i
  :ARG2 (b / balderdash)
  :polarity -)
```
670. Two and five make seven ... " (lpp_1943.670)

```
(e / equal-01
  :ARG1 7
  :ARG2 (s / sum-of
          :op1 2
          :op2 5))
```
671. " Five - hundred - and - one million what ? " repeated the little prince , who never in his life had let go of a question once he had asked it . (lpp_1943.671)

```
(r / repeat-01
      :ARG0 (p / prince
            :mod (l / little)
            :ARG0-of (l2 / let-01 :polarity -
                  :ARG1 (g / go-02
                        :ARG0 (t / thing
                              :ARG1-of (q / question-01
                                    :ARG0 p)))
                  :time (l3 / live-01
                        :ARG0 p)
                  :time (a2 / ask-01
                        :ARG0 p
                        :ARG1 t)
                  :time (e / ever)))
      :ARG1 (a / amr-unknown :quant 501000000))
```
672. The businessman raised his head . (lpp_1943.672)

```
(r / raise-01
      :ARG0 (b / businessman)
      :ARG1 (h / head
            :part-of b))
```
673. " During the fifty - four years that I have inhabited this planet , I have been disturbed only three times . (lpp_1943.673)

```
(d / disturb-01
      :ARG1 (i / i)
      :ARG1-of (h / have-frequency-91
            :ARG2 3
            :mod (o / only))
      :time (i2 / inhabit-01
            :ARG0 i
            :ARG1 (p / planet
                  :mod (t / this))
            :duration (t2 / temporal-quantity :quant 54
                  :unit (y / year))))
```
674. The first time was twenty - two years ago , when some giddy goose fell from goodness knows where . (lpp_1943.674)

```
(b / be-temporally-at-91
      :ARG1 (d / disturb-01
            :ord (o / ordinal-entity :value 1))
      :ARG2 (b2 / before
            :op1 (n / now)
            :quant (t4 / temporal-quantity :quant 22
                  :unit (y2 / year))
            :time-of (f3 / fall-01
                  :ARG1 (g4 / goose
                        :mod (g5 / giddy)
                        :mod (s2 / some))
                  :ARG3 (l / location
                        :ARG1-of (k2 / know-01
                              :ARG0 (g6 / goodness))))))
```
675. He made the most frightful noise that resounded all over the place , and I made four mistakes in my addition . (lpp_1943.675)

```
(a / and
      :op1 (m / make-01
            :ARG0 (h / he)
            :ARG1 (n / noise
                  :ARG1-of (r / resound-01
                        :ARG2 (a4 / all-over
                              :op1 (p / place)))
                  :ARG0-of (f2 / frighten-01
                        :degree (m2 / most))))
      :op1 (m4 / mistake-02 :quant 4
            :ARG0 i
            :ARG1 (a3 / add-02
                  :ARG0 (i / i))))
```
676. The second time , eleven years ago , I was disturbed by an attack of rheumatism . (lpp_1943.676)

```
(d / disturb-01
      :ARG0 (a / attack-01
            :ARG0 (r / rheumatism)
            :ARG1 i)
      :ARG1 (i / i)
      :time (b / before
            :op1 (n / now)
            :quant (t2 / temporal-quantity :quant 11
                  :unit (y / year)))
      :domain (d2 / disturb-01
            :ord (o / ordinal-entity :value 2)))
```
677. I do n't get enough exercise . (lpp_1943.677)

```
(e / exercise-02
  :ARG0 (i / i)
  :degree (e2 / enough
            :polarity -))
```
678. I have no time for loafing . (lpp_1943.678)

```
(h / have-03
  :ARG0 (i / i)
  :ARG1 (t / time
          :purpose (l / loaf-01
                     :ARG0 i))
  :polarity -)
```
679. The third time - - well , this is it ! (lpp_1943.679)

```
(d / disturb-01
      :ord (o / ordinal-entity :value 3)
      :domain (t / this))
```
680. I was saying , then , five - hundred - and - one millions - - " (lpp_1943.680)

```
(s / say-01
  :ARG0 (i / i)
  :ARG1 501000000)
```
681. " Millions of what ? " (lpp_1943.681)

```
(a / amr-unknown
  :quant (m / multiple
           :op1 1000000))
```
682. The businessman suddenly realized that there was no hope of being left in peace until he answered this question . (lpp_1943.682)

```
(r / realize-01
      :ARG0 (b / businessman)
      :ARG1 (h / hopeful-03 :polarity -
            :ARG1 (l / leave-14
                  :ARG1 (p / peace
                        :domain b))
            :time (u / until
                  :op1 (a / answer-01
                        :ARG0 b
                        :ARG1 (q / question-01
                              :ARG1 (t / this)))))
      :manner (s / sudden))
```
683. " Millions of those little objects , " he said , " which one sometimes sees in the sky . " (lpp_1943.683)

```
(s / say-01
  :ARG0 (h / he)
  :ARG1 (o / object
          :ARG1-of (i / include-91
                     :ARG2 (o3 / object
                             :mod (l / little)
                             :mod (t2 / that)
                             :location (s4 / sky)
                             :ARG1-of (s2 / see-01
                                        :ARG0 (o2 / one)
                                        :frequency (s3 / sometimes))))
          :quant (m / multiple
                   :op1 1000000)))
```
684. " Flies ? " (lpp_1943.684)

```
(f / fly :mode interrogative)
```
685. " Oh , no . (lpp_1943.685)

```
(n / no
  :mod (o / oh
         :mode expressive))
```
686. Little glittering objects . " (lpp_1943.686)

```
(o / object
  :mod (l / little)
  :ARG0-of (g / glitter-01))
```
687. " Bees ? " (lpp_1943.687)

```
(b / bee
  :mode interrogative)
```
688. " Oh , no . (lpp_1943.688)

```
(n / no
  :mod (o / oh
         :mode expressive))
```
689. Little golden objects that set lazy men to idle dreaming . (lpp_1943.689)

```
(c / cause-01
  :ARG0 (o / object
          :consist-of (g / gold)
          :mod (l / little))
  :ARG1 (d / dream-01
          :ARG0 (m / man
                  :mod (l2 / lazy))
          :manner (i / idle-01)))
```
690. As for me , I am concerned with matters of consequence . (lpp_1943.690)

```
(c / concern-01
  :ARG0 (m / matter
          :mod (c2 / consequence))
  :ARG1 (i / i))
```
691. There is no time for idle dreaming in my life . " (lpp_1943.691)

```
(t2 / time :polarity -
      :purpose (d2 / dream-01
            :manner (i2 / idle))
      :duration (l / live-01
            :ARG0 (i / i)))
```
692. " Ah ! (lpp_1943.692)

```
(a / ah :mode expressive)
```
693. You mean the stars ? " (lpp_1943.693)

```
(m / mean-01 :mode interrogative
      :ARG0 (y / you)
      :ARG2 (s / star))
```
694. " Yes , that 's it . (lpp_1943.694)

```
(t / that-is-it-00)
```
695. The stars . " (lpp_1943.695)

```
(s / star)
```
696. " And what do you do with five - hundred millions of stars ? " (lpp_1943.696)

```
(a / and
  :op2 (d / do-02
         :ARG0 (y / you)
         :ARG1 (a2 / amr-unknown)
         :ARG3 (s / star
                 :quant 500000000)))
```
697. " Five - hundred - and - one million , six - hundred - twenty - two thousand , seven - hundred - thirty - one . (lpp_1943.697)

```
(h / have-quant-91
      :ARG2 501622731)
```
698. I am concerned with matters of consequence : I am accurate . " (lpp_1943.698)

```
(a / and
      :op1 (c / concern-01
            :ARG0 (m / matter
                  :mod (c2 / consequence))
            :ARG1 (i / i))
      :op2 (a2 / accurate
            :domain i))
```
699. " And what do you do with these stars ? " (lpp_1943.699)

```
(a / and
      :op2 (d / do-02
            :ARG0 (y / you)
            :ARG1 (a2 / amr-unknown)
            :ARG3 (s / star
                  :mod (t / this))))
```
700. " What do I do with them ? " (lpp_1943.700)

```
(d / do-02
  :ARG0 (i / i)
  :ARG1 (a / amr-unknown)
  :ARG3 (t / they))
```
701. " Yes . " (lpp_1943.701)

```
(y / yes)
```
702. " Nothing . (lpp_1943.702)

```
(n / nothing)
```
703. I own them . " (lpp_1943.703)

```
(o / own-01
  :ARG0 (i / i)
  :ARG1 (t / they))
```
704. " You own the stars ? " (lpp_1943.704)

```
(o / own-01
  :ARG0 (y / you)
  :ARG1 (s / star)
  :mode interrogative)
```
705. " Yes . " (lpp_1943.705)

```
(y / yes)
```
706. " But I have already seen a king who - - " (lpp_1943.706)

```
(c / contrast-01
      :ARG2 (s / see-01
            :ARG0 (i / i)
            :ARG1 (k / king)
            :time (a / already)))
```
707. " Kings do not own , they reign over . (lpp_1943.707)

```
(c / contrast-01
      :ARG1 (o / own-01 :polarity -
            :ARG0 (k / king))
      :ARG2 (r / reign-01
            :ARG0 k))
```
708. It is a very different matter . " (lpp_1943.708)

```
(m / matter
      :ARG1-of (d / differ-02
            :degree (v / very))
      :domain (i / it))
```
709. " And what good does it do you to own the stars ? " (lpp_1943.709)

```
(a / and
      :op2 (c / cause-01
            :ARG0 (o / own-01
                  :ARG1 (s / star))
            :ARG1 (g / good-04
                  :ARG1 (a2 / amr-unknown)
                  :ARG2 (y / you))))
```
710. " It does me the good of making me rich . " (lpp_1943.710)

```
(c / cause-01
      :ARG0 (i2 / it)
      :ARG1 (g / good-04
            :ARG1 (m2 / make-02
                  :ARG1 (r / rich
                        :domain i))
            :ARG2 (i / i)))
```
711. " And what good does it do you to be rich ? " (lpp_1943.711)

```
(a / and
      :op2 (c / cause-01
            :ARG0 (r / rich
                  :domain (y / you))
            :ARG1 (g / good-04
                  :ARG1 (a2 / amr-unknown)
                  :ARG2 y)))
```
712. " It makes it possible for me to buy more stars , if any are ever discovered . " (lpp_1943.712)

```
(p / possible-01
  :ARG1 (b / buy-01
            :ARG0 (i / i)
            :ARG1 (s / star
                    :degree (m / more)))
  :condition (d / discover-01
               :ARG1 s
               :time (e / ever)))
```
713. " This man , " the little prince said to himself , " reasons a little like my poor tippler ... " (lpp_1943.713)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (r / reason-01
            :ARG0 (m / man
                  :mod (t2 / this))
            :ARG1-of (r2 / resemble-01
                  :ARG2 (r3 / reason-01
                        :ARG0 (p2 / person
                              :ARG0-of (t / tipple-01)
                              :mod (p3 / poor)
                              :poss p))
                  :degree (l2 / little)))
      :ARG2 p)
```
714. Nevertheless , he still had some more questions . (lpp_1943.714)

```
(h3 / have-concession-91
      :ARG1 (h / have-03
            :ARG0 (h2 / he)
            :ARG1 (t / thing
                  :degree (m / more)
                  :mod (s / some)
                  :ARG1-of (q / question-01))
            :mod (s2 / still)))
```
715. " How is it possible for one to own the stars ? " (lpp_1943.715)

```
(p / possible-01
      :ARG1 (o / own-01
            :ARG0 (o2 / one)
            :ARG1 (s / star))
      :manner (a / amr-unknown))
```
716. " To whom do they belong ? " the businessman retorted , peevishly . (lpp_1943.716)

```
(r / retort-01
      :ARG0 (b3 / businessman)
      :ARG2 (b2 / belong-01
            :ARG0 (t / they)
            :ARG1 (a / amr-unknown))
      :manner (p / peevish))
```
717. " I do n't know . (lpp_1943.717)

```
(k / know-01
  :ARG0 (i / i)
  :polarity -)
```
718. To nobody . " (lpp_1943.718)

```
(b / belong-01
      :ARG1 (n / nobody))
```
719. " Then they belong to me , because I was the first person to think of it . " (lpp_1943.719)

```
(b / belong-01
  :ARG0 (t / they)
  :ARG1 (i / i)
  :ARG1-of (c / cause-01
             :ARG0 (p / person
                     :ord (o / ordinal-entity :value 1)
                     :domain i
                     :ARG0-of (t2 / think-01
                                :ARG2 (i2 / it)))))
```
720. " Is that all that is necessary ? " (lpp_1943.720)

```
(a / all :mode interrogative
      :domain (t2 / that)
      :ARG1-of (n / need-01))
```
721. " Certainly . (lpp_1943.721)

```
(c / certain)
```
722. When you find a diamond that belongs to nobody , it is yours . (lpp_1943.722)

```
(b / belong-01
      :ARG0 d
      :ARG1 (y / you)
      :condition (f / find-01
            :ARG0 y
            :ARG1 (d / diamond
                  :ARG0-of (b2 / belong-01
                        :ARG1 (n / nobody)))))
```
723. When you discover an island that belongs to nobody , it is yours . (lpp_1943.723)

```
(b / belong-01
  :ARG0 i
  :ARG1 (y / you)
  :condition (d / discover-01
               :ARG0 y
               :ARG1 (i / island
                       :ARG0-of (b2 / belong-01
                                  :ARG1 (n / nobody)))))
```
724. When you get an idea before any one else , you take out a patent on it : it is yours . (lpp_1943.724)

```
(a / and
  :op1 (p / patent-01
         :ARG0 y
         :ARG1 i)
  :op2 (b2 / belong-01
         :ARG0 i
         :ARG1 (y / you))
  :condition (g / get-01
               :ARG0 y
               :ARG1 (i / idea)
               :time (b / before
                       :op1 (a3 / anyone
                              :mod (e / else)))))
```
725. So with me : I own the stars , because nobody else before me ever thought of owning them . " (lpp_1943.725)

```
(c / cause-01
      :ARG0 (t / think-01
            :ARG0 (n / nobody
                  :mod (e2 / else))
            :ARG1 (o / own-01
                  :ARG0 n
                  :ARG1 (s / star))
            :time (e / ever)
            :time (b / before
                  :op1 (i / i)))
      :ARG1 (o2 / own-01
            :ARG0 i
            :ARG1 s)
      :ARG1-of (r / resemble-01
            :beneficiary i))
```
726. " Yes , that is true , " said the little prince . (lpp_1943.726)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (t / true-01
            :ARG1 (t2 / that)))
```
727. " And what do you do with them ? " (lpp_1943.727)

```
(a / and
  :op2 (d / do-02
         :ARG0 (y / you)
         :ARG1 (a2 / amr-unknown)
         :ARG2 (t / they)))
```
728. " I administer them , " replied the businessman . (lpp_1943.728)

```
(r / reply-01
      :ARG0 (b / businessman)
      :ARG2 (a / administer-01
            :ARG0 b
            :ARG1 (t / they)))
```
729. " I count them and recount them . (lpp_1943.729)

```
(a / and
  :op1 (c / count-01
         :ARG0 (i / i)
         :ARG1 (t / they))
  :op2 (r2 / recount-01
         :ARG0 i
         :ARG1 t))
```
730. It is difficult . (lpp_1943.730)

```
(d / difficult
  :domain (i / it))
```
731. But I am a man who is naturally interested in matters of consequence . " (lpp_1943.731)

```
(c / contrast-01
      :ARG2 (m / man
            :domain (i / i)
            :ARG1-of (i2 / interest-01
                  :ARG2 (m2 / matter
                        :mod (c2 / consequence))
                  :ARG1-of (n / natural-02
                        :ARG2 i))))
```
732. The little prince was still not satisfied . (lpp_1943.732)

```
(s / satisfy-01
  :ARG1 (p / prince
          :mod (l / little))
  :mod (s2 / still)
  :polarity -)
```
733. " If I owned a silk scarf , " he said , " I could put it around my neck and take it away with me . (lpp_1943.733)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (p / possible-01
            :ARG1 (a2 / and
                  :op1 (p2 / put-01
                        :ARG0 h
                        :ARG1 (s2 / scarf
                              :consist-of (s3 / silk))
                        :ARG2 (a / around
                              :op1 (n / neck
                                    :part-of h)))
                  :op2 (t / take-away-05
                        :ARG0 h
                        :ARG1 s2
                        :accompanier h))
            :condition (o / own-01
                  :ARG0 h
                  :ARG1 s2)))
```
734. If I owned a flower , I could pluck that flower and take it away with me . (lpp_1943.734)

```
(p / possible-01
      :ARG1 (a / and
            :op1 (p2 / pluck-01
                  :ARG0 (i / i)
                  :ARG1 (f2 / flower
                        :mod (t / that)))
            :op2 (t2 / take-away-05
                  :ARG0 i
                  :ARG1 f2
                  :accompanier i))
      :condition (o / own-01
            :ARG0 i
            :ARG1 f2))
```
735. But you can not pluck the stars from heaven ... " (lpp_1943.735)

```
(c / contrast-01
  :ARG2 (p2 / possible-01
          :polarity -
          :ARG1 (p / pluck-01
                    :ARG0 (y / you)
                    :ARG1 (s / star)
                    :ARG2 (h / heaven))))
```
736. " No . (lpp_1943.736)

```
(n / no)
```
737. But I can put them in the bank . " (lpp_1943.737)

```
(c / contrast-01
      :ARG2 (p2 / possible-01
            :ARG1 (p / put-01
                  :ARG0 (i / i)
                  :ARG1 (t / they)
                  :ARG2 (b / bank))))
```
738. " Whatever does that mean ? " (lpp_1943.738)

```
(m / mean-01
      :ARG1 (t / that)
      :ARG2 (a / amr-unknown))
```
739. " That means that I write the number of my stars on a little paper . (lpp_1943.739)

```
(m / mean-01
      :ARG1 (t / that)
      :ARG2 (w / write-01
            :ARG0 (i / i)
            :ARG1 (n / number
                  :quant-of (s / star
                        :poss i))
            :location (p / paper
                  :mod (l / little))))
```
740. And then I put this paper in a drawer and lock it with a key . " (lpp_1943.740)

```
(a / and
      :op2 (a2 / and
            :op1 (p / put-01
                  :ARG0 (i / i)
                  :ARG1 (p2 / paper
                        :mod (t2 / this))
                  :ARG2 (d / drawer))
            :op2 (l / lock-01
                  :ARG0 i
                  :ARG1 d
                  :ARG3 (k / key)))
      :time (t / then))
```
741. " And that is all ? " (lpp_1943.741)

```
(a / and
  :op2 (a2 / all
         :domain (t / that))
  :mode interrogative)
```
742. " That is enough , " said the businessman . (lpp_1943.742)

```
(s / say-01
      :ARG0 (b2 / businessman)
      :ARG1 (e / enough
            :domain (t / that)))
```
743. " It is entertaining , " thought the little prince . (lpp_1943.743)

```
(t / think-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (e / entertain-01
          :ARG0 (i / it)))
```
744. " It is rather poetic . (lpp_1943.744)

```
(p / poetry
  :domain (i / it)
  :degree (r / rather))
```
745. But it is of no great consequence . " (lpp_1943.745)

```
(c / contrast-01
  :ARG2 (c2 / consequence
          :domain (i / it)
          :mod (g / great
                 :polarity -)))
```
746. On matters of consequence , the little prince had ideas which were very different from those of the grown - ups . (lpp_1943.746)

```
(h / have-03
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (i / idea
            :topic (m / matter
                  :mod (c / consequence))
            :ARG1-of (d / differ-02
                  :ARG2 (i2 / idea
                        :poss (g / grown-up))
                  :degree (v / very))))
```
747. " I myself own a flower , " he continued his conversation with the businessman , " which I water every day . (lpp_1943.747)

```
(c / continue-02
      :ARG0 (h / he)
      :ARG1 (o / own-01
            :ARG0 h
            :ARG1 (f2 / flower
                  :ARG1-of (w / water-01
                        :ARG0 h
                        :frequency (r / rate-entity-91
                              :ARG3 (t / temporal-quantity :quant 1
                                    :unit (d / day))))))
      :ARG2 (b / businessman)
      :ARG3 (c2 / converse-01
            :ARG0 h
            :ARG2 b))
```
748. I own three volcanoes , which I clean out every week ( for I also clean out the one that is extinct ; one never knows ) . (lpp_1943.748)

```
(o / own-01
      :ARG0 (i / i)
      :ARG1 (v / volcano :quant 3
            :ARG1-of (c / clean-out-03
                  :ARG0 i
                  :frequency (r / rate-entity-91
                        :ARG3 (t / temporal-quantity :quant 1
                              :unit (w / week)))
                  :ARG1-of (c2 / cause-01
                        :ARG0 (c3 / clean-out-03
                              :ARG0 i
                              :ARG1 (v2 / volcano
                                    :mod (e / extinct)
                                    :ARG1-of (i2 / include-91
                                          :ARG2 v))
                              :mod (a / also)
                              :ARG1-of (c4 / cause-01
                                    :ARG0 (k / know-01 :polarity -
                                          :ARG0 (o2 / one))))))))
```
749. It is of some use to my volcanoes , and it is of some use to my flower , that I own them . (lpp_1943.749)

```
(c / cause-01
      :ARG0 (o / own-01
            :ARG0 (i / i)
            :ARG1 (a / and
                  :op1 v
                  :op2 f2))
      :ARG1 (u / use-01
            :beneficiary (a2 / and
                  :op1 (v / volcano
                        :poss i)
                  :op2 (f2 / flower
                        :poss i))
            :degree (s / some)))
```
750. But you are of no use to the stars ... " (lpp_1943.750)

```
(c / contrast-01
      :ARG2 (u / use-01 :polarity -
            :ARG0 (s / star)
            :ARG1 (y / you)))
```
751. The businessman opened his mouth , but he found nothing to say in answer . (lpp_1943.751)

```
(c / contrast-01
      :ARG1 (o / open-01
            :ARG0 (b / businessman)
            :ARG1 (m / mouth
                  :part-of b))
      :ARG2 (f / find-01
            :ARG0 b
            :ARG1 (a / answer-01 :polarity -)))
```
752. And the little prince went away . (lpp_1943.752)

```
(a / and
      :op2 (g / go-02
            :ARG0 (p / prince
                  :mod (l / little))
            :direction (a2 / away)))
```
753. " The grown - ups are certainly altogether extraordinary , " he said simply , talking to himself as he continued on his journey . (lpp_1943.753)

```
(s / say-01
      :ARG0 (h / he
            :ARG0-of (t / talk-01
                  :ARG2 h
                  :time (c2 / continue-01
                        :ARG0 h
                        :ARG1 (j / journey-01
                              :ARG0 h))))
      :ARG1 (e / extraordinary
            :domain (g2 / grown-up)
            :mod (c / certain)
            :degree (a / altogether))
      :ARG1-of (s2 / simple-02))
```
754. Chapter 14 . (lpp_1943.754)

```
(c / chapter
  :mod 14)
```
755. The fifth planet was very strange . (lpp_1943.755)

```
(s / strange
  :degree (v / very)
  :domain (p / planet
            :ord (o / ordinal-entity :value 5)))
```
756. It was the smallest of all . (lpp_1943.756)

```
(s / small
  :compared-to (a / all)
  :degree (m / most)
  :domain (i / it))
```
757. There was just enough room on it for a street lamp and a lamplighter . (lpp_1943.757)

```
(a2 / accommodate-01
  :ARG0 (i / it)
  :ARG1 (a / and
          :op1 (l / lamp
                 :mod (s / street))
          :op2 (p / person
                 :ARG0-of (l2 / light-04
                            :ARG1 (l3 / lamp))))
  :extent (e / enough
            :mod (j / just)))
```
758. The little prince was not able to reach any explanation of the use of a street lamp and a lamplighter , somewhere in the heavens , on a planet which had no people , and not one house . (lpp_1943.758)

```
(p / possible-01 :polarity -
      :ARG1 (e / explain-01
            :ARG0 (p2 / prince
                  :mod (l / little))
            :ARG1 (u / use-01
                  :ARG1 (a / and
                        :op1 (l2 / lamp
                              :mod (s / street))
                        :op2 (p3 / person
                              :ARG0-of (l3 / light-04
                                    :ARG1 (l4 / lamp)))
                        :location (r / relative-position
                              :op1 (h / heaven)
                              :location (p4 / planet
                                    :ARG0-of (h2 / have-03 :polarity -
                                          :ARG1 (a2 / and
                                                :op1 (p5 / person)
                                                :op2 (h3 / house)))))))))
```
759. But he said to himself , nevertheless : " It may well be that this man is absurd . (lpp_1943.759)

```
(h2 / have-concession-91
  :ARG1 (s / say-01
          :ARG0 (h / he)
          :ARG1 (p / possible-01
                  :ARG1 (a / absurd
                            :domain (m / man
                                      :mod (t / this))))
          :ARG2 h))
```
760. But he is not so absurd as the king , the conceited man , the businessman , and the tippler . (lpp_1943.760)

```
(c / contrast-01
      :ARG2 (a / absurd :polarity -
            :domain (h / he)
            :compared-to (a2 / and
                  :op1 (k / king)
                  :op2 (m / man
                        :mod (c2 / conceit))
                  :op3 (b2 / businessman)
                  :op4 (p / person
                        :ARG0-of (t / tipple-01)))
            :degree (e / equal)))
```
761. For at least his work has some meaning . (lpp_1943.761)

```
(c / cause-01
      :ARG0 (m / mean-01
            :ARG1 (w / work-01
                  :ARG0 (h / he))
            :degree (s / some)
            :mod (a / at-least)))
```
762. When he lights his street lamp , it is as if he brought one more star to life , or one flower . (lpp_1943.762)

```
(l2 / light-04
      :ARG0 h
      :ARG1 (l3 / lamp
            :mod (s2 / street)
            :poss h)
      :ARG1-of (r / resemble-01
            :ARG2 (b / bring-01
                  :ARG0 (h / he)
                  :ARG1 (o / or
                        :op1 (s / star :quant 1
                              :mod (m / more))
                        :op2 (f2 / flower))
                  :ARG3 (l / live-01))))
```
763. When he puts out his lamp , he sends the flower , or the star , to sleep . (lpp_1943.763)

```
(s / send-02
      :ARG0 (h / he)
      :ARG1 (o / or
            :op1 (f2 / flower)
            :op2 (s3 / star))
      :ARG2 (s2 / sleep-01
            :ARG0 o)
      :time (p / put-out-09
            :ARG0 h
            :ARG1 (l / lamp
                  :poss h)))
```
764. That is a beautiful occupation . (lpp_1943.764)

```
(o / occupation
      :ARG1-of (b / beautiful-02)
      :domain (t / that))
```
765. And since it is beautiful , it is truly useful . " (lpp_1943.765)

```
(a / and
      :op2 (c / cause-01
            :ARG0 (b / beautiful-02
                  :ARG1 (i / it))
            :ARG1 (u / useful-05
                  :ARG1 i
                  :degree (t / truly))))
```
766. When he arrived on the planet he respectfully saluted the lamplighter . (lpp_1943.766)

```
(s / salute-01
  :ARG0 (h / he)
  :ARG1 (p / person
          :ARG0-of (l / light-04
                     :ARG1 (l2 / lamp)))
  :manner (r / respect-01)
  :time (a / arrive-01
          :ARG1 h
          :ARG4 (p2 / planet)))
```
767. " Good morning . (lpp_1943.767)

```
(m / morning
      :ARG1-of (g / good-02))
```
768. Why have you just put out your lamp ? " (lpp_1943.768)

```
(c / cause-01
  :ARG0 (a / amr-unknown)
  :ARG1 (p / put-out-09
          :ARG0 (y / you)
          :ARG1 (l / lamp
                  :poss y)
          :mod (j / just)))
```
769. " Those are the orders , " replied the lamplighter . (lpp_1943.769)

```
(r / reply-01
  :ARG0 (p / person
          :ARG0-of (l / light-04
                     :ARG1 (l2 / lamp)))
  :ARG2 (o / order-01
          :ARG2 (t / that)))
```
770. " Good morning . " (lpp_1943.770)

```
(m / morning
      :ARG1-of (g / good-02))
```
771. " What are the orders ? " (lpp_1943.771)

```
(o / order-01
  :ARG2 (a / amr-unknown))
```
772. " The orders are that I put out my lamp . (lpp_1943.772)

```
(o / order-01
  :ARG2 (p / put-out-09
          :ARG0 (i / i)
          :ARG1 (l / lamp
                  :poss i)))
```
773. Good evening . " (lpp_1943.773)

```
(e / evening
      :ARG1-of (g / good-02))
```
774. And he lighted his lamp again . (lpp_1943.774)

```
(a / and
  :op2 (l / light-04
         :ARG0 (h / he)
         :ARG1 (l2 / lamp
                 :poss h)
         :mod (a2 / again)))
```
775. " But why have you just lighted it again ? " (lpp_1943.775)

```
(c / contrast-01
  :ARG2 (c2 / cause-01
          :ARG0 (a / amr-unknown)
          :ARG1 (l / light-04
                  :ARG0 (y / you)
                  :ARG1 (i / it)
                  :mod (a2 / again)
                  :mod (j / just))))
```
776. " Those are the orders , " replied the lamplighter . (lpp_1943.776)

```
(r / reply-01
  :ARG0 (p / person
          :ARG0-of (l / light-04
                     :ARG1 (l2 / lamp)))
  :ARG2 (o / order-01
          :ARG2 (t / that)))
```
777. " I do not understand , " said the little prince . (lpp_1943.777)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (u / understand-01
          :ARG0 p
          :polarity -))
```
778. " There is nothing to understand , " said the lamplighter . (lpp_1943.778)

```
(s / say-01
      :ARG0 (p / person
            :ARG0-of (l / light-04
                  :ARG1 (l2 / lamp)))
      :ARG1 (n / nothing
            :ARG1-of (u / understand-01)))
```
779. " Orders are orders . (lpp_1943.779)

```
(o / order
  :domain (o2 / order))
```
780. Good morning . " (lpp_1943.780)

```
(m / morning
      :ARG1-of (g / good-02))
```
781. And he put out his lamp . (lpp_1943.781)

```
(a / and
  :op2 (p / put-out-09
         :ARG0 (h / he)
         :ARG1 (l / lamp
                 :poss h)))
```
782. Then he mopped his forehead with a handkerchief decorated with red squares . (lpp_1943.782)

```
(m / mop-01
      :ARG0 (h / he)
      :ARG1 (f / forehead
            :part-of h)
      :ARG2 (h2 / handkerchief
            :ARG1-of (d / decorate-01
                  :ARG2 (s / square
                        :ARG1-of (r / red-02))))
      :time (t / then))
```
783. " I follow a terrible profession . (lpp_1943.783)

```
(f / follow-02
      :ARG0 (i / i)
      :ARG1 (p / profession
            :ARG1-of (t / terrible-01)))
```
784. In the old days it was reasonable . (lpp_1943.784)

```
(r / reasonable-02
      :ARG1 (i / it)
      :time (d / day
            :mod (o / old)))
```
785. I put the lamp out in the morning , and in the evening I lighted it again . (lpp_1943.785)

```
(a / and
  :op1 (p / put-out-09
         :ARG0 (i / i)
         :ARG1 (l / lamp)
         :time (d2 / date-entity :dayperiod (m / morning)))
  :op2 (l2 / light-04
         :ARG0 i
         :ARG1 l
         :time (d / date-entity :dayperiod (e / evening))
         :mod (a2 / again)))
```
786. I had the rest of the day for relaxation and the rest of the night for sleep . " (lpp_1943.786)

```
(h / have-03
      :ARG0 (i / i)
      :ARG1 (a / and
            :op1 (r / rest
                  :purpose (r2 / relax-01)
                  :part-of (d / day))
            :op2 (r3 / rest
                  :purpose (s / sleep-01)
                  :part-of (n / night))))
```
787. " And the orders have been changed since that time ? " (lpp_1943.787)

```
(a / and
      :op2 (c / change-01 :mode interrogative
            :ARG1 (o / order-01)
            :time (s / since
                  :op1 (t / time
                        :mod (t2 / that)))))
```
788. " The orders have not been changed , " said the lamplighter . (lpp_1943.788)

```
(s / say-01
  :ARG0 (p / person
          :ARG0-of (l / light-04
                     :ARG1 (l2 / lamp)))
  :ARG1 (c / change-01
          :ARG1 (o / order-01)
          :polarity -))
```
789. " That is the tragedy ! (lpp_1943.789)

```
(t / tragedy
      :domain (t2 / that))
```
790. From year to year the planet has turned more rapidly and the orders have not been changed ! " (lpp_1943.790)

```
(a / and
  :op1 (t / turn-01
         :ARG1 (p / planet)
         :manner (r / rapid
                   :degree (m / more))
         :frequency (y / year))
  :op2 (c / change-01
         :ARG1 (o / order-01)
         :polarity -))
```
791. " Then what ? " asked the little prince . (lpp_1943.791)

```
(a / ask-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (a2 / amr-unknown
          :time (t / then)))
```
792. " Then - - the planet now makes a complete turn every minute , and I no longer have a single second for repose . (lpp_1943.792)

```
(a / and
      :op1 (t / turn-01
            :ARG1 (p / planet)
            :ARG1-of (c / complete-02)
            :time (n / now)
            :frequency (r2 / rate-entity-91
                  :ARG3 (t3 / temporal-quantity :quant 1
                        :unit (m / minute))))
      :op2 (h / have-03 :polarity -
            :ARG0 (i / i)
            :ARG1 (t2 / temporal-quantity :quant 1
                  :unit (s / second)
                  :purpose (r / repose-01))
            :time (n2 / no-longer))
      :time (t4 / then))
```
793. Once every minute I have to light my lamp and put it out ! " (lpp_1943.793)

```
(o / obligate-01
      :ARG1 (i / i)
      :ARG2 (a / and
            :op1 (l / light-04
                  :ARG0 i
                  :ARG1 (l2 / lamp
                        :poss i))
            :op2 (p / put-out-09
                  :ARG0 i
                  :ARG1 l2))
      :frequency (r / rate-entity-91
            :ARG2 (t / temporal-quantity :quant 1
                  :unit (m / minute))))
```
794. " That is very funny ! (lpp_1943.794)

```
(f / funny
  :degree (v / very)
  :domain (t / that))
```
795. A day lasts only one minute , here where you live ! " (lpp_1943.795)

```
(l / last-01
      :ARG1 (t / temporal-quantity :quant 1
            :unit (d / day))
      :ARG2 (t2 / temporal-quantity :quant 1
            :unit (m / minute))
      :mod (o / only)
      :location (l2 / live-01
            :ARG0 (y / you)))
```
796. " It is not funny at all ! " said the lamplighter . (lpp_1943.796)

```
(s / say-01
      :ARG0 (p / person
            :ARG0-of (l / light-04
                  :ARG1 (l2 / lamp)))
      :ARG1 (f / funny :polarity -
            :domain (i / it)
            :degree (a / at-all)))
```
797. " While we have been talking together a month has gone by . " (lpp_1943.797)

```
(p / pass-03
      :ARG1 (t / temporal-quantity :quant 1
            :unit (m / month))
      :duration-of (t2 / talk-01
            :ARG0 (w / we)
            :mod (t3 / together)))
```
798. " A month ? " (lpp_1943.798)

```
(t / temporal-quantity :mode interrogative :quant 1
      :unit (m / month))
```
799. " Yes , a month . (lpp_1943.799)

```
(t / temporal-quantity
  :unit (m / month)
  :quant 1)
```
800. Thirty minutes . (lpp_1943.800)

```
(t / temporal-quantity
  :unit (m / minute)
  :quant 30)
```
801. Thirty days . (lpp_1943.801)

```
(t / temporal-quantity
  :unit (d / day)
  :quant 30)
```
802. Good evening . " (lpp_1943.802)

```
(e / evening
      :ARG1-of (g / good-02))
```
803. And he lighted his lamp again . (lpp_1943.803)

```
(a / and
  :op2 (l / light-04
         :ARG0 (h / he)
         :ARG1 (l2 / lamp
                 :poss h)
         :mod (a2 / again)))
```
804. As the little prince watched him , he felt that he loved this lamplighter who was so faithful to his orders . (lpp_1943.804)

```
(f / feel-01
      :ARG0 (p / prince
            :mod (l2 / little))
      :ARG1 (l / love-01
            :ARG0 p
            :ARG1 (p2 / person
                  :ARG0-of (l3 / light-04
                        :ARG1 (l4 / lamp))
                  :mod (t / this)
                  :ARG1-of (f2 / faithful-00
                        :ARG2 (t2 / thing
                              :ARG2-of (o / order-01
                                    :ARG1 p2)))))
      :time (w / watch-01
            :ARG0 p
            :ARG1 p2))
```
805. He remembered the sunsets which he himself had gone to seek , in other days , merely by pulling up his chair ; and he wanted to help his friend . (lpp_1943.805)

```
(a / and
      :op1 (r / remember-01
            :ARG0 (h / he)
            :ARG1 (s3 / sunset
                  :ARG1-of (s / seek-01
                        :purpose-of (g / go-02
                              :ARG0 h
                              :manner (p / pull-01
                                    :ARG0 h
                                    :ARG1 (c / chair)
                                    :mod (m / mere)
                                    :direction (u / up))
                              :time (d / day
                                    :mod (o / other))))))
      :op2 (w / want-01
            :ARG0 h
            :ARG1 (h2 / help-01
                  :ARG0 h
                  :ARG1 (p2 / person
                        :ARG0-of (h3 / have-rel-role-91
                              :ARG1 h
                              :ARG2 (f / friend))))))
```
806. " You know , " he said , " I can tell you a way you can rest whenever you want to ... " (lpp_1943.806)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (p / possible-01
            :ARG1 (t / tell-01
                  :ARG0 h
                  :ARG1 (w / way
                        :purpose (p2 / possible-01
                              :ARG1 (r / rest-01
                                    :ARG1 (y / you)
                                    :time (w2 / want-01
                                          :ARG0 y
                                          :mod (a / any)))))
                  :ARG2 y)))
```
807. " I always want to rest , " said the lamplighter . (lpp_1943.807)

```
(s / say-01
      :ARG0 (p / person
            :ARG0-of (l / light-04
                  :ARG1 (l2 / lamp)))
      :ARG1 (w / want-01
            :ARG0 p
            :ARG1 (r / rest-01
                  :ARG1 p)
            :time (a / always)))
```
808. For it is possible for a man to be faithful and lazy at the same time . (lpp_1943.808)

```
(c / cause-01
  :ARG0 (p / possible-01
          :ARG1 (a / and
                    :op1 (f / faithful)
                    :op2 (l / lazy)
                    :domain (m / man)
                    :time (s / same-01
                            :ARG1 (t / time)))))
```
809. The little prince went on with his explanation : " Your planet is so small that three strides will take you all the way around it . (lpp_1943.809)

```
(g / go-on-25
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (e / explain-01
            :ARG0 p
            :ARG1 (c / cause-01
                  :ARG0 (s / small
                        :domain (p2 / planet
                              :poss (y / you))
                        :degree (s2 / so))
                  :ARG1 (t / take-03
                        :ARG0 (s3 / stride-01 :quant 3)
                        :ARG1 y
                        :ARG2 (a / around
                              :op1 p2
                              :degree (a2 / all-the-way))))))
```
810. To be always in the sunshine , you need only walk along rather slowly . (lpp_1943.810)

```
(n / need-01
      :ARG0 (y / you)
      :ARG1 (w / walk-01
            :ARG1-of (s / slow-05
                  :degree (r / rather))
            :mod (o / only))
      :purpose (b / be-located-at-91
            :ARG1 y
            :ARG2 (s2 / sunshine)
            :time (a / always)))
```
811. When you want to rest , you will walk - - and the day will last as long as you like . " (lpp_1943.811)

```
(w / walk-01
      :ARG0 (y / you)
      :time (w2 / want-01
            :ARG0 y
            :ARG1 (r / rest-01
                  :ARG1 y))
      :ARG0-of (c / cause-01
            :ARG1 (l / last-01
                  :ARG1 (d / day)
                  :ARG2 (t / temporal-quantity
                        :degree (e / equal)
                        :compared-to (l2 / like-02
                              :ARG0 y)))))
```
812. " That does n't do me much good , " said the lamplighter . (lpp_1943.812)

```
(s / say-01
      :ARG0 (p / person
            :ARG0-of (l / light-04
                  :ARG1 (l2 / lamp)))
      :ARG1 (d / do-02 :polarity -
            :ARG0 (t / that)
            :ARG1 (g / good-04
                  :ARG2 p
                  :degree (m / much))
            :ARG2 p))
```
813. " The one thing I love in life is to sleep . " (lpp_1943.813)

```
(l / love-01
      :ARG0 (i / i)
      :ARG1 (s / sleep-01
            :ARG0 i
            :mod (t / thing :quant 1))
      :time (l2 / live-01))
```
814. " Then you 're unlucky , " said the little prince . (lpp_1943.814)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (l2 / lucky :polarity -
            :domain (y / you)
            :time (t / then)))
```
815. " I am unlucky , " said the lamplighter . (lpp_1943.815)

```
(s / say-01
  :ARG0 (p / person
          :ARG0-of (l / light-04
                     :ARG1 (l2 / lamp)))
  :ARG1 (l3 / lucky
          :domain p
          :polarity -))
```
816. " Good morning . " (lpp_1943.816)

```
(m / morning
      :ARG1-of (g / good-02))
```
817. And he put out his lamp . (lpp_1943.817)

```
(a / and
  :op2 (p / put-out-09
         :ARG0 (h / he)
         :ARG1 (l / lamp
                 :poss h)))
```
818. " That man , " said the little prince to himself , as he continued farther on his journey , " that man would be scorned by all the others : by the king , by the conceited man , by the tippler , by the businessman . (lpp_1943.818)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (s2 / scorn-01
            :ARG0 (o / other
                  :mod (a / all)
                  :domain (a2 / and
                        :op1 (k / king)
                        :op2 (m / man
                              :mod (c / conceit))
                        :op3 (p2 / person
                              :ARG0-of (t / tipple-01))
                        :op4 (b / businessman)))
            :ARG1 (m2 / man
                  :mod (t2 / that)))
      :ARG2 p
      :time (c2 / continue-01
            :ARG0 p
            :ARG1 (j / journey-01
                  :ARG0 p)
            :extent (f / far
                  :degree (m3 / more))))
```
819. Nevertheless he is the only one of them all who does not seem to me ridiculous . (lpp_1943.819)

```
(h2 / have-concession-91
      :ARG1 (s / seem-01 :polarity -
            :ARG1 (r / ridiculous-02
                  :ARG1 (p / person
                        :mod (o2 / only)
                        :ARG1-of (i2 / include-91
                              :ARG2 (t / they
                                    :mod (a / all)))
                        :domain (h / he)))
            :ARG2 (i / i)))
```
820. Perhaps that is because he is thinking of something else besides himself . " (lpp_1943.820)

```
(p / possible-01
      :ARG1 (c / cause-01
            :ARG0 (t / think-01
                  :ARG0 (h / he)
                  :ARG2 (s / something
                        :mod (e / else)
                        :ARG1-of (d / differ-02
                              :ARG2 h)))))
```
821. He breathed a sigh of regret , and said to himself , again : " That man is the only one of them all whom I could have made my friend . (lpp_1943.821)

```
(a / and
      :op1 (b / breathe-02
            :ARG0 (h / he)
            :ARG1 (s / sigh-02
                  :manner (r / regret-01)))
      :op2 (s2 / say-01
            :ARG0 h
            :ARG1 (p / person
                  :mod (o2 / only)
                  :ARG1-of (i / include-91
                        :ARG2 (t / they
                              :mod (a2 / all)))
                  :domain (m2 / man
                        :mod (t2 / that))
                  :ARG2-of (m / make-01
                        :ARG0 h
                        :ARG1 (h2 / have-rel-role-91
                              :ARG0 p
                              :ARG1 h
                              :ARG2 (f / friend))
                        :ARG1-of (p2 / possible-01)))
            :ARG2 h
            :mod (a3 / again)))
```
822. But his planet is indeed too small . (lpp_1943.822)

```
(c / contrast-01
      :ARG2 (s / small
            :degree (t / too)
            :domain (p / planet
                  :poss (h / he))
            :mod (i / indeed)))
```
823. There is no room on it for two people ... " (lpp_1943.823)

```
(r / room
  :poss (i / it)
  :beneficiary (p / person
                 :quant 2)
  :polarity -)
```
824. What the little prince did not dare confess was that he was sorry most of all to leave this planet , because it was blest every day with 1440 sunsets ! (lpp_1943.824)

```
(d / dare-01 :polarity -
      :ARG0 (p / prince
            :mod (l / little))
      :ARG2 (c / confess-01
            :ARG1 (c2 / cause-01
                  :ARG0 (b / bless-01
                        :ARG1 (p2 / planet
                              :mod (t / this))
                        :ARG2 (s / sunset :quant 1440)
                        :frequency (r / rate-entity-91
                              :ARG3 (t2 / temporal-quantity :quant 1
                                    :unit (d2 / day))))
                  :ARG1 (s2 / sorry-01
                        :ARG1 p
                        :ARG2 (l2 / leave-11
                              :ARG1 p2))
                  :degree (m / most))))
```
825. Chapter 15 . (lpp_1943.825)

```
(c / chapter
  :mod 15)
```
826. The sixth planet was ten times larger than the last one . (lpp_1943.826)

```
(l / large
      :domain (p / planet
            :ord (o / ordinal-entity :value 6))
      :quant (p3 / product-of :op1 10
            :op2 (v / volume-quantity
                  :quant-of (p2 / planet
                        :mod (l2 / last)))))
```
827. It was inhabited by an old gentleman who wrote voluminous books . (lpp_1943.827)

```
(i / inhabit-01
  :ARG0 (g / gentleman
          :mod (o / old)
          :ARG0-of (w / write-01
                     :ARG1 (b / book
                             :mod (v / volume))))
  :ARG1 (i2 / it))
```
828. " Oh , look ! (lpp_1943.828)

```
(a / and
      :op1 (o / oh :mode expressive)
      :op2 (l / look-01 :mode imperative
            :ARG0 (y / you)))
```
829. Here is an explorer ! " he exclaimed to himself when he saw the little prince coming . (lpp_1943.829)

```
(e / exclaim-01
  :ARG0 (h / he)
  :ARG1 (p / person
          :ARG0-of (e2 / explore-01))
  :ARG2 h
  :time (s / see-01
          :ARG0 h
          :ARG1 (c / come-01
                  :ARG1 (p2 / prince
                          :mod (l / little)))))
```
830. The little prince sat down on the table and panted a little . (lpp_1943.830)

```
(a / and
  :op1 (s / sit-down-02
         :ARG1 (p2 / prince
                 :mod (l / little))
         :location (t / table))
  :op2 (p / pant-01
         :ARG0 p2
         :duration (l2 / little)))
```
831. He had already traveled so much and so far ! (lpp_1943.831)

```
(a2 / and
      :op1 (t / travel-01
            :ARG0 (h / he)
            :quant (m / much
                  :mod (s / so)))
      :op2 (t2 / travel-01
            :ARG0 h
            :ARG1 (f / far
                  :mod (s2 / so)))
      :time (a / already))
```
832. " Where do you come from ? " the old gentleman said to him . (lpp_1943.832)

```
(s / say-01
  :ARG0 (g / gentleman
          :mod (o / old))
  :ARG1 (c / come-01
          :ARG1 h
          :ARG3 (a / amr-unknown))
  :ARG2 (h / he))
```
833. " What is that big book ? " said the little prince . (lpp_1943.833)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (b / book
          :domain (a / amr-unknown)
          :mod (b2 / big)
          :mod (t / that)))
```
834. " What are you doing ? " (lpp_1943.834)

```
(d2 / do-02
  :ARG0 (y / you)
  :ARG1 (a / amr-unknown))
```
835. " I am a geographer , " the old gentleman said to him . (lpp_1943.835)

```
(s / say-01
  :ARG0 (g / gentleman
          :mod (o / old))
  :ARG1 (g2 / geographer
          :domain g)
  :ARG2 (h / he))
```
836. " What is a geographer ? " asked the little prince . (lpp_1943.836)

```
(a / ask-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (g / geographer
            :domain (a2 / amr-unknown)))
```
837. " A geographer is a scholar who knows the location of all the seas , rivers , towns , mountains , and deserts . " (lpp_1943.837)

```
(s4 / scholar
      :domain (g / geographer)
      :ARG0-of (k / know-01
            :ARG1 (l / location
                  :location-of (a / and
                        :op1 (s2 / sea)
                        :op2 (r / river)
                        :op3 (t / town)
                        :op4 (m / mountain)
                        :op5 (d / desert)
                        :mod (a2 / all)))))
```
838. " That is very interesting , " said the little prince . (lpp_1943.838)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (i / interest-01
            :ARG0 (t2 / that)
            :ARG1 p
            :degree (v / very)))
```
839. " Here at last is a man who has a real profession ! " (lpp_1943.839)

```
(m2 / man
      :ARG0-of (h2 / have-03
            :ARG1 (p2 / profession
                  :ARG1-of (r / real-04)))
      :time (a / at-last))
```
840. And he cast a look around him at the planet of the geographer . (lpp_1943.840)

```
(a / and
      :op2 (l / look-01
            :ARG0 (h / he)
            :ARG1 (p / planet
                  :poss (g / geographer))
            :direction (a2 / around
                  :op1 h)))
```
841. It was the most magnificent and stately planet that he had ever seen . (lpp_1943.841)

```
(p / planet
      :domain (i / it)
      :mod (m2 / magnificent
            :degree (m / most)
            :compared-to (p2 / planet
                  :ARG1-of (s2 / see-01
                        :ARG0 (h / he)
                        :time (e / ever))))
      :mod (s / stately
            :degree (m3 / most)
            :compared-to p2))
```
842. " Your planet is very beautiful , " he said . (lpp_1943.842)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (b / beautiful-02
            :ARG1 (p / planet
                  :poss (y / you))
            :degree (v / very)))
```
843. " Has it any oceans ? " (lpp_1943.843)

```
(h / have-03
      :ARG0 (i / it)
      :ARG1 (o / ocean
            :mod (a / any))
      :mode interrogative)
```
844. " I could n't tell you , " said the geographer . (lpp_1943.844)

```
(s / say-01
  :ARG0 (g / geographer)
  :ARG1 (p / possible-01
          :ARG1 (t / tell-01
                    :ARG0 g
                    :ARG2 (y / you))
          :polarity -))
```
845. " Ah ! " (lpp_1943.845)

```
(a / ah :mode expressive)
```
846. The little prince was disappointed . (lpp_1943.846)

```
(d / disappoint-01
      :ARG1 (p / prince
            :mod (l / little)))
```
847. " Has it any mountains ? " (lpp_1943.847)

```
(h2 / have-03 :mode interrogative
      :ARG0 (i / it)
      :ARG1 (m / mountain
            :mod (a / any)))
```
848. " I could n't tell you , " said the geographer . (lpp_1943.848)

```
(s / say-01
  :ARG0 (g / geographer)
  :ARG1 (p / possible-01
          :ARG1 (t / tell-01
                    :ARG0 g
                    :ARG2 (y / you))
          :polarity -))
```
849. " And towns , and rivers , and deserts ? " (lpp_1943.849)

```
(a3 / and
      :op2 (a4 / and
            :op1 (t2 / town)
            :op2 (r2 / river)
            :op3 (d2 / desert))
      :mode interrogative)
```
850. " I could n't tell you that , either . " (lpp_1943.850)

```
(p2 / possible-01 :polarity -
      :ARG1 (t / tell-01
            :ARG0 (i / i)
            :ARG1 (t2 / that)
            :ARG2 (y / you))
      :mod (e / either))
```
851. " But you are a geographer ! " (lpp_1943.851)

```
(c / contrast-01 :mode expressive
      :ARG2 (g2 / geographer
            :domain (y2 / you)))
```
852. " Exactly , " the geographer said . (lpp_1943.852)

```
(s / say-01
      :ARG0 (g / geographer)
      :ARG1 (e / exact))
```
853. " But I am not an explorer . (lpp_1943.853)

```
(c / contrast-01
      :ARG2 (p / person :polarity -
            :domain (i / i)
            :ARG0-of (e / explore-01)))
```
854. I have n't a single explorer on my planet . (lpp_1943.854)

```
(h2 / have-03 :polarity -
      :ARG0 (i / i)
      :ARG1 (p2 / person
            :ARG1-of (s / single-02)
            :ARG0-of (e / explore-01)
            :location (p3 / planet
                  :poss i)))
```
855. It is not the geographer who goes out to count the towns , the rivers , the mountains , the seas , the oceans , and the deserts . (lpp_1943.855)

```
(p2 / person
      :domain (g / geographer :polarity -)
      :ARG0-of (g2 / go-02
            :purpose (c / count-01
                  :ARG0 g
                  :ARG1 (a / and
                        :op1 (t / town)
                        :op2 (r / river)
                        :op3 (m / mountain)
                        :op4 (o2 / ocean)
                        :op5 (d / desert)
                        :op6 (s2 / sea)))))
```
856. The geographer is much too important to go loafing about . (lpp_1943.856)

```
(i2 / important
      :domain (g / geographer
            :ARG1-of (g2 / go-01
                  :purpose (l / loaf-01
                        :ARG0 g
                        :path (a / about))))
      :degree (t / too
            :degree (m / much)))
```
857. He does not leave his desk . (lpp_1943.857)

```
(l / leave-11 :polarity -
      :ARG0 (h / he)
      :ARG1 (d / desk
            :poss h))
```
858. But he receives the explorers in his study . (lpp_1943.858)

```
(c / contrast-01
      :ARG2 (r / receive-01
            :ARG0 (h / he)
            :ARG1 (p / person
                  :ARG0-of (e / explore-01))
            :location (s / study
                  :poss h)))
```
859. He asks them questions , and he notes down what they recall of their travels . (lpp_1943.859)

```
(a3 / and
      :op1 (q2 / question-01
            :ARG0 (h / he)
            :ARG2 (t / they))
      :op2 (n / note-02
            :ARG0 h
            :ARG1 (t3 / thing
                  :ARG1-of (r / recall-02)
                  :source (t2 / travel-01
                        :ARG0 t))))
```
860. And if the recollections of any one among them seem interesting to him , the geographer orders an inquiry into that explorer 's moral character . " (lpp_1943.860)

```
(a3 / and
      :op2 (o / order-02
            :ARG0 (g / geographer)
            :ARG1 (i / inquire-01
                  :ARG1 (c / character
                        :ARG1-of (m / moral-02)
                        :poss (p / person
                              :ARG0-of (e / explore-01)
                              :mod (t2 / that))))
            :condition (i4 / interest-01
                  :ARG1 g
                  :ARG2 (t4 / thing
                        :ARG1-of (r2 / recall-02)
                        :poss (p2 / person
                              :ARG0-of (e2 / explore-01)
                              :mod (a / any)
                              :ARG1-of (i5 / include-91
                                    :ARG2 (t5 / they)))))))
```
861. " Why is that ? " (lpp_1943.861)

```
(t2 / that
      :ARG1-of (c / cause-01
            :ARG0 (a / amr-unknown)))
```
862. " Because an explorer who told lies would bring disaster on the books of the geographer . (lpp_1943.862)

```
(c / cause-01
      :ARG1 (l / lie-08
            :ARG0 (p2 / person
                  :ARG0-of (e2 / explore-01))
            :condition-of (b3 / bring-01
                  :ARG1 (d2 / disaster)
                  :ARG2 (b4 / book
                        :poss (g2 / geographer)))))
```
863. So would an explorer who drank too much . " (lpp_1943.863)

```
(d3 / drink-01
      :ARG0 (p2 / person
            :ARG0-of (e2 / explore-01))
      :quant (m2 / much
            :degree (t2 / too))
      :ARG0-of (c / cause-01
            :ARG1 (t / thing
                  :ARG1-of (s / same-01))))
```
864. " Why is that ? " asked the little prince . (lpp_1943.864)

```
(a / ask-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (t / that
          :ARG1-of (c / cause-01
                     :ARG0 (a2 / amr-unknown))))
```
865. " Because intoxicated men see double . (lpp_1943.865)

```
(s3 / see-01
      :ARG0 (m2 / man
            :ARG1-of (i2 / intoxicate-01))
      :ARG2 (d / double)
      :ARG0-of (c2 / cause-01
            :ARG1 (t2 / thing)))
```
866. Then the geographer would note down two mountains in a place where there was only one . " (lpp_1943.866)

```
(t / thing
      :ARG0-of (c / cause-01
            :ARG1 (n2 / note-02
                  :ARG0 (g / geographer)
                  :ARG1 (m / mountain :quant 2
                        :location (p / place
                              :location-of (m2 / mountain :quant 1
                                    :mod (o2 / only))))
                  :time (t2 / then))))
```
867. " I know some one , " said the little prince , " who would make a bad explorer . " (lpp_1943.867)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (k / know-02
            :ARG0 p
            :ARG1 (s2 / someone
                  :ARG1-of (m / make-06
                        :ARG2 (p2 / person
                              :ARG0-of (e / explore-01)
                              :ARG1-of (b / bad-02
                                    :ARG2 e))))))
```
868. " That is possible . (lpp_1943.868)

```
(p2 / possible-01
      :ARG1 (t / that))
```
869. Then , when the moral character of the explorer is shown to be good , an inquiry is ordered into his discovery . " (lpp_1943.869)

```
(o2 / order-01
      :ARG1 (i / inquire-01
            :ARG1 (t / thing
                  :ARG1-of (d / discover-01
                        :ARG0 p)))
      :time (s3 / show-01
            :ARG1 (g / good-02
                  :ARG1 (c / character
                        :poss (p / person
                              :ARG0-of (e / explore-01))
                        :ARG1-of (m / moral-02))))
      :time (t3 / then))
```
870. " One goes to see it ? " (lpp_1943.870)

```
(g / go-02 :mode interrogative
      :ARG0 (o / one)
      :purpose (s2 / see-01
            :ARG0 o
            :ARG1 (i / it)))
```
871. " No . (lpp_1943.871)

```
(n / no)
```
872. That would be too complicated . (lpp_1943.872)

```
(c2 / complicate-01
      :ARG1 (t3 / that)
      :degree (t2 / too))
```
873. But one requires the explorer to furnish proofs . (lpp_1943.873)

```
(c / contrast-01
      :ARG2 (r / require-01
            :ARG0 (o / one)
            :ARG1 (f / furnish-01
                  :ARG0 p
                  :ARG1 (p2 / prove-01))
            :ARG2 (p / person
                  :ARG0-of (e / explore-01))))
```
874. For example , if the discovery in question is that of a large mountain , one requires that large stones be brought back from it . " (lpp_1943.874)

```
(e2 / exemplify-01
      :ARG0 (r / require-01
            :ARG0 (o / one)
            :ARG1 (b / bring-01
                  :ARG1 (s2 / stone
                        :mod (l2 / large))
                  :direction (b2 / back)
                  :source m)
            :condition (d / discover-01
                  :ARG1 (m / mountain
                        :mod (l / large))
                  :ARG1-of (q / question-01))))
```
875. The geographer was suddenly stirred to excitement . (lpp_1943.875)

```
(s / stir-02
  :ARG1 (g / geographer)
  :ARG3 (e / excite-01)
  :manner (s2 / sudden))
```
876. " But you - - you come from far away ! (lpp_1943.876)

```
(c3 / contrast-01
      :ARG2 (c / come-01
            :ARG1 (y / you)
            :ARG3 (a / away
                  :extent (f / far))))
```
877. You are an explorer ! (lpp_1943.877)

```
(p2 / person
      :ARG0-of (e / explore-01)
      :domain (y / you))
```
878. You shall describe your planet to me ! " (lpp_1943.878)

```
(d2 / describe-01 :mode imperative
      :ARG0 (y / you)
      :ARG1 (p / planet
            :source-of y)
      :beneficiary (i / i))
```
879. And , having opened his big register , the geographer sharpened his pencil . (lpp_1943.879)

```
(a / and
      :op2 (s / sharpen-01
            :ARG0 g
            :ARG1 (p / pencil
                  :poss g)
            :time (a3 / after
                  :op1 (o / open-01
                        :ARG0 (g / geographer)
                        :ARG1 (r / register-02
                              :ARG0 g
                              :mod (b / big))))))
```
880. The recitals of explorers are put down first in pencil . (lpp_1943.880)

```
(p / put-01
      :ARG1 (t / thing
            :ARG1-of (r / recite-01
                  :ARG0 (p2 / person
                        :ARG0-of (e / explore-01))))
      :direction (d / down)
      :time (f / first)
      :instrument (p3 / pencil))
```
881. One waits until the explorer has furnished proofs , before putting them down in ink . (lpp_1943.881)

```
(w / wait-01
      :ARG1 (o / one)
      :time (u / until
            :op1 (f / furnish-01
                  :ARG0 (p2 / person
                        :ARG0-of (e / explore-01))
                  :ARG1 (p / prove-01)))
      :time (b / before
            :op1 (p3 / put-01
                  :ARG0 o
                  :ARG1 (t / they)
                  :direction (d / down)
                  :instrument (i / ink))))
```
882. " Well ? " said the geographer expectantly . (lpp_1943.882)

```
(s / say-01
      :ARG0 (g / geographer)
      :ARG1 (w / well :mode interrogative)
      :manner (e / expect-01))
```
883. " Oh , where I live , " said the little prince , " it is not very interesting . (lpp_1943.883)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (a / and
            :op1 (o / oh
                  :mode expressive)
            :op2 (i2 / interest-01
                  :ARG0 (l2 / location
                        :location-of (l3 / live-01
                              :ARG0 p))
                  :ARG1 p
                  :degree (v / very)
                  :polarity -)))
```
884. It is all so small . (lpp_1943.884)

```
(s3 / small
      :domain (i / it
            :mod (a / all))
      :degree (s / so))
```
885. I have three volcanoes . (lpp_1943.885)

```
(h2 / have-03
      :ARG0 (i / i)
      :ARG1 (v / volcano
            :quant 3))
```
886. Two volcanoes are active and the other is extinct . (lpp_1943.886)

```
(a3 / and
      :op1 (a / activity-06
            :ARG0 (v / volcano :quant 2))
      :op2 (e / extinct
            :domain (o / other)))
```
887. But one never knows . " (lpp_1943.887)

```
(c / contrast-01
      :ARG2 (k / know-01
            :ARG0 (o / one)
            :polarity -
            :time (e / ever)))
```
888. " One never knows , " said the geographer . (lpp_1943.888)

```
(s / say-01
      :ARG0 (g / geographer)
      :ARG1 (k / know-01 :polarity -
            :ARG0 (o / one)
            :time (e / ever)))
```
889. " I have also a flower . " (lpp_1943.889)

```
(h2 / have-03
      :ARG0 (i / i)
      :ARG1 (t / thing
            :ARG1-of (f / flower-01))
      :mod (a2 / also))
```
890. " We do not record flowers , " said the geographer . (lpp_1943.890)

```
(s / say-01
  :ARG0 (g / geographer)
  :ARG1 (r / record-01
          :ARG0 (w / we)
          :ARG1 (t / thing
                  :ARG1-of (f / flower-01))
          :polarity -))
```
891. " Why is that ? (lpp_1943.891)

```
(t2 / that
      :ARG1-of (c / cause-01
            :ARG0 (a / amr-unknown)))
```
892. The flower is the most beautiful thing on my planet ! " (lpp_1943.892)

```
(t3 / thing
      :ARG1-of (b / beautiful-02
            :degree (m2 / most))
      :location (p / planet
            :source-of (i / i))
      :domain (t2 / thing
            :ARG1-of (f / flower-01)))
```
893. " We do not record them , " said the geographer , " because they are ephemeral . " (lpp_1943.893)

```
(s / say-01
      :ARG0 (g / geographer)
      :ARG1 (r / record-01 :polarity -
            :ARG0 (w / we)
            :ARG1 (t / they)
            :ARG1-of (c / cause-01
                  :ARG0 (e / ephemeral
                        :domain t))))
```
894. " What does that mean - - ' ephemeral ' ? " (lpp_1943.894)

```
(m2 / mean-01
      :ARG1 (e / ephemeral)
      :ARG2 (a / amr-unknown))
```
895. " Geographies , " said the geographer , " are the books which , of all books , are most concerned with matters of consequence . (lpp_1943.895)

```
(s / say-01
      :ARG0 (g / geographer)
      :ARG1 (b / book
            :domain (g2 / geography)
            :ARG1-of (i / include-91
                  :ARG2 (b2 / book
                        :mod (a / all)))
            :ARG0-of (c / concern-02
                  :ARG1 (m2 / matter
                        :mod (c2 / consequence))
                  :degree (m / most))))
```
896. They never become old - fashioned . (lpp_1943.896)

```
(b / become-01
      :ARG1 (t / they)
      :ARG2 (f / fashion
            :mod (o / old))
      :time (e / ever)
      :polarity -)
```
897. It is very rarely that a mountain changes its position . (lpp_1943.897)

```
(c / change-01
      :ARG0 (m / mountain)
      :ARG1 (l / location
            :ARG2-of (p / position-01
                  :ARG1 m))
      :ARG1-of (r / rare-02
            :degree (v / very)))
```
898. It is very rarely that an ocean empties itself of its waters . (lpp_1943.898)

```
(e / empty-01
      :ARG0 (o / ocean)
      :ARG1 o
      :ARG2 (w / water
            :poss o)
      :ARG1-of (r / rare-02
            :degree (v / very)))
```
899. We write of eternal things . " (lpp_1943.899)

```
(w3 / write-01
      :ARG0 (w2 / we)
      :ARG1 (t / thing
            :mod (e / eternal)))
```
900. " But extinct volcanoes may come to life again , " the little prince interrupted . (lpp_1943.900)

```
(i / interrupt-01
      :ARG0 (p2 / prince
            :mod (l / little))
      :ARG2 (c / contrast-01
            :ARG2 (p / possible-01
                  :ARG1 (c2 / come-04
                        :ARG1 (v / volcano
                              :mod (e / extinct))
                        :ARG2 (t / thing
                              :ARG1-of (l3 / live-01))
                        :mod (a / again)))))
```
901. " What does that mean - - ' ephemeral ' ? " (lpp_1943.901)

```
(m2 / mean-01
      :ARG1 (e / ephemeral)
      :ARG2 (a / amr-unknown))
```
902. " Whether volcanoes are extinct or alive , it comes to the same thing for us , " said the geographer . (lpp_1943.902)

```
(s / say-01
      :ARG0 (g / geographer)
      :ARG1 (s2 / same-01
            :ARG1 (e2 / extinct
                  :domain (v / volcano))
            :ARG2 (l2 / live-01
                  :ARG0 v)
            :ARG3 (w / we)))
```
903. " The thing that matters to us is the mountain . (lpp_1943.903)

```
(m3 / mountain
      :domain (t / thing
            :ARG1-of (m2 / matter-01
                  :ARG2 (w / we))))
```
904. It does not change . " (lpp_1943.904)

```
(c2 / change-01
      :ARG1 (i / it)
      :polarity -)
```
905. " But what does that mean - - ' ephemeral ' ? " repeated the little prince , who never in his life had let go of a question , once he had asked it . (lpp_1943.905)

```
(r / repeat-01
      :ARG0 (p / prince
            :mod (l / little)
            :ARG0-of (l2 / let-01 :polarity -
                  :ARG1 (g / go-02
                        :ARG0 (t / thing
                              :ARG1-of (q / question-01
                                    :ARG0 p)))
                  :time (o / once
                        :op1 (a2 / ask-01
                              :ARG1 t))
                  :time (e2 / ever
                        :duration (t2 / thing
                              :ARG1-of (l3 / live-01
                                    :ARG0 p)))))
      :ARG1 (c / contrast-01
            :ARG2 (m / mean-01
                  :ARG1 (e / ephemeral)
                  :ARG2 (a / amr-unknown))))
```
906. " It means , ' which is in danger of speedy disappearance . ' " (lpp_1943.906)

```
(m2 / mean-01
      :ARG1 (i / it)
      :ARG2 (t / thing
            :ARG1-of (e / endanger-01
                  :ARG1-of (c / cause-01
                        :ARG0 (d / disappear-01
                              :ARG1-of (s / speedy-03))))))
```
907. " Is my flower in danger of speedy disappearance ? " (lpp_1943.907)

```
(e2 / endanger-01 :mode interrogative
      :ARG1 (f2 / flower
            :poss (i / i))
      :ARG1-of (c / cause-01
            :ARG0 (d / disappear-01
                  :ARG1-of (s / speedy-03))))
```
908. " Certainly it is . " (lpp_1943.908)

```
(c2 / certain
      :domain (i2 / it))
```
909. " My flower is ephemeral , " the little prince said to himself , " and she has only four thorns to defend herself against the world . (lpp_1943.909)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (a / and
            :op1 (e / ephemeral
                  :domain (f2 / flower
                        :poss p))
            :op2 (h / have-03
                  :ARG0 f2
                  :ARG1 (t2 / thorn
                        :ARG2-of (d / defend-01
                              :ARG0 f2
                              :ARG1 f2
                              :ARG3 (w / world))
                        :quant (o / only :op1 4))))
      :ARG2 p)
```
910. And I have left her on my planet , all alone ! " (lpp_1943.910)

```
(a4 / and
      :op2 (l / leave-12
            :ARG0 (i / i)
            :ARG1 (s / she)
            :ARG2 (p / planet
                  :source-of i)
            :ARG0-of (c / cause-01
                  :ARG1 (a2 / alone
                        :degree (a3 / all)
                        :domain s))))
```
911. That was his first moment of regret . (lpp_1943.911)

```
(m / moment
  :domain (t / that)
  :mod (r / regret-01)
  :ord (o / ordinal-entity :value 1)
  :poss (h / he))
```
912. But he took courage once more . (lpp_1943.912)

```
(c / contrast-01
      :ARG2 (t / take-01
            :ARG0 (h / he)
            :ARG1 (c2 / courage)
            :mod (a / again :frequency 1)))
```
913. " What place would you advise me to visit now ? " he asked . (lpp_1943.913)

```
(a / ask-01
      :ARG0 (h / he)
      :ARG1 (a2 / advise-01
            :ARG0 (y / you)
            :ARG1 h
            :ARG2 (v / visit-01
                  :ARG0 h
                  :ARG1 (p / place
                        :domain (a3 / amr-unknown))
                  :time (n / now))))
```
914. " The planet Earth , " replied the geographer . (lpp_1943.914)

```
(r / reply-01
      :ARG0 (g / geographer)
      :ARG2 (p2 / planet :wiki "Earth"
            :name (n / name :op1 "Earth")))
```
915. " It has a good reputation . " (lpp_1943.915)

```
(h2 / have-03
      :ARG0 (i / it)
      :ARG1 (r / reputation
            :ARG1-of (g / good-02)))
```
916. And the little prince went away , thinking of his flower . (lpp_1943.916)

```
(a / and
      :op2 (a2 / and
            :op1 (g / go-02
                  :ARG0 (p / prince
                        :mod (l / little))
                  :direction (a3 / away))
            :op2 (t / think-01
                  :ARG0 p
                  :ARG1 (f2 / flower
                        :poss p))))
```
917. Chapter 16 . (lpp_1943.917)

```
(c / chapter
      :mod 16)
```
918. So then the seventh planet was the Earth . (lpp_1943.918)

```
(p2 / planet
      :ord (o / ordinal-entity :value 7)
      :domain (p / planet :wiki "Earth"
            :name (n / name :op1 "Earth"))
      :ARG1-of (c / cause-01))
```
919. The Earth is not just an ordinary planet ! (lpp_1943.919)

```
(p / planet
      :mod (o / ordinary
            :mod (j / just :polarity -))
      :domain (p2 / planet :wiki "Earth"
            :name (n / name :op1 "Earth")))
```
920. One can count , there 111 kings ( not forgetting , to be sure , the Negro kings among them ) , 7000 geographers , 900,000 businessmen , 7,500,000 tipplers , 311,000,000 conceited men - - that is to say , about 2,000,000,000 grown - ups . (lpp_1943.920)

```
(p / possible-01
      :ARG1 (a3 / and
            :op1 (c / count-01
                  :ARG0 (o / one)
                  :ARG1 (a / and
                        :op1 (p5 / person :quant 111
                              :ARG0-of (h2 / have-org-role-91
                                    :ARG2 (k / king)))
                        :op2 (g2 / geographer :quant 7000)
                        :op3 (b / businessman :quant 900000)
                        :op4 (p4 / person :quant 7500000
                              :ARG0-of (t2 / tipple-01))
                        :op5 (m / man :quant 311000000
                              :mod (c2 / conceited))
                        :mod (g3 / grown-up
                              :quant (a2 / about :op1 2000000000)))
                  :location (t / there))
            :op2 (f / forget-01 :polarity -
                  :ARG0 o
                  :ARG1 (n / negro
                        :ARG1-of (i2 / include-91
                              :ARG2 p5)
                        :ARG0-of (h / have-org-role-91
                              :ARG2 (k2 / king)))
                  :ARG1-of (s / sure-02))))
```
921. To give you an idea of the size of the Earth , I will tell you that before the invention of electricity it was necessary to maintain , over the whole of the six continents , a veritable army of 462,511 lamplighters for the street lamps . (lpp_1943.921)

```
(t / tell-01
      :ARG0 (i3 / i)
      :ARG1 (o / obligate-01
            :ARG2 (m / maintain-01
                  :ARG1 (a / army
                        :consist-of (p2 / person :quant 462511
                              :ARG0-of (l2 / light-04
                                    :ARG1 (l3 / lamp)))
                        :mod (v / veritable))
                  :location (o2 / over
                        :op1 (c / continent
                              :quant (w / whole :op1 6)))
                  :purpose (l / lamp
                        :location (s2 / street)))
            :time (b / before
                  :op1 (i2 / invent-01
                        :ARG1 (e / electricity))))
      :ARG2 y
      :purpose (g / give-01
            :ARG1 (i / idea
                  :topic (s / size-01
                        :ARG1 (p3 / planet :wiki "Earth"
                              :name (n / name :op1 "Earth"))))
            :ARG2 (y / you)))
```
922. Seen from a slight distance , that would make a splendid spectacle . (lpp_1943.922)

```
(m / make-01
      :ARG0 (t / that)
      :ARG1 (s / spectacle
            :mod (s2 / splendid))
      :condition (s3 / see-01
            :ARG1 t
            :manner (d / distance-01
                  :ARG2 t
                  :degree (s4 / slight))))
```
923. The movements of this army would be regulated like those of the ballet in the opera . (lpp_1943.923)

```
(r / regulate-01
      :ARG1 (m / move-01
            :ARG0 (a / army
                  :mod (t / this))
            :ARG1-of (r3 / resemble-01
                  :ARG2 (m2 / move-01
                        :ARG0 (b / ballet
                              :subevent-of (o / opera))))))
```
924. First would come the turn of the lamplighters of New Zealand and Australia . (lpp_1943.924)

```
(c / come-03
      :ARG1 (t / turn-01
            :ARG1 (p / person
                  :source (a / and
                        :op1 (c2 / country :wiki "New_Zealand"
                              :name (n / name :op1 "New" :op2 "Zealand"))
                        :op2 (c3 / country :wiki "Australia"
                              :name (n2 / name :op1 "Australia")))
                  :ARG0-of (l / light-04
                        :ARG1 (l2 / lamp))))
      :time (f / first))
```
925. Having set their lamps alight , these would go off to sleep . (lpp_1943.925)

```
(g / go-02
      :ARG0 (t / they)
      :purpose (s / sleep-01
            :ARG0 t)
      :time (a / after
            :op1 (l2 / light-04
                  :ARG0 t
                  :ARG1 (l / lamp
                        :poss t))))
```
926. Next , the lamplighters of China and Siberia would enter for their steps in the dance , and then they too would be waved back into the wings . (lpp_1943.926)

```
(a / and
      :op1 (e / enter-01
            :ARG0 (p / person
                  :ARG0-of (l / light-04
                        :ARG1 (l2 / lamp))
                  :source (a2 / and
                        :op1 (c / country :wiki "China"
                              :name (n2 / name :op1 "China"))
                        :op2 (c2 / country-region :wiki "Siberia"
                              :name (n3 / name :op1 "Siberia"))))
            :time (n / next)
            :purpose (s / step
                  :poss p
                  :part-of (d2 / dance-01)))
      :op2 (w / wave-02
            :ARG1 p
            :ARG2 (b / back
                  :direction (i / into
                        :op1 (w2 / wing)))
            :time (t / then)
            :degree (t2 / too)))
```
927. After that would come the turn of the lamplighters of Russia and the Indies ; then those of Africa and Europe , then those of South America ; then those of South America ; then those of North America . (lpp_1943.927)

```
(c8 / come-03
      :ARG1 (t2 / turn
            :poss (p / person
                  :ARG0-of (l / light-04
                        :ARG1 (l2 / lamp))
                  :location (c3 / continent :wiki "North_America" :name (n2 / name :op1 "North" :op2 "America")))
            :time (a / after
                  :op1 (t / turn
                        :poss (p3 / person
                              :ARG0-of l
                              :location (c2 / continent :wiki "South_America" :name (n / name :op1 "South" :op2 "America")))
                        :time (a6 / after
                              :op1 (t3 / turn
                                    :poss (p2 / person
                                          :ARG0-of l
                                          :location (a4 / and
                                                :op1 (c4 / continent :wiki "Africa" :name (n5 / name :op1 "Africa"))
                                                :op2 (c5 / continent :wiki "Europe" :name (n6 / name :op1 "Europe"))))
                                    :time (a3 / after
                                          :op1 (t4 / turn
                                                :poss (p4 / person
                                                      :ARG0-of l
                                                      :location (a2 / and
                                                            :op1 (c / country :wiki "Russia" :name (n3 / name :op1 "Russia"))
                                                            :op2 (w / world-region :wiki "Indies" :name (n4 / name :op1 "Indies"))))))))))))
```
928. And never would they make a mistake in the order of their entry upon the stage . (lpp_1943.928)

```
(a / and
      :op2 (m2 / mistake-02 :polarity -
            :ARG0 (t / they)
            :ARG1 (o / order-03
                  :ARG1 (e / enter-01
                        :ARG0 t
                        :ARG1 (s / stage)))
            :time (e2 / ever)))
```
929. It would be magnificent . (lpp_1943.929)

```
(m / magnificent
  :domain (i / it))
```
930. Only the man who was in charge of the single lamp at the North Pole , and his colleague who was responsible for the single lamp at the South Pole - - only these two would live free from toil and care : they would be busy twice a year . (lpp_1943.930)

```
(l / live-01
      :ARG0 (a2 / and
            :op1 (m / man
                  :ARG1-of (c4 / charge-05
                        :ARG2 (l2 / lamp
                              :ARG1-of (s / single-02)
                              :location (w / world-region :wiki "North_Pole" :name (n3 / name :op1 "North" :op2 "Pole"))))
                  :mod (o / only))
            :op2 (c3 / colleague
                  :poss m
                  :ARG0-of (r / responsible-03
                        :ARG1 (l4 / lamp
                              :ARG1-of (s2 / single-02))
                        :location (w2 / world-region :wiki "South_Pole" :name (n / name :op1 "South" :op2 "Pole"))))
            :mod (p / person :quant 2
                  :mod (t4 / this)
                  :mod (o2 / only)))
      :ARG3-of (f / free-04
            :ARG1 a2
            :ARG2 (a / and
                  :op1 (t / toil-01)
                  :op2 (c / care-01)))
      :ARG1-of (c2 / cause-01
            :ARG0 (b / busy-01
                  :ARG1 a2
                  :frequency (r2 / rate-entity-91
                        :ARG1 2
                        :ARG2 (t3 / temporal-quantity :quant 1
                              :unit (y / year))))))
```
931. Chapter 17 . (lpp_1943.931)

```
(c / chapter
      :mod 17)
```
932. When one wishes to play the wit , he sometimes wanders a little from the truth . (lpp_1943.932)

```
(w / wander-01
      :ARG0 o
      :ARG1 (f / from
            :op1 (t / truth))
      :time (w2 / wish-01
            :ARG0 (o / one)
            :ARG1 (p / play-02
                  :ARG0 o
                  :ARG1 (w3 / wit)))
      :degree (l / little)
      :frequency (s / sometimes))
```
933. I have not been altogether honest in what I have told you about the lamplighters . (lpp_1943.933)

```
(h / honest-01
      :ARG0 (i / i)
      :ARG1 (t2 / thing
            :ARG1-of (t / tell-01
                  :ARG0 i
                  :ARG2 (y / you)
                  :topic (p2 / person
                        :ARG0-of (l / light-04
                              :ARG1 (l2 / lamp)))))
      :degree (a / altogether :polarity -))
```
934. And I realize that I run the risk of giving a false idea of our planet to those who do not know it . (lpp_1943.934)

```
(a / and
      :op2 (r / realize-01
            :ARG0 (i / i)
            :ARG1 (r2 / risk-01
                  :ARG0 i
                  :ARG2 (g / give-01
                        :ARG0 i
                        :ARG1 (i2 / idea
                              :mod (f / false)
                              :topic (p2 / planet
                                    :source (w / we)))
                        :ARG2 (p / person
                              :ARG0-of (k / know-02 :polarity -
                                    :ARG1 p2))))))
```
935. Men occupy a very small place upon the Earth . (lpp_1943.935)

```
(o / occupy-01
      :ARG0 (m / man)
      :ARG1 (p2 / place
            :mod (s / small
                  :degree (v / very))
            :location (p / planet :wiki "Earth"
                  :name (n / name :op1 "Earth"))))
```
936. If the two billion inhabitants who people its surface were all to stand upright and somewhat crowded together , as they do for some big public assembly , they could easily be put into one public square twenty miles long and twenty miles wide . (lpp_1943.936)

```
(p / possible-01
      :ARG1 (p2 / put-01
            :ARG1 p3
            :ARG2 (s5 / square
                  :ARG1-of (p6 / public-02)
                  :ARG1-of (l / long-03
                        :ARG2 (d2 / distance-quantity :quant 20
                              :unit (m / mile)))
                  :ARG1-of (w / wide-02
                        :mod (d3 / distance-quantity :quant 20
                              :unit (m2 / mile))))
            :ARG1-of (e / easy-05))
      :condition (s / stand-01
            :ARG0 (p3 / person :quant 2000000000
                  :ARG0-of (i / inhabit-01)
                  :ARG2-of (p4 / people-01
                        :ARG1 (s2 / surface
                              :poss (i2 / it)))
                  :mod (a / all))
            :ARG1-of (r / resemble-01
                  :ARG2 (d / do-02
                        :ARG0 p3
                        :purpose (a3 / assemble-02
                              :mod (p5 / public)
                              :mod (b / big)
                              :mod (s4 / some))))
            :manner (a2 / and
                  :op1 (u / upright)
                  :op2 (c / crowd-02
                        :manner (t / together)
                        :degree (s3 / somewhat)))))
```
937. All humanity could be piled up on a small Pacific islet . (lpp_1943.937)

```
(p / possible-01
      :ARG1 (p2 / pile-01
            :ARG1 (h / humanity
                  :mod (a / all))
            :ARG2 (i / islet
                  :mod (s / small)
                  :location (o2 / ocean :wiki "Pacific_Ocean"
                        :name (n / name :op1 "Pacific")))))
```
938. The grown - ups , to be sure , will not believe you when you tell them that . (lpp_1943.938)

```
(b / believe-01 :polarity -
      :ARG0 (g2 / grown-up)
      :ARG1 (y / you)
      :time (t / tell-01
            :ARG0 y
            :ARG1 (t2 / that)
            :ARG2 g2)
      :ARG1-of (s / sure-02))
```
939. They imagine that they fill a great deal of space . (lpp_1943.939)

```
(i / imagine-01
  :ARG0 (t / they)
  :ARG1 (f / fill-01
          :ARG1 (s / space
                  :quant (d / deal
                           :mod (g / great)))
          :ARG2 t))
```
940. They fancy themselves as important as the baobabs . (lpp_1943.940)

```
(f / fancy-01
      :ARG0 (t / they)
      :ARG1 (i / important
            :domain t
            :degree (e / equal)
            :compared-to (b / baobab)))
```
941. You should advise them , then , to make their own calculations . (lpp_1943.941)

```
(r / recommend-01
      :ARG1 (a / advise-01
            :ARG0 (y / you)
            :ARG1 (t / they)
            :ARG2 (c / calculate-01
                  :ARG0 t))
      :ARG2 y)
```
942. They adore figures , and that will please them . (lpp_1943.942)

```
(a / and
  :op1 (a2 / adore-01
         :ARG0 (t / they)
         :ARG1 (f / figure))
  :op2 (p / please-01
         :ARG1 t
         :ARG2 (t2 / that)))
```
943. But do not waste your time on this extra task . (lpp_1943.943)

```
(c / contrast-01
      :ARG2 (w / waste-01 :mode imperative :polarity -
            :ARG0 (y / you)
            :ARG1 (t / time
                  :poss y)
            :ARG2 (t2 / task-01
                  :mod (e / extra)
                  :mod (t3 / this))))
```
944. It is unnecessary . (lpp_1943.944)

```
(n / need-01
  :ARG1 (i / it)
  :polarity -)
```
945. You have , I know , confidence in me . (lpp_1943.945)

```
(t / trust-01
      :ARG0 (y / you)
      :ARG2 (i / i)
      :ARG1-of (k / know-01
            :ARG0 i))
```
946. When the little prince arrived on the Earth , he was very much surprised not to see any people . (lpp_1943.946)

```
(s / surprise-01
      :ARG0 (s2 / see-01 :polarity -
            :ARG0 p
            :ARG1 (p2 / person
                  :quant (a / any)))
      :ARG1 (p / prince
            :mod (l / little))
      :degree (m / much
            :degree (v / very))
      :time (a2 / arrive-01
            :ARG1 p
            :ARG4 (p3 / planet :wiki "Earth"
                  :name (n / name :op1 "Earth"))))
```
947. He was beginning to be afraid he had come to the wrong planet , when a coil of gold , the color of the moonlight , flashed across the sand . (lpp_1943.947)

```
(b / begin-01
      :ARG0 (h / he)
      :ARG1 (f / fear-01
            :ARG0 h
            :ARG1 (c / come-01
                  :ARG1 h
                  :ARG4 (p / planet
                        :ARG2-of (w / wrong-04))))
      :time (f2 / flash-02
            :ARG1 (c2 / coil
                  :mod (g / gold
                        :mod (c3 / color
                              :poss (l / light-04
                                    :ARG0 (m / moon)))))
            :path (a / across
                  :op1 (s / sand))))
```
948. " Good evening , " said the little prince courteously . (lpp_1943.948)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (e2 / evening
            :ARG1-of (g / good-02))
      :manner (c / courteous))
```
949. " Good evening , " said the snake . (lpp_1943.949)

```
(s / say-01
      :ARG0 (s2 / snake)
      :ARG1 (d / date-entity
            :dayperiod (e / evening)
            :ARG1-of (g / good-02)))
```
950. " What planet is this on which I have come down ? " asked the little prince . (lpp_1943.950)

```
(a / ask-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (p2 / planet
            :ARG4-of (c / come-01
                  :ARG1 p
                  :direction (d / down))
            :domain (a2 / amr-unknown)))
```
951. " This is the Earth ; this is Africa , " the snake answered . (lpp_1943.951)

```
(a / answer-01
      :ARG0 (s / snake)
      :ARG2 (a2 / and
            :op1 (p / planet :wiki "Earth"
                  :name (n / name :op1 "Earth")
                  :domain (t / this))
            :op2 (c / continent :wiki "Africa"
                  :name (n2 / name :op1 "Africa")
                  :domain (t2 / this))))
```
952. " Ah ! (lpp_1943.952)

```
(a / ah :mode expressive)
```
953. Then there are no people on the Earth ? " (lpp_1943.953)

```
(p / person :mode interrogative :polarity -
      :location (p2 / planet :wiki "Earth" :name (n2 / name :op1 "Earth")))
```
954. " This is the desert . (lpp_1943.954)

```
(d2 / desert
      :domain (t / this))
```
955. There are no people in the desert . (lpp_1943.955)

```
(p / person :polarity -
      :location (d / desert))
```
956. The Earth is large , " said the snake . (lpp_1943.956)

```
(s / say-01
      :ARG0 (s2 / snake)
      :ARG1 (l / large
            :domain (p / planet :wiki "Earth"
                  :name (n / name :op1 "Earth"))))
```
957. The little prince sat down on a stone , and raised his eyes toward the sky . (lpp_1943.957)

```
(a / and
      :op1 (s / sit-down-02
            :ARG1 (p / prince
                  :mod (l / little))
            :ARG2 (s2 / stone)
            :direction (d / down))
      :op2 (r / raise-01
            :ARG0 p
            :ARG1 (e / eye
                  :part-of p)
            :direction (s3 / sky)))
```
958. " I wonder , " he said , " whether the stars are set alight in heaven so that one day each one of us may find his own again ... (lpp_1943.958)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (w2 / wonder-01
            :ARG0 h
            :ARG1 (l / light-04 :mode interrogative
                  :ARG1 (s2 / star)
                  :location (h2 / heaven)
                  :purpose (f / find-01
                        :ARG0 (w / we
                              :mod (e / each))
                        :ARG1 (s3 / star
                              :poss w)
                        :time (d / day
                              :mod (o / one))
                        :mod (a / again)
                        :ARG1-of (p / possible-01)))))
```
959. Look at my planet . (lpp_1943.959)

```
(l2 / look-01 :mode imperative
      :ARG0 (y / you)
      :ARG1 (p / planet
            :source (i / i)))
```
960. It is right there above us . (lpp_1943.960)

```
(b2 / be-located-at-91
      :ARG1 (i / it)
      :ARG2 (t / there
            :mod (r / right)
            :direction (a / above
                  :op1 (w / we))))
```
961. But how far away it is ! " (lpp_1943.961)

```
(c2 / contrast-01
      :ARG2 (f / far
            :direction (a / away)
            :domain (i / it)
            :degree (s / so)))
```
962. " It is beautiful , " the snake said . (lpp_1943.962)

```
(s / say-01
      :ARG0 (s2 / snake)
      :ARG1 (b / beautiful-02
            :ARG1 (i / it)))
```
963. " What has brought you here ? " (lpp_1943.963)

```
(b2 / bring-01
      :ARG0 (a / amr-unknown)
      :ARG1 (y / you)
      :ARG2 (h / here))
```
964. " I have been having some trouble with a flower , " said the little prince . (lpp_1943.964)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (h / have-03
            :ARG0 p
            :ARG1 (t / trouble-01
                  :ARG0 (f2 / flower)
                  :mod (s2 / some))))
```
965. " Ah ! " said the snake . (lpp_1943.965)

```
(s / say-01
      :ARG0 (s2 / snake)
      :ARG1 (a / ah-01))
```
966. And they were both silent . (lpp_1943.966)

```
(a / and
  :op2 (s / silent
         :domain (t / they
                   :mod (b / both))))
```
967. " Where are the men ? " the little prince at last took up the conversation again . (lpp_1943.967)

```
(a3 / and
      :op1 (t / take-up-31
            :ARG0 (p / prince
                  :mod (l / little))
            :ARG1 (c / converse-01)
            :mod (a / again)
            :time (a2 / at-last))
      :op2 (b2 / be-located-at-91
            :ARG1 (m / man)
            :ARG2 (a4 / amr-unknown)))
```
968. " It is a little lonely in the desert ... " (lpp_1943.968)

```
(l2 / lonely
      :domain (b / be-located-at-91
            :ARG2 (d / desert))
      :degree (l / little))
```
969. " It is also lonely among men , " the snake said . (lpp_1943.969)

```
(s / say-01
      :ARG0 (s2 / snake)
      :ARG1 (l / lonely
            :domain (b / be-located-at-91
                  :ARG2 (a3 / among
                        :op1 (m / man)))
            :mod (a2 / also)))
```
970. The little prince gazed at him for a long time . (lpp_1943.970)

```
(g / gaze-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (h / he)
      :ARG1-of (l2 / long-03))
```
971. " You are a funny animal , " he said at last . (lpp_1943.971)

```
(s / say-01
  :ARG0 (h / he)
  :ARG1 (a2 / animal
          :mod (f / funny)
          :domain (y / you))
  :time (a / at-last))
```
972. " You are no thicker than a finger ... " (lpp_1943.972)

```
(t / thick-03
      :ARG1 (y / you)
      :degree (m / more :polarity -)
      :compared-to (f / finger))
```
973. " But I am more powerful than the finger of a king , " said the snake . (lpp_1943.973)

```
(s / say-01
      :ARG0 (s2 / snake)
      :ARG1 (c2 / contrast-01
            :ARG2 (p / powerful-02
                  :ARG1 (i / i)
                  :degree (m / more)
                  :compared-to (f / finger
                        :part-of (k / king)))))
```
974. The little prince smiled . (lpp_1943.974)

```
(s / smile-01
  :ARG0 (p / prince
          :mod (l / little)))
```
975. " You are not very powerful . (lpp_1943.975)

```
(p / powerful-02
      :ARG1 (y / you)
      :degree (v / very :polarity -))
```
976. You have n't even any feet . (lpp_1943.976)

```
(h / have-03 :polarity -
      :ARG0 (y / you)
      :ARG1 (f / foot
            :quant (a / any))
      :mod (e / even))
```
977. You can not even travel ... " (lpp_1943.977)

```
(p / possible-01 :polarity -
      :ARG1 (t / travel-01
            :ARG0 (y / you))
      :mod (e / even))
```
978. " I can carry you farther than any ship could take you , " said the snake . (lpp_1943.978)

```
(s / say-01
  :ARG0 (s2 / snake)
  :ARG1 (p / possible-01
          :ARG1 (c / carry-01
                    :ARG0 s2
                    :ARG1 (y / you)
                    :extent (f / far
                              :degree (m / more)
                              :compared-to (t / take-01
                                             :ARG0 (s3 / ship
                                                     :mod (a / any))
                                             :ARG1 y)))))
```
979. He twined himself around the little prince 's ankle , like a golden bracelet . (lpp_1943.979)

```
(t / twine-01
      :ARG0 (h / he)
      :ARG1 h
      :ARG2 (a / ankle
            :part-of (p / prince
                  :mod (l / little)))
      :manner (r / resemble-01
            :ARG2 (b / bracelet
                  :consist-of (g / gold))))
```
980. " Whomever I touch , I send back to the earth from whence he came , " the snake spoke again . (lpp_1943.980)

```
(s / speak-01
      :ARG0 (s2 / snake)
      :ARG1 (s3 / send-01
            :ARG0 s2
            :ARG1 (p / person
                  :ARG1-of (t / touch-01
                        :ARG0 s2)
                  :mod (a2 / any))
            :ARG2 (b / back
                  :op1 (e / earth
                        :ARG3-of (c / come-01
                              :ARG1 p))))
      :mod (a / again))
```
981. " But you are innocent and true , and you come from a star ... " (lpp_1943.981)

```
(c / contrast-01
      :ARG2 (a / and
            :op1 (a2 / and
                  :op1 (i / innocent-01
                        :ARG1 (y / you))
                  :op2 (t / true-01
                        :ARG1 y))
            :op2 (c2 / come-01
                  :ARG1 y
                  :ARG3 (s2 / star))))
```
982. The little prince made no reply . (lpp_1943.982)

```
(r / reply-01
  :ARG0 (p / prince
          :mod (l / little))
  :polarity -)
```
983. " You move me to pity - - you are so weak on this Earth made of granite , " the snake said . (lpp_1943.983)

```
(s / say-01
      :ARG0 (s2 / snake)
      :ARG1 (p3 / pity-01
            :ARG0 s2
            :ARG1 (y / you)
            :ARG1-of (c / cause-01
                  :ARG0 (w / weak-02
                        :ARG1 y
                        :degree (s3 / so)
                        :location (p2 / planet :wiki "Earth" :name (n / name :op1 "Earth")
                              :consist-of (g / granite)
                              :mod (t / this))))))
```
984. " I can help you , some day , if you grow too homesick for your own planet . (lpp_1943.984)

```
(p / possible-01
      :ARG1 (h / help-01
            :ARG0 (i / i)
            :ARG1 (y / you)
            :time (d / day
                  :mod (s / some)))
      :condition (g / grow-02
            :ARG1 y
            :ARG2 (h2 / homesick
                  :topic (p2 / planet
                        :source-of y)
                  :degree (t / too)
                  :domain y)))
```
985. I can - - " (lpp_1943.985)

```
(p / possible-01
      :ARG1 (d / do-02
            :ARG0 (i / i)))
```
986. " Oh ! (lpp_1943.986)

```
(o / oh :mode expressive)
```
987. I understand you very well , " said the little prince . (lpp_1943.987)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (u / understand-01
          :ARG0 p
          :ARG1 (y / you)
          :mod (w / well
                 :degree (v / very))))
```
988. " But why do you always speak in riddles ? " (lpp_1943.988)

```
(c / contrast-01
      :ARG2 (s2 / speak-01
            :ARG0 (y / you)
            :ARG1 (r / riddle)
            :time (a / always)
            :purpose (a2 / amr-unknown)))
```
989. " I solve them all , " said the snake . (lpp_1943.989)

```
(s / say-01
      :ARG0 (s2 / snake)
      :ARG1 (s3 / solve-01
            :ARG0 s2
            :ARG1 (t / they
                  :mod (a / all))))
```
990. And they were both silent . (lpp_1943.990)

```
(a / and
  :op2 (s / silent
         :domain (t / they
                   :mod (b / both))))
```
991. Chapter 18 . (lpp_1943.991)

```
(c / chapter :mod 18)
```
992. The little prince crossed the desert and met with only one flower . (lpp_1943.992)

```
(a / and
  :op1 (c / cross-02
         :ARG0 (p / prince
                 :mod (l / little))
         :ARG1 (d / desert))
  :op2 (m / meet-03
         :ARG0 p
         :ARG1 (f / flower :quant 1)
         :mod (o2 / only)))
```
993. It was a flower with three petals , a flower of no account at all . (lpp_1943.993)

```
(f2 / flower
      :ARG0-of (h / have-03
            :ARG1 (p / petal :quant 3))
      :mod (a2 / account :polarity -)
      :domain (i / it))
```
994. " Good morning , " said the little prince . (lpp_1943.994)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (m2 / morning
            :ARG1-of (g / good-02)))
```
995. " Good morning , " said the flower . (lpp_1943.995)

```
(s / say-01
      :ARG0 (f / flower-01)
      :ARG1 (m2 / morning
            :ARG1-of (g / good-02)))
```
996. " Where are the men ? " the little prince asked , politely . (lpp_1943.996)

```
(a / ask-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (b / be-located-at-91
            :ARG1 (m / man)
            :ARG2 (a2 / amr-unknown))
      :manner (p3 / polite-01))
```
997. The flower had once seen a caravan passing . (lpp_1943.997)

```
(s / see-01 :frequency 1
      :ARG0 (f / flower)
      :ARG1 (p / pass-02
            :ARG0 (c / caravan-01)))
```
998. " Men ? " she echoed . (lpp_1943.998)

```
(e / echo-01
      :ARG0 (s / she)
      :ARG1 (m / man :mode interrogative))
```
999. " I think there are six or seven of them in existence . (lpp_1943.999)

```
(t / think-01
  :ARG0 (i / i)
  :ARG1 (e / exist-01
          :ARG1 (t2 / they
                  :quant (o / or :op1 6 :op2 7))))
```
1000. I saw them , several years ago . (lpp_1943.1000)

```
(s / see-01
      :ARG0 (i / i)
      :ARG1 (t / they)
      :time (b / before
            :op1 (n / now)
            :quant (s2 / several
                  :op1 (t2 / temporal-quantity :quant 1
                        :unit (y / year)))))
```
1001. But one never knows where to find them . (lpp_1943.1001)

```
(c / contrast-01
      :ARG2 (k / know-01
            :ARG0 (p / person
                  :ARG1-of (i / include-91
                        :ARG2 (t2 / they)))
            :ARG1 (f / find-01
                  :ARG0 p
                  :ARG1 (t / they)
                  :location (a / amr-unknown))
            :time (e / ever :polarity -)))
```
1002. The wind blows them away . (lpp_1943.1002)

```
(b / blow-01
  :ARG0 (w / wind)
  :ARG1 (t / they)
  :direction (a / away))
```
1003. They have no roots , and that makes their life very difficult . " (lpp_1943.1003)

```
(a / and
      :op1 (h / have-03 :polarity -
            :ARG0 (t / they)
            :ARG1 (r / root))
      :op2 (m / make-02
            :ARG0 h
            :ARG1 (d / difficult
                  :domain (t2 / thing
                        :ARG1-of (l / live-01)
                        :poss t)
                  :degree (v / very))))
```
1004. " Goodbye , " said the little prince . (lpp_1943.1004)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (g / goodbye))
```
1005. " Goodbye , " said the flower . (lpp_1943.1005)

```
(s / say-01
  :ARG0 (f / flower)
  :ARG1 (g / goodbye))
```
1006. Chapter 19 . (lpp_1943.1006)

```
(c / chapter :mod 19)
```
1007. After that , the little prince climbed a high mountain . (lpp_1943.1007)

```
(c / climb-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (m / mountain
            :ARG1-of (h / high-02))
      :time (a / after
            :op1 (t / that)))
```
1008. The only mountains he had ever known were the three volcanoes , which came up to his knees . (lpp_1943.1008)

```
(v / volcano :quant 3
  :domain (m / mountain
            :mod (o / only)
            :ARG1-of (k / know-01
                       :ARG0 (h / he)
                       :time (e / ever)))
  :ARG1-of (c / come-04
             :ARG2 (u / up-to
                     :op1 (k2 / knee
                            :part-of h))))
```
1009. And he used the extinct volcano as a footstool . (lpp_1943.1009)

```
(a / and
  :op2 (u / use-01
         :ARG0 (h / he)
         :ARG1 (v / volcano
                 :mod (e / extinct))
         :ARG2 (f / footstool)))
```
1010. " From a mountain as high as this one , " he said to himself , " I shall be able to see the whole planet at one glance , and all the people ... " (lpp_1943.1010)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (p / possible-01
            :ARG1 (s2 / see-01
                  :ARG0 h
                  :ARG1 (a / and
                        :op1 (p2 / planet
                              :extent (w / whole))
                        :op2 (p3 / person
                              :mod (a3 / all)))
                  :source (m / mountain
                        :ARG1-of (h2 / high-02
                              :degree (e / equal)
                              :compared-to (m2 / mountain
                                    :mod (t / this))))
                  :manner (g / glance-01 :quant 1)))
      :ARG2 h)
```
1011. But he saw nothing , save peaks of rock that were sharpened like needles . (lpp_1943.1011)

```
(c / contrast-01
      :ARG2 (s / see-01
            :ARG0 (h / he)
            :ARG1 (n / nothing
                  :ARG2-of (e / except-01
                        :ARG1 (p / peak
                              :consist-of (r / rock)
                              :ARG1-of (s2 / sharpen-01
                                    :manner (r2 / resemble-01
                                          :ARG1 p
                                          :ARG2 (n2 / needle))))))))
```
1012. " Good morning , " he said courteously . (lpp_1943.1012)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (m / morning
            :ARG1-of (g / good-02))
      :manner (c / courtesy))
```
1013. " Good morning - - Good morning - - Good morning , " answered the echo . (lpp_1943.1013)

```
(a / answer-01
      :ARG0 (e / echo-01)
      :ARG1 (m2 / morning
            :ARG1-of (g / good-02)))
```
1014. " Who are you ? " said the little prince . (lpp_1943.1014)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG2 (y / you
          :domain (a / amr-unknown)))
```
1015. " Who are you - - Who are you - - Who are you ? " answered the echo . (lpp_1943.1015)

```
(a / answer-01
  :ARG0 (e / echo-01)
  :ARG2 (y / you
          :domain (a2 / amr-unknown)))
```
1016. " Be my friends . (lpp_1943.1016)

```
(h / have-rel-role-91 :mode imperative
      :ARG0 (y / you)
      :ARG1 (i / i)
      :ARG2 (f / friend))
```
1017. I am all alone , " he said . (lpp_1943.1017)

```
(s / say-01
  :ARG0 (h / he)
  :ARG1 (a / alone
          :degree (a2 / all)
          :domain h))
```
1018. " I am all alone - - all alone - - all alone , " answered the echo . (lpp_1943.1018)

```
(a / answer-01
      :ARG0 (e / echo-01)
      :ARG2 (a2 / alone
            :domain (i / i)
            :mod (a3 / all)))
```
1019. " What a queer planet ! " he thought . (lpp_1943.1019)

```
(t / think-01
      :ARG0 (h / he)
      :ARG1 (p / planet
            :mod (q / queer
                  :degree (a / amr-unknown))))
```
1020. " It is altogether dry , and altogether pointed , and altogether harsh and forbidding . (lpp_1943.1020)

```
(a / and
      :op1 (d / dry-08
            :ARG1 (i / it)
            :degree (a2 / altogether))
      :op2 (p / pointed
            :degree (a3 / altogether)
            :domain i)
      :op3 (a4 / and
            :op1 (h / harsh-02
                  :ARG1 i)
            :op2 (f / forbidding
                  :domain i)
            :degree (a5 / altogether)))
```
1021. And the people have no imagination . (lpp_1943.1021)

```
(a / and
      :op2 (h / have-03
            :ARG0 (p / person)
            :ARG1 (i2 / imagine-01 :polarity -)))
```
1022. They repeat whatever one says to them ... (lpp_1943.1022)

```
(r / repeat-01
      :ARG0 (t2 / they)
      :ARG1 (t / thing
            :ARG1-of (s2 / say-01
                  :ARG0 (p / person
                        :ARG1-of (i / include-91
                              :ARG2 (t3 / they)))
                  :ARG2 t2)
            :mod (a / all)))
```
1023. On my planet I had a flower ; she always was the first to speak ... " (lpp_1943.1023)

```
(h / have-03
      :ARG0 (i / i)
      :ARG1 (f / flower
            :ARG0-of (s / speak-01
                  :ord (o / ordinal-entity :value 1)
                  :time (a / always)))
      :location (p2 / planet
            :poss i))
```
1024. Chapter 20 . (lpp_1943.1024)

```
(c / chapter :mod 20)
```
1025. But it happened that after walking for a long time through sand , and rocks , and snow , the little prince at last came upon a road . (lpp_1943.1025)

```
(c / contrast-01
      :ARG2 (c2 / come-upon-26
            :ARG0 (p / prince
                  :mod (l / little))
            :ARG1 (r / road)
            :time (a / after
                  :op1 (w / walk-01
                        :ARG0 p
                        :path (a2 / and
                              :op1 (s / sand)
                              :op2 (r2 / rock)
                              :op3 (t / thing
                                    :ARG1-of (s2 / snow-01)))
                        :ARG1-of (l3 / long-03)))
            :time (a3 / at-last)))
```
1026. And all roads lead to the abodes of men . (lpp_1943.1026)

```
(a / and
      :op2 (l / lead-01
            :ARG0 (r / road
                  :mod (a2 / all))
            :ARG4 (a3 / abode
                  :poss (m / man))))
```
1027. " Good morning , " he said . (lpp_1943.1027)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (m / morning
            :ARG1-of (g / good-02)))
```
1028. He was standing before a garden , all a - bloom with roses . (lpp_1943.1028)

```
(s / stand-01
      :ARG1 (h / he)
      :ARG2 (b / before
            :op1 (g / garden
                  :location-of (b2 / bloom-01
                        :ARG0 (r / rose)))))
```
1029. " Good morning , " said the roses . (lpp_1943.1029)

```
(s / say-01
      :ARG0 (r / rose)
      :ARG1 (m / morning
            :ARG1-of (g / good-02)))
```
1030. The little prince gazed at them . (lpp_1943.1030)

```
(g / gaze-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (t / they))
```
1031. They all looked like his flower . (lpp_1943.1031)

```
(l / look-02
      :ARG0 (t / they
            :mod (a / all))
      :ARG1 (f / flower
            :poss (h / he)))
```
1032. " Who are you ? " he demanded , thunderstruck . (lpp_1943.1032)

```
(d / demand-01
      :ARG0 (h / he
            :mod (t / thunderstruck))
      :ARG1 (a / amr-unknown
            :domain (y2 / you)))
```
1033. " We are roses , " the roses said . (lpp_1943.1033)

```
(s / say-01
  :ARG0 (r / rose)
  :ARG1 (r2 / rose
          :domain r))
```
1034. And he was overcome with sadness . (lpp_1943.1034)

```
(a / and
      :op2 (o / overcome-01
            :ARG0 (s / sad-02)
            :ARG1 (h / he)))
```
1035. His flower had told him that she was the only one of her kind in all the universe . (lpp_1943.1035)

```
(t / tell-01
      :ARG0 (f / flower
            :poss (h / he))
      :ARG1 (u2 / unique
            :domain (s / she)
            :location (u / universe
                  :mod (a / all)))
      :ARG2 h)
```
1036. And here were five thousand of them , all alike , in one single garden ! (lpp_1943.1036)

```
(a / and
      :op1 (t / they :quant 5000
            :ARG1-of (a2 / alike-05
                  :mod (a3 / all))
            :location (h / here)
            :location (g / garden :quant 1)))
```
1037. " She would be very much annoyed , " he said to himself , " if she should see that ... she would cough most dreadfully , and she would pretend that she was dying , to avoid being laughed at . (lpp_1943.1037)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (a / and
            :op1 (a2 / annoy-01
                  :ARG1 (s2 / she)
                  :degree (m2 / much
                        :degree (v / very)))
            :op2 (c / cough-01
                  :ARG0 s2
                  :manner (d2 / dreadful-02
                        :degree (m / most)))
            :op3 (p / pretend-01
                  :ARG0 s2
                  :ARG1 (d / die-01
                        :ARG1 s2)
                  :purpose (a3 / avoid-01
                        :ARG0 s2
                        :ARG1 (l / laugh-01
                              :ARG2 s2)))
            :condition (s3 / see-01
                  :ARG0 s2
                  :ARG1 (t / that)))
      :ARG2 h)
```
1038. And I should be obliged to pretend that I was nursing her back to life - - for if I did not do that , to humble myself also , she would really allow herself to die ... " (lpp_1943.1038)

```
(a / and
      :op2 (o / oblige-02
            :ARG1 i
            :ARG2 (p / pretend-01
                  :ARG0 i
                  :ARG1 (n / nurse-01
                        :ARG0 i
                        :ARG1 s
                        :purpose (l / live-01
                              :ARG0 s))))
      :ARG1-of (c / cause-01
            :ARG0 (a2 / allow-01
                  :ARG0 (s / she)
                  :ARG1 (d / die-01
                        :ARG1 s)
                  :ARG1-of (r / real-04)
                  :condition (p2 / pretend-01 :polarity -
                        :ARG0 i
                        :ARG1 n
                        :purpose (h / humble-01
                              :ARG0 i
                              :ARG1 (i / i)
                              :mod (a3 / also))))))
```
1039. Then he went on with his reflections : " I thought that I was rich , with a flower that was unique in all the world ; and all I had was a common rose . (lpp_1943.1039)

```
(g / go-on-25
      :ARG0 h
      :ARG1 (r / reflect-02
            :ARG0 (h / he)
            :ARG1 (c2 / contrast-01
                  :ARG1 (t / think-01
                        :ARG0 h
                        :ARG1 (r3 / rich
                              :ARG1-of (c3 / cause-01
                                    :ARG0 (h3 / have-03
                                          :ARG0 h
                                          :ARG1 (f / flower
                                                :mod (u / unique
                                                      :compared-to (w / world
                                                            :mod (a2 / all))))))
                              :domain h))
                  :ARG2 (h2 / have-03
                        :ARG0 h
                        :ARG1 (r2 / rose
                              :mod (c / common))
                        :mod (a / all))))
      :time (t2 / then))
```
1040. A common rose , and three volcanoes that come up to my knees - - and one of them perhaps extinct forever ... that does n't make me a very great prince ... " (lpp_1943.1040)

```
(m / make-02 :polarity -
      :ARG0 (a / and
            :op1 (r / rose
                  :mod (c / common))
            :op2 (v2 / volcano :quant 3
                  :ARG1-of (c2 / come-01
                        :ARG4 (k / knee
                              :part-of i)
                        :direction (u / up))
                  :ARG2-of (i2 / include-91
                        :ARG1 (v3 / volcano :quant 1
                              :mod (e / extinct
                                    :mod (p2 / perhaps)
                                    :duration (f / forever))))))
      :ARG1 (p / prince
            :mod (g / great
                  :degree (v / very))
            :domain (i / i)))
```
1041. And he lay down in the grass and cried . (lpp_1943.1041)

```
(a2 / and
      :op2 (a / and
            :op1 (l / lie-07
                  :ARG1 (h / he)
                  :ARG2 (g / grass)
                  :direction (d / down))
            :op2 (c / cry-02
                  :ARG0 h)))
```
1042. Chapter 21 . (lpp_1943.1042)

```
(c / chapter :mod 21)
```
1043. It was then that the fox appeared . (lpp_1943.1043)

```
(a / appear-01
      :ARG1 (f / fox)
      :time (t / then))
```
1044. " Good morning , " said the fox . (lpp_1943.1044)

```
(s / say-01
      :ARG0 (f / fox)
      :ARG1 (m / morning
            :ARG1-of (g / good-02)))
```
1045. " Good morning , " the little prince responded politely , although when he turned around he saw nothing . (lpp_1943.1045)

```
(r / respond-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG2 (m / morning
            :ARG1-of (g / good-02))
      :manner (p2 / polite-01)
      :concession (s / see-01
            :ARG0 p
            :ARG1 (n / nothing)
            :time (t / turn-01
                  :ARG1 p
                  :direction (a / around))))
```
1046. " I am right here , " the voice said , " under the apple tree . " (lpp_1943.1046)

```
(s / say-01
      :ARG0 (v / voice)
      :ARG1 (i / i
            :location (h / here
                  :location (u / under
                        :op1 (t / tree
                              :mod (a / apple)))
                  :mod (r / right))))
```
1047. " Who are you ? " asked the little prince , and added , " You are very pretty to look at . " (lpp_1943.1047)

```
(a / and
  :op1 (a2 / ask-01
         :ARG0 (p / prince
                 :mod (l / little))
         :ARG1 (y2 / you
                 :mod (a3 / amr-unknown)))
  :op2 (a4 / add-01
         :ARG0 p
         :ARG1 (l2 / look-01
                 :ARG0 p
                 :ARG1 y2
                 :ARG2 (p2 / pretty
                         :degree (v / very)))))
```
1048. " I am a fox , " said the fox . (lpp_1943.1048)

```
(s / say-01
  :ARG0 (f / fox)
  :ARG1 (f2 / fox
          :domain f))
```
1049. " Come and play with me , " proposed the little prince . (lpp_1943.1049)

```
(p / propose-01
      :ARG0 (p2 / prince
            :mod (l / little))
      :ARG1 (a / and
            :op1 (c / come-01)
            :op2 (p3 / play-01
                  :ARG3 p2)))
```
1050. " I am so unhappy . " (lpp_1943.1050)

```
(h / happy-01 :polarity -
      :ARG1 (i / i)
      :mod (s / so))
```
1051. " I can not play with you , " the fox said . (lpp_1943.1051)

```
(s / say-01
      :ARG0 (f / fox)
      :ARG1 (p / possible-01 :polarity -
            :ARG1 (p2 / play-01
                  :ARG0 f
                  :ARG3 (y / you))))
```
1052. " I am not tamed . " (lpp_1943.1052)

```
(t / tame-01
  :ARG1 (i / i)
  :polarity -)
```
1053. " Ah ! (lpp_1943.1053)

```
(a / ah :mode expressive)
```
1054. Please excuse me , " said the little prince . (lpp_1943.1054)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (e / excuse-01 :mode imperative :polite +
            :ARG0 (y / you)
            :ARG1 (i / i)))
```
1055. But , after some thought , he added : " What does that mean - - ' tame ' ? " (lpp_1943.1055)

```
(c / contrast-01
      :ARG2 (a / add-01
            :ARG0 (h / he)
            :ARG1 (m / mean-01
                  :ARG1 (t2 / tame-01)
                  :ARG2 (a3 / amr-unknown))
            :time (a2 / after
                  :op1 (t / think-01
                        :mod (s / some)))))
```
1056. " You do not live here , " said the fox . (lpp_1943.1056)

```
(s / say-01
  :ARG0 (f / fox)
  :ARG1 (l / live-01
          :ARG0 (y / you)
          :location (h / here
                      :polarity -)))
```
1057. " What is it that you are looking for ? " (lpp_1943.1057)

```
(l / look-01
  :ARG0 (y / you)
  :ARG1 (a / amr-unknown))
```
1058. " I am looking for men , " said the little prince . (lpp_1943.1058)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (l2 / look-01
          :ARG0 p
          :ARG1 (m / man)))
```
1059. " What does that mean - - ' tame ' ? " (lpp_1943.1059)

```
(m / mean-01
      :ARG1 (t / tame-01)
      :ARG2 (a / amr-unknown))
```
1060. " Men , " said the fox . (lpp_1943.1060)

```
(s / say-01
  :ARG0 (f / fox)
  :ARG1 (m / man))
```
1061. " They have guns , and they hunt . (lpp_1943.1061)

```
(a / and
  :op1 (h / have-03
         :ARG0 (t / they)
         :ARG1 (g / gun))
  :op2 (h2 / hunt-01
         :ARG0 t))
```
1062. It is very disturbing . (lpp_1943.1062)

```
(d / disturb-01
      :ARG0 (i / it)
      :degree (v / very))
```
1063. They also raise chickens . (lpp_1943.1063)

```
(r / raise-03
  :ARG0 (t / they)
  :ARG1 (c / chicken)
  :mod (a / also))
```
1064. These are their only interests . (lpp_1943.1064)

```
(i / interest-01
      :ARG0 (t / this)
      :ARG1 (t2 / they)
      :mod (o / only))
```
1065. Are you looking for chickens ? " (lpp_1943.1065)

```
(l / look-01
  :ARG0 (y / you)
  :ARG1 (c / chicken)
  :mode interrogative)
```
1066. " No , " said the little prince . (lpp_1943.1066)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (n / no))
```
1067. " I am looking for friends . (lpp_1943.1067)

```
(l / look-01
      :ARG0 (i / i)
      :ARG1 (p / person
            :ARG0-of (h / have-rel-role-91
                  :ARG1 i
                  :ARG2 (f / friend))))
```
1068. What does that mean - - ' tame ' ? " (lpp_1943.1068)

```
(m / mean-01
      :ARG1 (t / tame-01)
      :ARG2 (a / amr-unknown))
```
1069. " It is an act too often neglected , " said the fox . (lpp_1943.1069)

```
(s / say-01
  :ARG0 (f / fox)
  :ARG1 (n / neglect-01
          :ARG1 (a / act-02)
          :frequency (o / often
                       :degree (t / too))))
```
1070. It means to establish ties . " (lpp_1943.1070)

```
(m / mean-01
      :ARG1 (i / it)
      :ARG2 (e / establish-01
            :ARG1 (t / tie-01)))
```
1071. " ' To establish ties ' ? " (lpp_1943.1071)

```
(e / establish-01
  :ARG1 (t / tie-01)
  :mode interrogative)
```
1072. " Just that , " said the fox . (lpp_1943.1072)

```
(s / say-01
  :ARG0 (f / fox)
  :ARG1 (t / that
          :mod (j / just)))
```
1073. " To me , you are still nothing more than a little boy who is just like a hundred thousand other little boys . (lpp_1943.1073)

```
(o2 / opine-01
      :ARG0 (i / i)
      :ARG1 (b / boy
            :mod (l / little)
            :ARG1-of (r / resemble-01
                  :ARG2 (b2 / boy :quant 100000
                        :mod (l2 / little)
                        :mod (o / other))
                  :mod (j / just))
            :domain (y2 / you
                  :mod (m2 / more :polarity -))
            :mod (s2 / still)))
```
1074. And I have no need of you . (lpp_1943.1074)

```
(a / and
  :op2 (n / need-01
         :ARG0 (i / i)
         :ARG1 (y / you)
         :polarity -))
```
1075. And you , on your part , have no need of me . (lpp_1943.1075)

```
(a / and
      :op2 (n / need-01 :polarity -
            :ARG0 (y / you)
            :ARG1 (i / i)))
```
1076. To you , I am nothing more than a fox like a hundred thousand other foxes . (lpp_1943.1076)

```
(o / opine-01
      :ARG0 (y2 / you)
      :ARG1 (f / fox
            :ARG1-of (r3 / resemble-01
                  :ARG2 (f2 / fox :quant 100000
                        :mod (o3 / other)))
            :domain (i / i
                  :mod (m2 / more :polarity -))))
```
1077. But if you tame me , then we shall need each other . (lpp_1943.1077)

```
(c / contrast-01
  :ARG2 (n / need-01
          :ARG0 (w / we)
          :ARG1 (o / other
                  :mod (e / each))
          :condition (t / tame-01
                       :ARG0 (y / you)
                       :ARG1 (i / i))))
```
1078. To me , you will be unique in all the world . (lpp_1943.1078)

```
(o / opine-01
      :ARG0 (i / i)
      :ARG1 (u / unique
            :domain (y / you)
            :location (w / world
                  :mod (a / all))))
```
1079. To you , I shall be unique in all the world ... " (lpp_1943.1079)

```
(o / opine-01
      :ARG0 (y / you)
      :ARG1 (u / unique
            :domain (i / i)
            :location (w / world
                  :mod (a / all))))
```
1080. " I am beginning to understand , " said the little prince . (lpp_1943.1080)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (b / begin-01
          :ARG0 (i / i)
          :ARG1 (u / understand-01
                  :ARG0 i)))
```
1081. " There is a flower ... (lpp_1943.1081)

```
(f / flower)
```
1082. I think that she has tamed me ... " (lpp_1943.1082)

```
(t / think-01
  :ARG0 (i / i)
  :ARG1 (t2 / tame-01
          :ARG0 (s / she)
          :ARG1 i))
```
1083. " It is possible , " said the fox . (lpp_1943.1083)

```
(s / say-01
  :ARG0 (f / fox)
  :ARG1 (p / possible-01
          :ARG1 (i / it)))
```
1084. " On the Earth one sees all sorts of things . " (lpp_1943.1084)

```
(s / see-01
      :ARG0 (o / one)
      :ARG1 (t / thing
            :mod (s2 / sort
                  :mod (a / all)))
      :location (p / planet :wiki "Earth"
            :name (n / name :op1 "Earth")))
```
1085. " Oh , but this is not on the Earth ! " said the little prince . (lpp_1943.1085)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (a / and
            :op1 (o / oh :mode expressive)
            :op2 (c / contrast-01
                  :ARG2 (b / be-located-at-91 :polarity -
                        :ARG1 (t / this)
                        :ARG2 (p2 / planet :wiki "Earth" :name (n / name :op1 "Earth"))))))
```
1086. The fox seemed perplexed , and very curious . (lpp_1943.1086)

```
(s / seem-01
  :ARG1 (a / and
          :op1 (p / perplex-01
                 :ARG1 (f / fox))
          :op2 (c / curious-01
                 :ARG1 f
                 :degree (v / very))))
```
1087. " On another planet ? " (lpp_1943.1087)

```
(b / be-located-at-91
  :ARG2 (p / planet
          :mod (a2 / another))
  :mode interrogative)
```
1088. " Yes . " (lpp_1943.1088)

```
(y / yes)
```
1089. " Are there hunters on this planet ? " (lpp_1943.1089)

```
(p / person
  :ARG0-of (h / hunt-01)
  :location (p2 / planet
              :mod (t / this))
  :mode interrogative)
```
1090. " No . " (lpp_1943.1090)

```
(n / no)
```
1091. " Ah , that is interesting ! (lpp_1943.1091)

```
(a / ah-01
  :ARG1 (i2 / interest-01
          :ARG0 (t / that)))
```
1092. Are there chickens ? " (lpp_1943.1092)

```
(c / chicken
  :mode interrogative)
```
1093. " No . " (lpp_1943.1093)

```
(n / no)
```
1094. " Nothing is perfect , " sighed the fox . (lpp_1943.1094)

```
(s / sigh-01
      :ARG0 (f / fox)
      :ARG1 (p / perfect-02
            :ARG1 (n / nothing)))
```
1095. But he came back to his idea . (lpp_1943.1095)

```
(c2 / contrast-01
  :ARG2 (c / come-01
          :ARG1 (h / he)
          :ARG4 (i / idea
                  :poss h)
          :direction (b2 / back)))
```
1096. " My life is very monotonous , " the fox said . (lpp_1943.1096)

```
(s / say-01
  :ARG0 (f / fox)
  :ARG1 (m / monotonous
          :domain (l / life
                    :poss (i / i))
          :degree (v / very)))
```
1097. " I hunt chickens ; men hunt me . (lpp_1943.1097)

```
(a / and
  :op1 (h / hunt-01
         :ARG0 (i / i)
         :ARG1 (c / chicken))
  :op2 (h2 / hunt-01
         :ARG0 (m / man)
         :ARG1 i))
```
1098. All the chickens are just alike , and all the men are just alike . (lpp_1943.1098)

```
(a / and
      :op1 (a2 / alike-05
            :ARG1 (c / chicken
                  :mod (a5 / all))
            :mod (j / just))
      :op2 (a3 / alike-05
            :ARG1 (m / man
                  :mod (a7 / all))
            :mod (j2 / just)))
```
1099. And , in consequence , I am a little bored . (lpp_1943.1099)

```
(a / and
  :op2 (c2 / cause-01
         :ARG1 (b / bore-02
                 :ARG1 (i / i)
                 :degree (l / little))))
```
1100. But if you tame me , it will be as if the sun came to shine on my life . (lpp_1943.1100)

```
(c / contrast-01
  :ARG2 (s / shine-01
          :ARG1 (s2 / sun)
          :ARG2 (l / life
                  :poss (i / i))
          :condition (t / tame-01
                       :ARG0 (y / you)
                       :ARG1 i)))
```
1101. I shall know the sound of a step that will be different from all the others . (lpp_1943.1101)

```
(k / know-04
      :ARG0 (i / i)
      :ARG1 (s / sound-02
            :ARG1 (s2 / step-01
                  :ARG1-of (d / differ-02
                        :ARG2 (s3 / step-01
                              :mod (o / other
                                    :mod (a / all)))))))
```
1102. Other steps send me hurrying back underneath the ground . (lpp_1943.1102)

```
(s / send-03
  :ARG0 (s2 / step-01
          :mod (o / other))
  :ARG1 (i / i)
  :ARG4 (u / underneath
          :op1 (g / ground))
  :ARG5 (b / back)
  :manner (h / hurry-01
            :ARG1 i))
```
1103. Yours will call me , like music , out of my burrow . (lpp_1943.1103)

```
(c / call-03
      :ARG0 (s / step-01
            :ARG1 (y / you))
      :ARG1 (o / out-06
            :ARG1 i
            :ARG2 (b / burrow
                  :poss i))
      :ARG2 (i / i)
      :ARG1-of (r / resemble-01
            :ARG2 (m / music)))
```
1104. And then look : you see the grain - fields down yonder ? (lpp_1943.1104)

```
(a / and
  :op2 (l / look-01
         :ARG0 y
         :time (t / then)
         :mode imperative)
  :op3 (s / see-01
         :ARG0 (y / you)
         :ARG1 (f / field
                 :mod (g / grain)
                 :location (y2 / yonder
                             :mod (d / down)))
         :mode interrogative))
```
1105. I do not eat bread . (lpp_1943.1105)

```
(e / eat-01
  :ARG0 (i / i)
  :ARG1 (b / bread)
  :polarity -)
```
1106. Wheat is of no use to me . (lpp_1943.1106)

```
(u / use-01
  :ARG0 (i / i)
  :ARG1 (w / wheat)
  :polarity -)
```
1107. The wheat fields have nothing to say to me . (lpp_1943.1107)

```
(s / say-01
  :ARG0 (f / field
          :mod (w / wheat))
  :ARG1 (n / nothing)
  :ARG2 (i / i))
```
1108. And that is sad . (lpp_1943.1108)

```
(a / and
      :op2 (s / sad-02
            :ARG0 (t2 / that)))
```
1109. But you have hair that is the colour of gold . (lpp_1943.1109)

```
(c2 / contrast-01
      :ARG2 (h / have-03
            :ARG0 (y / you)
            :ARG1 (h2 / hair
                  :mod (c / color
                        :mod (g / gold)))))
```
1110. Think how wonderful that will be when you have tamed me ! (lpp_1943.1110)

```
(t / think-01 :mode imperative
      :ARG0 y
      :ARG1 (w / wonderful-03
            :ARG1 (t2 / tame-01
                  :ARG0 (y / you)
                  :ARG1 (i / i))
            :degree (a / amr-unknown)))
```
1111. The grain , which is also golden , will bring me back the thought of you . (lpp_1943.1111)

```
(b / bring-01
  :ARG0 (g / grain
          :mod (g2 / golden
                 :mod (a / also)))
  :ARG1 (t / think-01
          :ARG1 (y / you))
  :ARG2 (i / i)
  :direction (b2 / back))
```
1112. And I shall love to listen to the wind in the wheat ... " (lpp_1943.1112)

```
(a / and
  :op2 (l / love-02
         :ARG0 (i / i)
         :ARG1 (l2 / listen-01
                 :ARG0 i
                 :ARG1 (w / wind
                         :location (w2 / wheat)))))
```
1113. The fox gazed at the little prince , for a long time . (lpp_1943.1113)

```
(g / gaze-01
      :ARG0 (f / fox)
      :ARG1 (p / prince
            :mod (l / little))
      :ARG1-of (l2 / long-03))
```
1114. " Please - - tame me ! " he said . (lpp_1943.1114)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (t / tame-01 :mode imperative :polite +
            :ARG0 (y / you)
            :ARG1 h))
```
1115. " I want to , very much , " the little prince replied . (lpp_1943.1115)

```
(r / reply-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG2 (w / want-01
          :ARG0 p
          :ARG1 (t / tame-01
                  :ARG0 p
                  :ARG1 (y / you))
          :degree (m / much
                    :degree (v / very))))
```
1116. " But I have not much time . (lpp_1943.1116)

```
(c / contrast-01
  :ARG2 (h / have-03
          :ARG0 (i / i)
          :ARG1 (t / time
                  :quant (m / much
                           :polarity -))))
```
1117. I have friends to discover , and a great many things to understand . " (lpp_1943.1117)

```
(o / obligate-01
      :ARG2 (a / and
            :op1 (d / discover-01
                  :ARG0 (i / i)
                  :ARG1 (p / person
                        :ARG0-of (h / have-rel-role-91
                              :ARG1 i
                              :ARG2 (f / friend))))
            :op2 (u / understand-01
                  :ARG0 i
                  :ARG1 (t / thing
                        :quant (m / many
                              :mod (g / great))))))
```
1118. " One only understands the things that one tames , " said the fox . (lpp_1943.1118)

```
(s / say-01
  :ARG0 (f / fox)
  :ARG1 (u / understand-01
          :ARG0 (o / one)
          :ARG1 (t / thing
                  :ARG1-of (t2 / tame-01
                             :ARG0 o))
          :mod (o2 / only)))
```
1119. " Men have no more time to understand anything . (lpp_1943.1119)

```
(h / have-03
  :ARG0 (m / man)
  :ARG1 (t / time
          :duration-of (u / understand-01
                         :ARG0 m
                         :ARG1 (a / anything)))
  :polarity -)
```
1120. They buy things all ready made at the shops . (lpp_1943.1120)

```
(b / buy-01
  :ARG0 (t / they)
  :ARG1 (t2 / thing
          :ARG1-of (m / make-01
                     :time (a / already)))
  :location (s / shop))
```
1121. But there is no shop anywhere where one can buy friendship , and so men have no friends any more . (lpp_1943.1121)

```
(c / contrast-01
      :ARG2 (p / possible-01 :polarity -
            :ARG1 (b / buy-01
                  :ARG0 (o / one)
                  :ARG1 (f / friendship)
                  :location (s / shop
                        :location (a2 / anywhere))
                  :ARG0-of (c2 / cause-01
                        :ARG1 (h / have-rel-role-91 :polarity -
                              :ARG0 (p2 / person)
                              :ARG1 (m / man)
                              :ARG2 (f2 / friend)
                              :mod (a / anymore))))))
```
1122. If you want a friend , tame me ... " (lpp_1943.1122)

```
(t / tame-01
      :ARG0 (y / you)
      :ARG1 (i / i)
      :condition (w / want-01
            :ARG0 y
            :ARG1 (h / have-rel-role-91
                  :ARG0 (p / person)
                  :ARG1 y
                  :ARG2 (f / friend))))
```
1123. " What must I do , to tame you ? " asked the little prince . (lpp_1943.1123)

```
(a / ask-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (o / obligate-01
          :ARG2 (d / do-02
                  :ARG0 p
                  :ARG1 (a2 / amr-unknown)
                  :purpose (t / tame-01
                             :ARG0 p
                             :ARG1 (y / you)))))
```
1124. " You must be very patient , " replied the fox . (lpp_1943.1124)

```
(r / reply-01
      :ARG0 (f / fox)
      :ARG2 (o / obligate-01
            :ARG2 (p / patient-01
                  :ARG1 (y / you)
                  :degree (v / very))))
```
1125. " First you will sit down at a little distance from me - - like that - - in the grass . (lpp_1943.1125)

```
(s / sit-down-02
      :ARG1 (y / you)
      :time (f / first)
      :location (r / relative-position
            :op1 (i / i)
            :quant (l / little)
            :unit (d / distance))
      :direction (d2 / down
            :location (g / grass))
      :example (t / that))
```
1126. I shall look at you out of the corner of my eye , and you will say nothing . (lpp_1943.1126)

```
(a / and
      :op1 (l / look-01
            :ARG0 (i / i)
            :ARG1 (y / you)
            :source (c / corner
                  :part-of (e / eye
                        :part-of i)))
      :op2 (s / say-01
            :ARG0 y
            :ARG1 (n / nothing)))
```
1127. Words are the source of misunderstandings . (lpp_1943.1127)

```
(s / source-01
      :ARG1 (m / misunderstand-01)
      :ARG2 (w / word))
```
1128. But you will sit a little closer to me , every day ... " (lpp_1943.1128)

```
(c2 / contrast-01
      :ARG2 (s / sit-01
            :ARG1 (y / you)
            :ARG2 (c / close-10
                  :ARG1 y
                  :ARG2 (i / i)
                  :degree (m / more
                        :mod (l / little))
                  :frequency (r2 / rate-entity-91
                        :ARG3 (t / temporal-quantity :quant 1
                              :unit (d / day))))))
```
1129. The next day the little prince came back . (lpp_1943.1129)

```
(c / come-01
      :ARG1 (p / prince
            :mod (l / little))
      :direction (b / back)
      :time (d / day
            :mod (n / next)))
```
1130. " It would have been better to come back at the same hour , " said the fox . (lpp_1943.1130)

```
(s / say-01
      :ARG0 (f / fox)
      :ARG1 (g / good-02
            :ARG1 (c / come-01
                  :direction (b2 / back)
                  :time (h / hour
                        :ARG1-of (s2 / same-01)))
            :degree (m / more)))
```
1131. " If , for example , you come at four o'clock in the afternoon , then at three o'clock I shall begin to be happy . (lpp_1943.1131)

```
(b / begin-01
      :ARG0 (i / i)
      :ARG1 (h / happy-01
            :ARG1 i)
      :condition (c / come-01
            :ARG1 (y / you)
            :time (d2 / date-entity :time "4:00"
                  :dayperiod (a / afternoon))
            :ARG0-of (e / exemplify-01))
      :time (d / date-entity :time "3:00"))
```
1132. I shall feel happier and happier as the hour advances . (lpp_1943.1132)

```
(f / feel-01
      :ARG0 (i / i)
      :ARG1 (a / and
            :op1 (h / happy-01
                  :ARG1 i
                  :degree (m / more))
            :op2 (h2 / happy-01
                  :ARG1 i
                  :degree (m2 / more)))
      :time (a2 / advance-01
            :ARG1 (h3 / hour)))
```
1133. At four o'clock , I shall already be worrying and jumping about . (lpp_1943.1133)

```
(a / and
      :op1 (w / worry-01
            :ARG1 (i / i))
      :op2 (j / jump-03
            :ARG0 i
            :direction (a2 / about))
      :time (d / date-entity :time "4:00")
      :time (a3 / already))
```
1134. I shall show you how happy I am ! (lpp_1943.1134)

```
(s / show-01
      :ARG0 (i / i)
      :ARG1 (h / happy-01
            :ARG1 i
            :degree (s2 / so))
      :ARG2 (y / you))
```
1135. But if you come at just any time , I shall never know at what hour my heart is to be ready to greet you ... (lpp_1943.1135)

```
(c / contrast-01
      :ARG2 (k / know-01 :polarity -
            :ARG0 (i / i)
            :ARG1 (h3 / hour
                  :time (r / ready-02
                        :ARG1 (h2 / heart
                              :part-of i)
                        :ARG2 (g / greet-01
                              :ARG0 h2
                              :ARG1 (y / you))))
            :time (e / ever)
            :condition (c2 / come-01
                  :ARG1 (y2 / you)
                  :time (t / time
                        :mod (a2 / any
                              :mod (j2 / just))))))
```
1136. One must observe the proper rites ... " (lpp_1943.1136)

```
(o / obligate-01
      :ARG1 (o3 / one)
      :ARG2 (o2 / observe-01
            :ARG0 o3
            :ARG1 (r / rite
                  :mod (p2 / proper))))
```
1137. " What is a rite ? " asked the little prince . (lpp_1943.1137)

```
(a / ask-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (r / rite
            :domain (a2 / amr-unknown)))
```
1138. " Those also are actions too often neglected , " said the fox . (lpp_1943.1138)

```
(s / say-01
  :ARG0 (f / fox)
  :ARG1 (a / act-02
          :domain (t2 / that)
          :ARG1-of (n2 / neglect-01
                     :frequency (o / often
                                  :degree (t3 / too)))
          :mod (a3 / also)))
```
1139. " They are what make one day different from other days , one hour from other hours . (lpp_1943.1139)

```
(t2 / thing
      :domain (t / they)
      :ARG0-of (m / make-02
            :ARG1 (a / and
                  :op1 (d / differ-02
                        :ARG1 (d2 / day
                              :mod (o4 / one))
                        :ARG2 (d3 / day
                              :mod (o / other)))
                  :op2 (d4 / differ-02
                        :ARG1 (h / hour
                              :mod (o3 / one))
                        :ARG2 (h2 / hour
                              :mod (o2 / other))))))
```
1140. There is a rite , for example , among my hunters . (lpp_1943.1140)

```
(r / rite
      :ARG1-of (h / have-03
            :ARG0 (p / person
                  :ARG0-of (h2 / hunt-01
                        :ARG1 (i / i))))
      :ARG0-of (e / exemplify-01))
```
1141. Every Thursday they dance with the village girls . (lpp_1943.1141)

```
(d / dance-01
      :ARG0 (t / they)
      :ARG2 (g / girl
            :source (v / village))
      :frequency (r / rate-entity-91
            :ARG4 (d2 / date-entity
                  :weekday (t2 / thursday))))
```
1142. So Thursday is a wonderful day for me ! (lpp_1943.1142)

```
(c / cause-01
      :ARG1 (d2 / day
            :domain (d / date-entity
                  :weekday (t / thursday))
            :ARG1-of (w / wonderful-03)
            :beneficiary (i / i)))
```
1143. I can take a walk as far as the vineyards . (lpp_1943.1143)

```
(p / possible-01
      :ARG1 (w / walk-01
            :ARG0 (i / i)
            :extent (f / far
                  :degree (e / equal)
                  :compared-to (v / vineyard))))
```
1144. But if the hunters danced at just any time , every day would be like every other day , and I should never have any vacation at all . " (lpp_1943.1144)

```
(c2 / contrast-01
      :ARG2 (v2 / vacation-01 :polarity -
            :ARG0 (i / i)
            :condition (d / dance-01
                  :ARG0 (p / person
                        :ARG0-of (h2 / hunt-01))
                  :time (a2 / any
                        :mod (j / just))
                  :ARG1-of (c / cause-01
                        :ARG0 (r / resemble-01
                              :ARG1 (d2 / day
                                    :mod (e / every))
                              :ARG2 (d3 / day
                                    :mod (o / other
                                          :mod (e2 / every))))))
            :quant (a4 / any)
            :mod (a3 / at-all)))
```
1145. So the little prince tamed the fox . (lpp_1943.1145)

```
(c / cause-01
      :ARG1 (t / tame-01
            :ARG0 (p / prince
                  :mod (l / little))
            :ARG1 (f / fox)))
```
1146. And when the hour of his departure drew near - - " Ah , " said the fox , " I shall cry . " (lpp_1943.1146)

```
(a / and
      :op1 (s / say-01
            :ARG0 (f / fox)
            :ARG1 (a2 / and
                  :op1 (a3 / ah :mode expressive)
                  :op2 (c / cry-02
                        :ARG0 f))
            :time (h2 / hour
                  :time-of (d / depart-01
                        :ARG0 f)
                  :ARG1-of (n2 / near-01))))
```
1147. " It is your own fault , " said the little prince . (lpp_1943.1147)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (f / fault-01
            :ARG1 (y / you)
            :ARG2 (i / it)))
```
1148. " I never wished you any sort of harm ; but you wanted me to tame you ... " (lpp_1943.1148)

```
(c / contrast-01
      :ARG1 (w / wish-01 :polarity -
            :ARG0 (i / i)
            :ARG1 (h / harm-01
                  :ARG1 (y / you)
                  :mod (s / sort
                        :mod (a / any)))
            :ARG2 y
            :time (e / ever))
      :ARG2 (w2 / want-01
            :ARG0 (y2 / you)
            :ARG1 (t / tame-01
                  :ARG0 i
                  :ARG1 y)))
```
1149. " Yes , that is so , " said the fox . (lpp_1943.1149)

```
(s / say-01
      :ARG0 (f / fox)
      :ARG1 (s2 / so
            :domain (t / that)))
```
1150. " But now you are going to cry ! " said the little prince . (lpp_1943.1150)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (c / contrast-01
            :ARG2 (c2 / cry-02
                  :ARG0 (y / you)
                  :time (n / now))))
```
1151. " Yes , that is so , " said the fox . (lpp_1943.1151)

```
(s / say-01
      :ARG0 (f / fox)
      :ARG1 (s2 / so
            :domain (t / that)))
```
1152. " Then it has done you no good at all ! " (lpp_1943.1152)

```
(d / do-02
      :ARG0 (i / it)
      :ARG1 (g / good-04 :polarity -)
      :ARG2 (y / you)
      :mod (a / at-all))
```
1153. " It has done me good , " said the fox , " because of the color of the wheat fields . " (lpp_1943.1153)

```
(s / say-01
      :ARG0 (f2 / fox)
      :ARG1 (d / do-02
            :ARG0 (i / it)
            :ARG1 (g / good-04
                  :ARG1 i
                  :ARG2 f2)
            :ARG2 f2
            :ARG1-of (c / cause-01
                  :ARG0 (c2 / color-01
                        :ARG1 (f / field
                              :mod (w / wheat))))))
```
1154. And then he added : " Go and look again at the roses . (lpp_1943.1154)

```
(a / and
  :op1 (a2 / add-01
         :ARG0 (h / he)
         :ARG1 (a3 / and
                 :op1 (g / go-02
                        :ARG0 (y / you)
                        :mode imperative)
                 :op2 (l / look-01
                        :ARG0 y
                        :ARG1 (r / rose)
                        :mod (a4 / again)
                        :mode imperative))
         :time (t / then)))
```
1155. You will understand now that yours is unique in all the world . (lpp_1943.1155)

```
(u / understand-01
      :ARG0 (y / you)
      :ARG1 (u2 / unique
            :domain (r / rose
                  :poss y)
            :location (w / world
                  :extent (a / all)))
      :time (n / now))
```
1156. Then come back to say goodbye to me , and I will make you a present of a secret . " (lpp_1943.1156)

```
(a / and
      :op1 (c / come-01 :mode imperative
            :ARG1 (y / you)
            :direction (b / back)
            :time (t / then)
            :purpose (s / say-01
                  :ARG0 y
                  :ARG1 (g / goodbye)
                  :ARG2 (i / i)))
      :op2 (g2 / give-01
            :ARG0 i
            :ARG1 (p / present)
            :ARG2 y
            :manner (r / reveal-01
                  :ARG0 i
                  :ARG1 (s2 / secret)
                  :ARG2 y)))
```
1157. The little prince went away , to look again at the roses . (lpp_1943.1157)

```
(g / go-02
  :ARG0 (p / prince
          :mod (l / little))
  :direction (a / away)
  :purpose (l2 / look-01
             :ARG0 p
             :ARG1 (r / rose)
             :mod (a2 / again)))
```
1158. " You are not at all like my rose , " he said . (lpp_1943.1158)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (r / resemble-01 :polarity -
            :ARG1 (y / you)
            :ARG2 (r2 / rose
                  :poss (i / i))
            :degree (a / at-all)))
```
1159. " As yet you are nothing . (lpp_1943.1159)

```
(n / nothing
      :domain (y / you)
      :time (a / as-yet))
```
1160. No one has tamed you , and you have tamed no one . (lpp_1943.1160)

```
(a / and
      :op1 (t / tame-01
            :ARG0 (n / no-one)
            :ARG1 (y / you))
      :op2 (t2 / tame-01
            :ARG0 y
            :ARG1 n))
```
1161. You are like my fox when I first knew him . (lpp_1943.1161)

```
(r / resemble-01
      :ARG1 (y / you)
      :ARG2 (f / fox
            :poss (i / i))
      :time (k / know-02
            :ARG0 i
            :ARG1 f
            :ord (o / ordinal-entity :value 1)))
```
1162. He was only a fox like a hundred thousand other foxes . (lpp_1943.1162)

```
(f2 / fox
      :domain (h / he)
      :ARG1-of (r / resemble-01
            :ARG2 (f3 / fox :quant 100000
                  :mod (o / other)))
      :mod (o2 / only))
```
1163. But I have made him my friend , and now he is unique in all the world . " (lpp_1943.1163)

```
(c / contrast-01
      :ARG2 (m / make-01
            :ARG0 (i / i)
            :ARG1 (h / have-rel-role-91
                  :ARG0 (h2 / he)
                  :ARG1 i
                  :ARG2 (f / friend))
            :ARG0-of (c2 / cause-01
                  :ARG1 (u / unique
                        :domain h2
                        :time (n / now)
                        :location (w / world
                              :extent (a2 / all))))))
```
1164. And the roses were very much embarassed . (lpp_1943.1164)

```
(a / and
      :op1 (e / embarrass-01
            :ARG1 (r / rose)
            :degree (m / much
                  :degree (v / very))))
```
1165. " You are beautiful , but you are empty , " he went on . (lpp_1943.1165)

```
(g / go-on-25
      :ARG0 (h / he)
      :ARG1 (c / contrast-01
            :ARG1 (b / beautiful-02
                  :ARG1 (y / you))
            :ARG2 (e / empty-02
                  :ARG1 y)))
```
1166. " One could not die for you . (lpp_1943.1166)

```
(p / possible-01 :polarity -
      :ARG1 (d / die-01
            :ARG1 (o / one)
            :beneficiary (y / you)))
```
1167. To be sure , an ordinary passerby would think that my rose looked just like you - - the rose that belongs to me . (lpp_1943.1167)

```
(t / think-01
      :ARG0 (p2 / person
            :ARG0-of (p3 / pass-by-17)
            :mod (o / ordinary))
      :ARG1 (l / look-02
            :ARG0 (r / rose
                  :poss (i / i)
                  :ARG0-of (b / belong-01
                        :ARG1 i))
            :ARG1 (y / you)
            :degree (j / just))
      :ARG1-of (s / sure-02))
```
1168. But in herself alone she is more important than all the hundreds of you other roses : because it is she that I have watered ; because it is she that I have put under the glass globe ; because it is she that I have sheltered behind the screen ; because it is for her that I have killed the caterpillars ( except the two or three that we saved to become butterflies ) ; because it is she that I have listened to , when she grumbled , or boasted , or ever sometimes when she said nothing . (lpp_1943.1168)

```
(c4 / contrast-01
      :ARG2 (i / important
            :degree (m / more)
            :domain (s / she
                  :mod (a / alone))
            :compared-to (r / rose
                  :mod (a3 / all)
                  :mod (o / other)
                  :quant (m2 / multiple :op1 100))
            :ARG1-of (c / cause-01
                  :ARG0 (a2 / and
                        :op1 (w / water-01
                              :ARG0 (i2 / i)
                              :ARG1 s)
                        :op2 (p / put-01
                              :ARG0 i2
                              :ARG1 s
                              :ARG2 (u / under
                                    :op1 (g / globe
                                          :consist-of (g2 / glass))))
                        :op3 (s3 / shelter-01
                              :ARG0 i2
                              :ARG1 s
                              :ARG2 (b2 / behind
                                    :op1 (s4 / screen)))
                        :op4 (k / kill-01
                              :ARG0 i2
                              :ARG1 (c2 / caterpillar
                                    :ARG2-of (e2 / except-01
                                          :ARG1 (c3 / caterpillar
                                                :quant (o2 / or :op1 2 :op2 3)
                                                :ARG1-of (s2 / save-02
                                                      :ARG0 (w2 / we)
                                                      :purpose (b3 / become-01
                                                            :ARG1 c3
                                                            :ARG2 (b4 / butterfly))))))
                              :beneficiary s)
                        :op4 (l / listen-01
                              :ARG0 i2
                              :ARG1 s
                              :time (o3 / or
                                    :op1 (g3 / grumble-01
                                          :ARG0 s)
                                    :op2 (b5 / boast-01
                                          :ARG0 s)
                                    :op3 (s6 / say-01
                                          :ARG0 s
                                          :ARG1 (n / nothing)
                                          :frequency (s7 / sometimes
                                                :time (e / ever)))))))))
```
1169. Because she is my rose . (lpp_1943.1169)

```
(c / cause-01
      :ARG0 (r / rose
            :domain (s / she)
            :poss (i / i)))
```
1170. And he went back to meet the fox . (lpp_1943.1170)

```
(a / and
      :op1 (g / go-02
            :ARG0 (h / he)
            :direction (b / back)
            :purpose (m / meet-03
                  :ARG0 h
                  :ARG1 (f / fox))))
```
1171. " Goodbye , " he said . (lpp_1943.1171)

```
(s / say-01
  :ARG0 (h / he)
  :ARG1 (g / goodbye))
```
1172. " Goodbye , " said the fox . (lpp_1943.1172)

```
(s / say-01
      :ARG0 (f / fox)
      :ARG1 (g / goodbye))
```
1173. " And now here is my secret , a very simple secret : It is only with the heart that one can see rightly ; what is essential is invisible to the eye . " (lpp_1943.1173)

```
(a / and
      :op1 (s / secret
            :poss (i / i)
            :ARG1-of (s2 / simple-02
                  :degree (v / very))
            :domain (a2 / and
                  :op1 (p / possible-01
                        :ARG1 (s3 / see-01
                              :ARG0 (o2 / one)
                              :ARG2-of (r / right-06)
                              :instrument (h2 / heart))
                        :mod (o / only))
                  :op2 (p2 / possible-01 :polarity -
                        :ARG1 (s4 / see-01
                              :ARG0 o2
                              :ARG1 (t / thing
                                    :mod (e / essential))
                              :instrument (e2 / eye))))
            :time (n / now)))
```
1174. " What is essential is invisible to the eye , " the little prince repeated , so that he would be sure to remember . (lpp_1943.1174)

```
(r / repeat-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (p2 / possible-01 :polarity -
            :ARG1 (s2 / see-01
                  :ARG1 (t / thing
                        :mod (e / essential))
                  :instrument (e2 / eye)))
      :purpose (r2 / remember-01
            :ARG0 p
            :ARG1 p2
            :ARG1-of (s / sure-02)))
```
1175. " It is the time you have wasted for your rose that makes your rose so important . " (lpp_1943.1175)

```
(t / time
      :ARG1-of (w / waste-01
            :ARG0 (y / you)
            :beneficiary (r / rose
                  :poss y))
      :ARG0-of (m / make-02
            :ARG1 (i / important
                  :domain r
                  :degree (s / so))))
```
1176. " It is the time I have wasted for my rose - - " said the little prince , so that he would be sure to remember . (lpp_1943.1176)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (t / time
            :ARG1-of (w / waste-01
                  :ARG0 p)
            :beneficiary (r / rose
                  :poss p))
      :purpose (r2 / remember-01
            :ARG0 p
            :ARG1-of (s2 / sure-02)))
```
1177. " Men have forgotten this truth , " said the fox . (lpp_1943.1177)

```
(s / say-01
      :ARG0 (f / fox)
      :ARG1 (f2 / forget-01
            :ARG0 (m / man)
            :ARG1 (t / truth
                  :mod (t2 / this))))
```
1178. " But you must not forget it . (lpp_1943.1178)

```
(c / contrast-01
      :ARG2 (o / obligate-01
            :ARG1 (y / you)
            :ARG2 (f / forget-01 :polarity -
                  :ARG0 y
                  :ARG1 (i / it))))
```
1179. You become responsible , forever , for what you have tamed . (lpp_1943.1179)

```
(b / become-01
      :ARG1 (y / you)
      :ARG2 (r / responsible-03
            :ARG0 y
            :ARG1 (t2 / thing
                  :ARG1-of (t / tame-01
                        :ARG0 y))
            :extent (f / forever)))
```
1180. You are responsible for your rose ... " (lpp_1943.1180)

```
(r / responsible-03
      :ARG0 (y / you)
      :ARG1 (r2 / rose
            :poss y))
```
1181. " I am responsible for my rose , " the little prince repeated , so that he would be sure to remember . (lpp_1943.1181)

```
(r / repeat-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (r2 / responsible-03
            :ARG0 p
            :ARG1 (r3 / rose
                  :poss p))
      :purpose (r4 / remember-01
            :ARG0 p
            :ARG1-of (s / sure-02)))
```
1182. Chapter 22 . (lpp_1943.1182)

```
(c / chapter :mod 22)
```
1183. " Good morning , " said the little prince . (lpp_1943.1183)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (m / morning
            :ARG1-of (g / good-02)))
```
1184. " Good morning , " said the railway switchman . (lpp_1943.1184)

```
(s / say-01
      :ARG0 (s2 / switchman
            :mod (r / railway))
      :ARG1 (m / morning
            :ARG1-of (g / good-02)))
```
1185. " What do you do here ? " the little prince asked . (lpp_1943.1185)

```
(a / ask-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (d / do-02
            :ARG0 (y / you)
            :ARG1 (a2 / amr-unknown)
            :location (h / here)))
```
1186. " I sort out travelers , in bundles of a thousand , " said the switchman . (lpp_1943.1186)

```
(s / say-01
  :ARG0 (s2 / switchman)
  :ARG1 (s3 / sort-01
          :ARG0 s2
          :ARG1 (p / person
                  :ARG0-of (t / travel-01))
          :ARG2 (b / bundle-01
                  :ARG0 s2
                  :ARG1 p
                  :ARG2 (p2 / person
                          :quant 1000))))
```
1187. " I send off the trains that carry them ; now to the right , now to the left . " (lpp_1943.1187)

```
(s / send-03
      :ARG0 (i / i)
      :ARG1 (t / train
            :ARG0-of (c / carry-01
                  :ARG1 (t2 / they)))
      :ARG5 (a / and
            :op1 (r / right-04
                  :time (n / now))
            :op2 (l / left-20
                  :time (n2 / now))))
```
1188. And a brilliantly lighted express train shook the switchman 's cabin as it rushed by with a roar like thunder . (lpp_1943.1188)

```
(a / and
      :op2 (s / shake-01
            :ARG0 (t / train
                  :mod (e / express-02)
                  :ARG1-of (l / light-04
                        :manner (b / brilliant-02)))
            :ARG1 (c / cabin
                  :poss (s2 / switchman))
            :time (r / rush-01
                  :ARG1 t
                  :direction (b2 / by)
                  :ARG0-of (r2 / roar-01
                        :ARG1-of (r3 / resemble-01
                              :ARG2 (t2 / thunder))))))
```
1189. " They are in a great hurry , " said the little prince . (lpp_1943.1189)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (h / hurry-01
            :ARG1 (t / they)
            :degree (g / great)))
```
1190. " What are they looking for ? " (lpp_1943.1190)

```
(l / look-01
      :ARG0 (t / they)
      :ARG1 (a / amr-unknown))
```
1191. " Not even the locomotive engineer knows that , " said the switchman . (lpp_1943.1191)

```
(s / say-01
      :ARG0 (s2 / switchman)
      :ARG1 (k / know-01 :polarity -
            :ARG0 (p / person
                  :ARG0-of (e / engineer-01
                        :ARG1 (l / locomotive))
                  :mod (e2 / even))
            :ARG1 (t / that)))
```
1192. And a second brilliantly lighted express thundered by , in the opposite direction . (lpp_1943.1192)

```
(a / and
      :op2 (t / thunder-01
            :ARG0 (t2 / train
                  :mod (e / express-02)
                  :ARG1-of (l / light-04
                        :manner (b2 / brilliant-02))
                  :ord (o2 / ordinal-entity :value 2))
            :direction (b / by)
            :direction (o / opposite-01
                  :ARG2 (d / direction))))
```
1193. " Are they coming back already ? " demanded the little prince . (lpp_1943.1193)

```
(d / demand-01 :mode interrogative
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (c / come-01
            :ARG1 (t / they)
            :direction (b / back)
            :time (a / already)))
```
1194. " These are not the same ones , " said the switchman . (lpp_1943.1194)

```
(s / say-01
  :ARG0 (s2 / switchman)
  :ARG1 (o / one
          :ARG1-of (s3 / same-01
                     :polarity -)
          :domain (t / this)))
```
1195. " It is an exchange . " (lpp_1943.1195)

```
(e / exchange-01
      :domain (i / it))
```
1196. " Were they not satisfied where they were ? " asked the little prince . (lpp_1943.1196)

```
(a / ask-01 :mode interrogative
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (s / satisfy-01 :polarity -
            :ARG1 (t / they)
            :location-of (t2 / they)))
```
1197. " No one is ever satisfied where he is , " said the switchman . (lpp_1943.1197)

```
(s / say-01
      :ARG0 (s2 / switchman)
      :ARG1 (s3 / satisfy-01
            :ARG1 (n / no-one)
            :time (e / ever)
            :location n))
```
1198. And they heard the roaring thunder of a third brilliantly lighted express . (lpp_1943.1198)

```
(a / and
      :op2 (h / hear-01
            :ARG0 (t / they)
            :ARG1 (t2 / thunder-01
                  :ARG1-of (r / roar-01))
            :ARG2 (t3 / train
                  :mod (e / express-02)
                  :ARG1-of (l / light-04
                        :manner (b / brilliant-02))
                  :ord (o / ordinal-entity :value 3))))
```
1199. " Are they pursuing the first travelers ? " demanded the little prince . (lpp_1943.1199)

```
(d / demand-01 :mode interrogative
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (p2 / pursue-01
            :ARG0 (t / they)
            :ARG1 (p3 / person
                  :ARG0-of (t2 / travel-01
                        :ord (o / ordinal-entity :value 1)))))
```
1200. " They are pursuing nothing at all , " said the switchman . (lpp_1943.1200)

```
(s / say-01
  :ARG0 (s2 / switchman)
  :ARG1 (p / pursue-01
          :ARG0 (t / they)
          :ARG1 (n / nothing
                  :extent (a / at-all))))
```
1201. " They are asleep in there , or if they are not asleep they are yawning . (lpp_1943.1201)

```
(o / or
      :op1 (s / sleep-01
            :ARG0 (t / they)
            :location (t2 / there))
      :op2 (y / yawn-01
            :ARG0 t
            :condition (s2 / sleep-01 :polarity -
                  :ARG0 t)))
```
1202. Only the children are flattening their noses against the windowpanes . " (lpp_1943.1202)

```
(f / flatten-01
      :ARG0 (c / child
            :mod (o / only))
      :ARG1 (n / nose
            :part-of c)
      :ARG1-of (c2 / cause-01
            :ARG0 (p / push-01
                  :ARG0 c
                  :ARG1 n
                  :ARG2 (w / windowpane))))
```
1203. " Only the children know what they are looking for , " said the little prince . (lpp_1943.1203)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (k / know-01
            :ARG0 (c / child
                  :mod (o / only))
            :ARG1 (t / thing
                  :ARG1-of (l2 / look-01
                        :ARG0 c))))
```
1204. " They waste their time over a rag doll and it becomes very important to them ; and if anybody takes it away from them , they cry ... " (lpp_1943.1204)

```
(a / and
      :op1 (c3 / cause-01
            :ARG0 (w / waste-01
                  :ARG0 (t / they)
                  :ARG1 (t2 / time
                        :poss t)
                  :ARG1-of (c / cause-01
                        :ARG0 (d / doll
                              :mod (r / rag))))
            :ARG1 (b / become-01
                  :ARG1 d
                  :ARG2 (i / important
                        :ARG1-of (o / opine-01
                              :ARG0 t)
                        :degree (v / very))))
      :op2 (c2 / cry-02
            :ARG0 t
            :condition (t3 / take-away-05
                  :ARG0 (a3 / anybody)
                  :ARG1 d
                  :source t)))
```
1205. " They are lucky , " the switchman said . (lpp_1943.1205)

```
(s / say-01
      :ARG0 (s2 / switchman)
      :ARG1 (l / lucky
            :domain (t / they)))
```
1206. Chapter 23 . (lpp_1943.1206)

```
(c / chapter :mod 23)
```
1207. " Good morning , " said the little prince . (lpp_1943.1207)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (m / morning
            :ARG1-of (g / good-02)))
```
1208. " Good morning , " said the merchant . (lpp_1943.1208)

```
(s / say-01
      :ARG0 (p / person
            :ARG0-of (m / merchandise-01))
      :ARG1 (m2 / morning
            :ARG1-of (g / good-02)))
```
1209. This was a merchant who sold pills that had been invented to quench thirst . (lpp_1943.1209)

```
(s / sell-01
      :ARG0 (p / person
            :ARG0-of (m / merchandise-01)
            :domain (t2 / this))
      :ARG1 (p2 / pill
            :ARG1-of (i / invent-01)
            :purpose (q / quench-01
                  :ARG0 p2
                  :ARG1 (t / thirst-01))))
```
1210. You need only swallow one pill a week , and you would feel no need of anything to drink . (lpp_1943.1210)

```
(c / cause-01
      :ARG0 (n / need-01
            :ARG0 (y / you)
            :ARG1 (s / swallow-01
                  :ARG1 (r / rate-entity-91
                        :ARG1 (p / pill :quant 1)
                        :ARG3 (t / temporal-quantity :quant 1
                              :unit (w / week))))
            :mod (o / only))
      :ARG1 (f / feel-01 :polarity -
            :ARG0 y
            :ARG1 (n2 / need-01
                  :ARG0 y
                  :ARG1 (d / drink-01
                        :ARG0 y
                        :ARG1 (a2 / anything)))))
```
1211. " Why are you selling those ? " asked the little prince . (lpp_1943.1211)

```
(a / ask-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (s / sell-01
            :ARG0 (y / you)
            :ARG1 (t / that)
            :ARG1-of (c / cause-01
                  :ARG0 (a2 / amr-unknown))))
```
1212. " Because they save a tremendous amount of time , " said the merchant . (lpp_1943.1212)

```
(s / say-01
  :ARG0 (p / person
          :ARG0-of (m / merchandise-01))
  :ARG1 (c / cause-01
          :ARG0 (t / they)
          :ARG1 (s2 / save-01
                  :ARG0 t
                  :ARG1 (t2 / time
                          :ARG1-of (a / amount-01
                                     :ARG2 (t3 / tremendous))))))
```
1213. " Computations have been made by experts . (lpp_1943.1213)

```
(m / make-01
      :ARG0 (p / person
            :ARG1-of (e / expert-01))
      :ARG1 (t / thing
            :ARG1-of (c / compute-01)))
```
1214. With these pills , you save fifty - three minutes in every week . " (lpp_1943.1214)

```
(s / save-03
      :ARG0 (y / you)
      :ARG1 (r / rate-entity-91
            :ARG1 (t / temporal-quantity :quant 53
                  :unit (m / minute))
            :ARG2 (t3 / temporal-quantity :quant 1
                  :unit (w / week)))
      :instrument (p / pill
            :mod (t2 / this)))
```
1215. " And what do I do with those fifty - three minutes ? " (lpp_1943.1215)

```
(a / and
      :op1 (d / do-02
            :ARG0 (i / i)
            :ARG1 (a2 / amr-unknown)
            :ARG2 (t / temporal-quantity :quant 53
                  :unit (m / minute)
                  :mod (t2 / that))))
```
1216. " Anything you like ... " (lpp_1943.1216)

```
(d / do-02
      :ARG0 (y2 / you)
      :ARG1 (a2 / anything
            :ARG1-of (l / like-02
                  :ARG0 y2)))
```
1217. " As for me , " said the little prince to himself , " if I had fifty - three minutes to spend as I liked , I should walk at my leisure toward a spring of fresh water . " (lpp_1943.1217)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (w / walk-01
            :ARG0 (i / i)
            :direction (t / toward
                  :destination (s2 / spring
                        :source-of (w2 / water
                              :ARG1-of (f / fresh-04))))
            :manner (l2 / leisure
                  :poss p)
            :condition (h / have-03
                  :ARG0 p
                  :ARG1 (t2 / temporal-quantity :quant 53
                        :unit (m / minute)
                        :ARG1-of (s3 / spend-02
                              :ARG2 (l3 / like-02
                                    :ARG0 p)))))
      :ARG2 p)
```
1218. Chapter 24 . (lpp_1943.1218)

```
(c / chapter
  :mod 24)
```
1219. It was now the eighth day since I had had my accident in the desert , and I had listened to the story of the merchant as I was drinking the last drop of my water supply . (lpp_1943.1219)

```
(a / and
      :op1 (p / pass-03
            :ARG1 (t2 / temporal-quantity :quant 8
                  :unit (d / day))
            :time (s / since
                  :op1 (a2 / accident
                        :poss (i / i)
                        :location (d2 / desert))))
      :op2 (l / listen-01
            :ARG0 i
            :ARG1 (s2 / story
                  :poss (p2 / person
                        :ARG0-of (m2 / merchandise-01)))
            :time (d3 / drink-01
                  :ARG0 i
                  :ARG1 (d4 / drop
                        :part-of (w / water
                              :ARG1-of (s3 / supply-01
                                    :ARG2 i))
                        :ord (o / ordinal-entity :value "-1")))))
```
1220. " Ah , " (lpp_1943.1220)

```
(a / ah :mode expressive)
```
1221. I said to the little prince , " these memories of yours are very charming ; but I have not yet succeeded in repairing my plane ; I have nothing more to drink ; and I , too , should be very happy if I could walk at my leisure toward a spring of fresh water ! " (lpp_1943.1221)

```
(s / say-01
      :ARG0 (i / i)
      :ARG1 (a / and
            :op1 (c2 / charm-01
                  :ARG0 (m / memory
                        :poss (y / you)
                        :mod (t / this))
                  :concession-of (a2 / and
                        :op1 (s2 / succeed-01 :polarity -
                              :ARG0 i
                              :ARG1 (r / repair-01
                                    :ARG0 i
                                    :ARG1 (p2 / plane
                                          :poss i))
                              :time (y2 / yet))
                        :op2 (h / have-03
                              :ARG0 i
                              :ARG1 (n / nothing
                                    :purpose (d / drink-01
                                          :ARG0 i)))
                        :op3 (h2 / happy-01
                              :ARG1 i
                              :degree (v2 / very)
                              :condition (p3 / possible-01
                                    :ARG1 (w / walk-01
                                          :ARG0 i
                                          :direction (s3 / spring
                                                :source-of (w2 / water
                                                      :ARG1-of (f / fresh-04)))
                                          :manner (a3 / at
                                                :op1 (l2 / leisure
                                                      :poss i))))))
                  :degree (v / very)))
      :ARG2 (p / prince
            :mod (l / little)))
```
1222. " My friend the fox - - " the little prince said to me . (lpp_1943.1222)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (f / fox
            :ARG0-of (h / have-rel-role-91
                  :ARG1 i
                  :ARG2 (f2 / friend)))
      :ARG2 (i / i))
```
1223. " My dear little man , this is no longer a matter that has anything to do with the fox ! " (lpp_1943.1223)

```
(s / say-01
  :ARG0 (i / i)
  :ARG1 (c / concern-02
          :ARG0 (m2 / matter
                  :domain (t / this))
          :ARG1 (f / fox)
          :time (n / no-longer))
  :ARG2 (m / man
          :mod (l / little)
          :poss i
          :mod (d / dear)))
```
1224. " Why not ? " (lpp_1943.1224)

```
(c2 / concern-02
  :polarity -
  :ARG1-of (c3 / cause-01
             :ARG0 (a / amr-unknown)))
```
1225. " Because I am about to die of thirst ... " (lpp_1943.1225)

```
(c / cause-01
      :ARG0 (d / die-01
            :ARG1 (i / i)
            :ARG1-of (c2 / cause-01
                  :ARG0 (t / thirst-01
                        :ARG0 i))
            :time (a / about-to)))
```
1226. He did not follow my reasoning , and he answered me : " It is a good thing to have had a friend , even if one is about to die . (lpp_1943.1226)

```
(a / and
      :op1 (f / follow-02 :polarity -
            :ARG0 (h / he)
            :ARG1 (r / reason-01
                  :ARG0 (i / i)))
      :op2 (a2 / answer-01
            :ARG0 h
            :ARG1 i
            :ARG2 (g / good-02
                  :ARG1 (h2 / have-rel-role-91
                        :ARG1 o
                        :ARG2 (f2 / friend))
                  :concession (e / even-if
                        :op1 (d / die-01
                              :ARG1 (o / one)
                              :time (a3 / about-to))))))
```
1227. I , for instance , am very glad to have had a fox as a friend ... " (lpp_1943.1227)

```
(g / glad-02
      :ARG0 (h / have-rel-role-91
            :ARG0 (f2 / fox)
            :ARG1 i
            :ARG2 (f / friend))
      :ARG1 (i / i
            :ARG0-of (e / exemplify-01))
      :degree (v / very))
```
1228. " He has no way of guessing the danger , " (lpp_1943.1228)

```
(p / possible-01
  :ARG1 (g / guess-01
            :ARG0 (h / he)
            :ARG1 (d / danger))
  :polarity -)
```
1229. I said to myself . (lpp_1943.1229)

```
(s / say-01
  :ARG0 (i / i)
  :ARG2 i)
```
1230. " He has never been either hungry or thirsty . (lpp_1943.1230)

```
(a / and
  :op1 (h / hunger-01
         :ARG0 (h2 / he)
         :polarity -)
  :op2 (t / thirst-01
         :ARG0 h2
         :polarity -)
  :time (e / ever))
```
1231. A little sunshine is all he needs ... " (lpp_1943.1231)

```
(n / need-01
  :ARG0 (h / he)
  :ARG1 (s / sunshine
          :quant (l / little))
  :mod (a / all))
```
1232. But he looked at me steadily , and replied to my thought : " I am thirsty , too . (lpp_1943.1232)

```
(c / contrast-01
  :ARG2 (a2 / and
          :op1 (l / look-01
                 :ARG0 (h / he)
                 :ARG1 (i / i)
                 :manner (s / steady))
          :op2 (r / reply-01
                 :ARG0 h
                 :ARG1 (t / thing
                         :ARG1-of (t2 / think-01
                                    :ARG0 i))
                 :ARG2 (t3 / thirst-01
                         :ARG0 h
                         :mod (t4 / too)))))
```
1233. Let us look for a well ... " (lpp_1943.1233)

```
(l / look-01
  :ARG0 (w / we)
  :ARG1 (w2 / well)
  :mode imperative)
```
1234. I made a gesture of weariness . (lpp_1943.1234)

```
(g2 / gesture-01
      :ARG0 (i / i)
      :ARG1 (w / weary-01
            :ARG1 i))
```
1235. It is absurd to look for a well , at random , in the immensity of the desert . (lpp_1943.1235)

```
(a / absurd
  :domain (l / look-01
            :ARG1 (w / well)
            :location (d / desert
                        :mod (i / immense))
            :manner (r / random)))
```
1236. But nevertheless we started walking . (lpp_1943.1236)

```
(h / have-concession-91
  :ARG1 (s / start-01
          :ARG0 (w / we)
          :ARG1 (w2 / walk-01)))
```
1237. When we had trudged along for several hours , in silence , the darkness fell , and the stars began to come out . (lpp_1943.1237)

```
(a / and
      :op1 (f / fall-04
            :ARG1 (d / darkness))
      :op2 (b / begin-01
            :ARG0 (s / star)
            :ARG1 (c / come-out-09
                  :ARG1 s))
      :time (t / trudge-01
            :ARG0 (w / we)
            :duration (s2 / several
                  :op1 (t2 / temporal-quantity :quant 1
                        :unit (h / hour)))
            :manner (s3 / silent)))
```
1238. Thirst had made me a little feverish , and I looked at them as if I were in a dream . (lpp_1943.1238)

```
(a / and
      :op1 (m / make-02
            :ARG0 (t / thirst-01
                  :ARG0 (i / i))
            :ARG1 (f / feverish
                  :domain i
                  :degree (l / little)))
      :op2 (l2 / look-01
            :ARG0 i
            :ARG1 (t2 / they)
            :ARG1-of (r / resemble-01
                  :ARG2 (d / dream-01
                        :ARG0 i))))
```
1239. The little prince 's last words came reeling back into my memory : " Then you are thirsty , too ? " (lpp_1943.1239)

```
(c / come-01
      :ARG1 (w / word-01
            :ARG0 (p / prince
                  :mod (l2 / little))
            :ARG1 (t / thirst-01 :mode interrogative
                  :ARG0 (y / you
                        :mod (t2 / too)))
            :mod (l / last))
      :ARG4 (m / memory
            :poss (i / i))
      :manner (r / reel-03
            :ARG1 w
            :ARG2 m))
```
1240. I demanded . (lpp_1943.1240)

```
(d / demand-01
      :ARG0 (i / i))
```
1241. But he did not reply to my question . (lpp_1943.1241)

```
(c / contrast-01
  :ARG2 (r / reply-01
          :ARG0 (h / he)
          :ARG1 (q / question-01
                  :ARG0 (i / i))
          :polarity -))
```
1242. He merely said to me : " Water may also be good for the heart ... " (lpp_1943.1242)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (p / possible-01
            :ARG1 (g / good-04
                  :ARG1 (w / water)
                  :ARG2 (h2 / heart)
                  :mod (a / also)))
      :ARG2 (i / i)
      :mod (m / mere))
```
1243. I did not understand this answer , but I said nothing . (lpp_1943.1243)

```
(u2 / understand-01
  :ARG0 (i / i)
  :ARG1 (a / answer
          :mod (t / this))
  :polarity -
  :concession-of (s / say-01
                   :ARG0 i
                   :ARG1 (n / nothing)))
```
1244. I knew very well that it was impossible to cross - examine him . (lpp_1943.1244)

```
(k / know-01
      :ARG0 (i / i)
      :ARG1 (p / possible-01 :polarity -
            :ARG1 (c / crossexamine-01
                  :ARG0 i
                  :ARG1 (h / he)))
      :degree (w / well
            :degree (v / very)))
```
1245. He was tired . (lpp_1943.1245)

```
(t / tire-01
      :ARG1 (h / he))
```
1246. He sat down . (lpp_1943.1246)

```
(s / sit-down-02
  :ARG1 (h / he))
```
1247. I sat down beside him . (lpp_1943.1247)

```
(s / sit-down-02
  :ARG1 (i / i)
  :location (b / beside
              :op1 (h / he)))
```
1248. And , after a little silence , he spoke again : " The stars are beautiful , because of a flower that can not be seen . " (lpp_1943.1248)

```
(a / and
      :op2 (s / speak-01
            :ARG0 (h / he)
            :ARG1 (b / beautiful-02
                  :ARG1 (s5 / star)
                  :ARG1-of (c / cause-01
                        :ARG0 (f / flower
                              :ARG1-of (s6 / see-01
                                    :ARG1-of (p / possible-01 :polarity -)))))
            :time (a2 / after
                  :op1 (s2 / silent
                        :duration (l / little)))
            :mod (a3 / again)))
```
1249. I replied , " Yes , that is so . " (lpp_1943.1249)

```
(r / reply-01
  :ARG0 (i / i)
  :ARG2 (s / so
          :domain (t / that)))
```
1250. And , without saying anything more , I looked across the ridges of sand that were stretched out before us in the moonlight . (lpp_1943.1250)

```
(a / and
      :op2 (l / look-01
            :ARG0 (i / i)
            :ARG1 (a3 / across
                  :op1 (r / ridge
                        :consist-of (s / sand)
                        :ARG1-of (s2 / stretch-out-02
                              :location (b / before
                                    :op1 (w / we)))
                        :ARG1-of (l2 / light-04
                              :ARG0 (m / moon))))
            :manner (s3 / say-01 :polarity -
                  :ARG0 i
                  :ARG1 (a2 / anything
                        :mod (m2 / more)))))
```
1251. " The desert is beautiful , " the little prince added . (lpp_1943.1251)

```
(a / add-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (b / beautiful-02
            :ARG1 (d / desert)))
```
1252. And that was true . (lpp_1943.1252)

```
(a / and
      :op2 (t / true-01
            :ARG1 (t2 / that)))
```
1253. I have always loved the desert . (lpp_1943.1253)

```
(l / love-01
      :ARG0 (i / i)
      :ARG1 (d / desert)
      :time (a / always))
```
1254. One sits down on a desert sand dune , sees nothing , hears nothing . (lpp_1943.1254)

```
(a / and
      :op1 (s / sit-down-02
            :ARG1 (o / one)
            :location (d / dune
                  :consist-of (s2 / sand)
                  :location (d2 / desert)))
      :op2 (s3 / see-01
            :ARG0 o
            :ARG1 (n / nothing))
      :op3 (h / hear-01
            :ARG0 o
            :ARG1 (n2 / nothing)))
```
1255. Yet through the silence something throbs , and gleams ... (lpp_1943.1255)

```
(a2 / and
      :op1 (t / throb-01
            :ARG1 (s / something))
      :op2 (g / gleam-01
            :ARG0 s)
      :concession (s2 / silent))
```
1256. " What makes the desert beautiful , " said the little prince , " is that somewhere it hides a well ... " (lpp_1943.1256)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (m / make-02
            :ARG0 (h / hide-01
                  :ARG0 d
                  :ARG1 (w / well)
                  :location (s2 / somewhere))
            :ARG1 (b / beautiful-02
                  :ARG1 (d / desert))))
```
1257. I was astonished by a sudden understanding of that mysterious radiation of the sands . (lpp_1943.1257)

```
(a / astonish-01
  :ARG0 (u / understand-01
          :ARG0 i
          :ARG1 (r / radiate-01
                  :ARG0 (s2 / sand)
                  :mod (m / mystery)
                  :mod (t / that))
          :manner (s / sudden))
  :ARG1 (i / i))
```
1258. When I was a little boy I lived in an old house , and legend told us that a treasure was buried there . (lpp_1943.1258)

```
(a / and
  :op1 (l / live-01
         :ARG0 (i / i)
         :location (h / house
                     :mod (o / old))
         :time (b / boy
                 :mod (l2 / little)
                 :domain i))
  :op2 (t / tell-01
         :ARG0 (l3 / legend)
         :ARG1 (b2 / bury-01
                 :ARG1 (t2 / treasure)
                 :location h)
         :ARG2 (w / we)))
```
1259. To be sure , no one had ever known how to find it ; perhaps no one had ever even looked for it . (lpp_1943.1259)

```
(a / and
      :op1 (s / sure-02
            :ARG0 (n / no-one)
            :ARG1 (t / thing
                  :manner-of (f / find-01
                        :ARG0 n
                        :ARG1 (i / it)))
            :time (e2 / ever)
            :mod (t2 / to-be-sure))
      :op2 (p2 / possible-01
            :ARG1 (l / look-01
                  :ARG0 n
                  :ARG1 i
                  :time e2)))
```
1260. But it cast an enchantment over that house . (lpp_1943.1260)

```
(c / contrast-01
  :ARG2 (c2 / cast-01
          :ARG0 (i / it)
          :ARG1 (e / enchant-01)
          :ARG2 (h / house
                  :mod (t / that))))
```
1261. My home was hiding a secret in the depths of its heart ... (lpp_1943.1261)

```
(h / hide-01
      :ARG0 (h2 / home
            :poss (i / i))
      :ARG1 (s / secret)
      :location (d / deep-02
            :ARG1 (h3 / heart
                  :part-of h2)))
```
1262. " Yes , " (lpp_1943.1262)

```
(y / yes)
```
1263. I said to the little prince . (lpp_1943.1263)

```
(s / say-01
  :ARG0 (i / i)
  :ARG2 (p / prince
          :mod (l / little)))
```
1264. " The house , the stars , the desert - - what gives them their beauty is something that is invisible ! " (lpp_1943.1264)

```
(g2 / give-01
      :ARG0 (s3 / something
            :ARG1-of (s4 / see-01
                  :ARG1-of (p / possible-01 :polarity -)))
      :ARG1 (b / beautiful-02
            :ARG1 a)
      :ARG2 (a / and
            :op1 (h / house)
            :op2 (s2 / star)
            :op3 (d / desert)))
```
1265. " I am glad , " he said , " that you agree with my fox . " (lpp_1943.1265)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (g / glad-02
            :ARG0 (a / agree-01
                  :ARG0 (y / you)
                  :ARG2 (f / fox
                        :poss h))
            :ARG1 h))
```
1266. As the little prince dropped off to sleep , I took him in my arms and set out walking once more . (lpp_1943.1266)

```
(a2 / and
      :op1 (t / take-01
            :ARG0 (i / i)
            :ARG1 (p / prince
                  :mod (l / little))
            :ARG3 (a / arm
                  :part-of i))
      :op2 (s / set-out-07
            :ARG0 i
            :manner (w / walk-01)
            :mod (a3 / again :frequency 1))
      :time (d / drop-off-03
            :ARG0 p
            :ARG2 (s2 / sleep-01
                  :ARG0 p)))
```
1267. I felt deeply moved , and stirred . (lpp_1943.1267)

```
(f / feel-01
      :ARG0 (i / i)
      :ARG1 (a / and
            :op1 (m / move-05
                  :ARG1 i
                  :ARG1-of (d / deep-02))
            :op2 (s / stir-02
                  :ARG1 i)))
```
1268. It seemed to me that I was carrying a very fragile treasure . (lpp_1943.1268)

```
(s / seem-01
      :ARG1 (c / carry-01
            :ARG0 i
            :ARG1 (t / treasure
                  :mod (f / fragile
                        :degree (v / very))))
      :ARG2 (i / i))
```
1269. It seemed to me , even , that there was nothing more fragile on all Earth . (lpp_1943.1269)

```
(s / seem-01
      :ARG1 (f / fragile
            :degree (m / more)
            :domain (n2 / nothing
                  :location (p / planet :wiki "Earth"
                        :name (n / name :op1 "Earth")
                        :mod (a / all))))
      :ARG2 (i / i)
      :mod (e / even))
```
1270. In the moonlight I looked at his pale forehead , his closed eyes , his locks of hair that trembled in the wind , and I said to myself : " What I see here is nothing but a shell . (lpp_1943.1270)

```
(a / and
      :op1 (l / look-01
            :ARG0 (i / i)
            :ARG1 (a2 / and
                  :op1 (f / forehead
                        :part-of (h / he)
                        :ARG1-of (p / pale-03))
                  :op2 (e / eye
                        :ARG1-of (c / close-01)
                        :part-of h)
                  :op3 (l2 / lock
                        :consist-of (h2 / hair)
                        :ARG1-of (t / tremble-01
                              :ARG1-of (c2 / cause-01
                                    :ARG0 (w / wind)))
                        :part-of h)
                  :ARG1-of (l3 / light-04
                        :ARG0 (m2 / moon))))
      :op2 (s / say-01
            :ARG0 i
            :ARG1 (s2 / see-01
                  :ARG0 i
                  :ARG1 (s3 / shell)
                  :mod (o / only)
                  :location (h3 / here))
            :ARG2 i))
```
1271. What is most important is invisible ... " (lpp_1943.1271)

```
(s / see-01
  :ARG1 (t / thing
          :mod (i2 / important
                 :degree (m / most)))
  :ARG1-of (p / possible-01
         :polarity -))
```
1272. As his lips opened slightly with the suspicious of a half - smile , I said to myself , again : " What moves me so deeply , about this little prince who is sleeping here , is his loyalty to a flower - - the image of a rose that shines through his whole being like the flame of a lamp , even when he is asleep ... " (lpp_1943.1272)

```
(s / say-01
      :ARG0 (i / i)
      :ARG1 (m / move-05
            :ARG0 (p / prince
                  :mod (l / little)
                  :ARG0-of (s2 / sleep-01
                        :location (h / here)))
            :ARG1 i
            :ARG2 (l2 / loyal-01
                  :ARG1 p
                  :ARG2 (f / flower
                        :op1 (i2 / image
                              :poss (r / rose
                                    :ARG1-of (s3 / shine-01
                                          :ARG2 (t / through
                                                :op1 (b / being
                                                      :poss p
                                                      :mod (w / whole)))
                                          :ARG1-of (r2 / resemble-01
                                                :ARG2 (f2 / flame-01
                                                      :ARG1 (l3 / lamp)))
                                          :concession (e / even-when
                                                :op1 (s6 / sleep-01
                                                      :ARG0 p)))))))
            :ARG1-of (d / deep-02))
      :ARG2 i
      :time (o / open-01
            :ARG1 (l4 / lip
                  :part-of p)
            :degree (s4 / slight)
            :manner (s8 / smile-01
                  :mod (h3 / half)
                  :mod (s5 / suspicious)))
      :mod (a2 / again))
```
1273. And I felt him to be more fragile still . (lpp_1943.1273)

```
(a / and
  :op2 (f / feel-02
         :ARG0 (i / i)
         :ARG1 (f3 / fragile
                 :domain (h / he)
                 :degree (m / more)
                 :mod (s / still))))
```
1274. I felt the need of protecting him , as if he himself were a flame that might be extinguished by a little puff of wind ... (lpp_1943.1274)

```
(f / feel-01
      :ARG0 (i / i)
      :ARG1 (n / need-01
            :ARG0 i
            :ARG1 (p / protect-01
                  :ARG0 i
                  :ARG1 (h / he)
                  :conj-as-if (f2 / flame-01
                        :ARG1 h
                        :ARG1-of (e / extinguish-01
                              :ARG0 (p3 / puff-up-04
                                    :ARG1 (w / wind)
                                    :mod (l / little))
                              :ARG1-of (p2 / possible-01))))))
```
1275. And , as I walked on so , I found the well , at daybreak . (lpp_1943.1275)

```
(a / and
      :op2 (f / find-01
            :ARG0 (i / i)
            :ARG1 (w / well)
            :time (d / daybreak)
            :time (w2 / walk-01
                  :ARG0 i
                  :mod (o / on)
                  :manner (s / so))))
```
1276. Chapter 25 . (lpp_1943.1276)

```
(c / chapter
  :mod 25)
```
1277. " Men , " said the little prince , " set out on their way in express trains , but they do not know what they are looking for . (lpp_1943.1277)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (h / have-concession-91
            :ARG1 (k / know-01 :polarity -
                  :ARG0 m
                  :ARG1 (t2 / thing
                        :ARG1-of (l2 / look-01
                              :ARG0 m)))
            :ARG2 (s2 / set-out-07
                  :ARG0 (m / man)
                  :path (w / way
                        :poss m)
                  :manner (t / train
                        :mod (e / express)))))
```
1278. Then they rush about , and get excited , and turn round and round ... " (lpp_1943.1278)

```
(a / and
  :op1 (r / rush-01
         :ARG1 (t / they)
         :ARG2 (a2 / about))
  :op2 (e / excite-01
         :ARG1 t)
  :op3 (t2 / turn-01
         :ARG1 t
         :direction (a3 / and
                      :op1 (r2 / round)
                      :op2 (r3 / round)))
  :time (t3 / then))
```
1279. And he added : " It is not worth the trouble ... " (lpp_1943.1279)

```
(a / and
      :op2 (a2 / add-01
            :ARG0 (h / he)
            :ARG1 (w / worth-02 :polarity -
                  :ARG1 (i / it)
                  :ARG2 (t / trouble-01))))
```
1280. The well that we had come to was not like the wells of the Sahara . (lpp_1943.1280)

```
(w / well
      :ARG4-of (c / come-01
            :ARG1 (w2 / we))
      :ARG1-of (r / resemble-01 :polarity -
            :ARG2 (w3 / well
                  :location (d / desert :wiki "Sahara"
                        :name (n / name :op1 "Sahara")))))
```
1281. The wells of the Sahara are mere holes dug in the sand . (lpp_1943.1281)

```
(h / hole
      :ARG1-of (d / dig-01
            :ARG2 (s / sand))
      :mod (m / mere)
      :domain (w / well
            :location (d2 / desert :wiki "Sahara" :name (n / name :op1 "Sahara"))))
```
1282. This one was like a well in a village . (lpp_1943.1282)

```
(r / resemble-01
      :ARG1 (w / well
            :mod (t / this))
      :ARG2 (w2 / well
            :location (v / village)))
```
1283. But there was no village here , and I thought I must be dreaming ... (lpp_1943.1283)

```
(c3 / contrast-01
  :ARG2 (a / and
          :op1 (v / village
                 :polarity -
                 :location (h / here))
          :op2 (t / think-01
                 :ARG0 (i / i)
                 :ARG1 (d / dream-01
                         :ARG0 i))))
```
1284. " It is strange , " (lpp_1943.1284)

```
(s / strange
      :domain (i / it))
```
1285. I said to the little prince . (lpp_1943.1285)

```
(s / say-01
  :ARG0 (i / i)
  :ARG2 (p / prince
          :mod (l / little)))
```
1286. " Everything is ready for use : the pulley , the bucket , the rope ... " (lpp_1943.1286)

```
(r / ready-02
      :ARG1 (e / everything
            :example (a / and
                  :op1 (p2 / pulley)
                  :op2 (b / bucket)
                  :op3 (r2 / rope)))
      :ARG2 (u / use-01
            :ARG1 e))
```
1287. He laughed , touched the rope , and set the pulley to working . (lpp_1943.1287)

```
(a / and
      :op1 (l / laugh-01
            :ARG0 (h / he))
      :op2 (t / touch-01
            :ARG0 h
            :ARG1 (r / rope))
      :op3 (s / set-08
            :ARG0 h
            :ARG1 (p / pulley)
            :ARG2 (w / work-09
                  :ARG1 p)))
```
1288. And the pulley moaned , like an old weathervane which the wind has long since forgotten . (lpp_1943.1288)

```
(a / and
  :op2 (m / moan-01
         :ARG0 (p / pulley)
         :ARG1-of (r / resemble-01
                    :ARG2 (m2 / moan-01
                            :ARG0 (w / weathervane
                                    :mod (o / old)
                                    :ARG1-of (f / forget-01
                                               :ARG0 (w2 / wind)
                                               :time (s / since
                                                       :op1 (l / long))))))))
```
1289. " Do you hear ? " said the little prince . (lpp_1943.1289)

```
(s / say-01
  :ARG0 (p / prince
          :mod (l / little))
  :ARG1 (h / hear-01
          :ARG0 (y / you)
          :mode interrogative))
```
1290. " We have wakened the well , and it is singing ... " (lpp_1943.1290)

```
(a / and
  :op1 (w / wake-01
         :ARG0 (w2 / we)
         :ARG1 (w3 / well))
  :op2 (s / sing-01
         :ARG0 w3))
```
1291. I did not want him to tire himself with the rope . (lpp_1943.1291)

```
(w / want-01
  :ARG0 (i / i)
  :ARG1 (t / tire-01
          :ARG0 (h / he)
          :ARG1 h
          :instrument (r / rope))
  :polarity -)
```
1292. " Leave it to me , " (lpp_1943.1292)

```
(l / leave-02
  :ARG0 (y / you)
  :ARG1 (i2 / it)
  :ARG2 (i / i)
  :mode imperative)
```
1293. I said . (lpp_1943.1293)

```
(s / say-01
  :ARG0 (i / i))
```
1294. " It is too heavy for you . " (lpp_1943.1294)

```
(h / heavy
      :domain (i2 / it)
      :degree (t / too)
      :compared-to (y / you))
```
1295. I hoisted the bucket slowly to the edge of the well and set it there - - happy , tired as I was , over my achievement . (lpp_1943.1295)

```
(a / and
      :op1 (h / hoist-01
            :ARG0 (i / i
                  :ARG1-of (c / content-01
                        :ARG2 (t3 / thing
                              :ARG1-of (a2 / achieve-01
                                    :ARG0 i))
                        :concession (a3 / and
                              :op1 (h2 / happy-01
                                    :ARG1 i)
                              :op2 (t2 / tire-01
                                    :ARG1 i))))
            :ARG1 (b / bucket)
            :ARG1-of (s / slow-05)
            :destination (e / edge
                  :part-of (w / well)))
      :op1 (s2 / set-01
            :ARG0 i
            :ARG1 b
            :ARG2 e))
```
1296. The song of the pulley was still in my ears , and I could see the sunlight shimmer in the still trembling water . (lpp_1943.1296)

```
(a / and
      :op1 (h / hear-01
            :ARG0 (i / i)
            :ARG1 (s / sing-01
                  :ARG0 (p / pulley))
            :mod (s2 / still))
      :op2 (p2 / possible-01
            :ARG1 (s3 / see-01
                  :ARG0 i
                  :ARG1 (s4 / shimmer-01
                        :ARG1 (s5 / sunlight)
                        :location (w / water
                              :ARG1-of (t / tremble-01
                                    :mod (s6 / still)))))))
```
1297. " I am thirsty for this water , " said the little prince . (lpp_1943.1297)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (t / thirst-01
            :ARG0 (i / i)
            :ARG1 (w / water
                  :mod (t2 / this))))
```
1298. " Give me some of it to drink ... " (lpp_1943.1298)

```
(g / give-01
  :ARG0 (y / you)
  :ARG1 (t / thing
          :ARG1-of (i3 / include-91
                     :ARG2 (i / it))
          :quant (s / some))
  :ARG2 (i2 / i)
  :mode imperative
  :purpose (d / drink-01
             :ARG0 i2
             :ARG1 t))
```
1299. And I understood what he had been looking for . (lpp_1943.1299)

```
(a / and
  :op2 (u / understand-01
         :ARG0 (i / i)
         :ARG1 (t / thing
                 :ARG1-of (l / look-01
                            :ARG0 (h / he)))))
```
1300. I raised the bucket to his lips . (lpp_1943.1300)

```
(r / raise-01
  :ARG0 (i / i)
  :ARG1 (b / bucket)
  :ARG4 (l / lip
          :part-of (h / he)))
```
1301. He drank , his eyes closed . (lpp_1943.1301)

```
(a / and
  :op1 (d / drink-01
         :ARG0 (h / he))
  :op2 (c / close-01
         :ARG0 h
         :ARG1 (e / eye
                 :part-of h)))
```
1302. It was as sweet as some special festival treat . (lpp_1943.1302)

```
(s / sweet-04
      :ARG1 (i / it)
      :degree (e / equal)
      :compared-to (f2 / food-dish
            :mod (f / festival)
            :mod (s2 / some)
            :ARG1-of (s3 / special-02)
            :ARG1-of (t / treat-02)))
```
1303. This water was indeed a different thing from ordinary nourishment . (lpp_1943.1303)

```
(r2 / resemble-01
  :ARG1 (w / water
          :mod (t / this))
  :ARG2 (t2 / thing
          :ARG2-of (n / nourish-01)
          :mod (o / ordinary))
  :mod (i / indeed)
  :polarity -)
```
1304. Its sweetness was born of the walk under the stars , the song of the pulley , the effort of my arms . (lpp_1943.1304)

```
(b2 / bear-02
      :ARG0 (a / and
            :op1 (w2 / walk-01
                  :location (u / under
                        :op1 (s2 / star)))
            :op2 (s3 / sing-01
                  :ARG0 (p / pulley))
            :op3 (e / effort-01
                  :ARG0 (a2 / arm
                        :part-of (i / i))))
      :ARG1 (s / sweet-05
            :ARG1 (i3 / it)))
```
1305. It was good for the heart , like a present . (lpp_1943.1305)

```
(g / good-04
      :ARG1 (i / it
            :ARG1-of (r / resemble-01
                  :ARG2 (p / present)))
      :ARG2 (h / heart))
```
1306. When I was a little boy , the lights of the Christmas tree , the music of the Midnight Mass , the tenderness of smiling faces , used to make up , so , the radiance of the gifts I received . (lpp_1943.1306)

```
(m / make-up-07
      :ARG0 (a / and
            :op1 (l / light-04
                  :ARG0 (t2 / tree
                        :mod (f2 / festival :wiki "Christmas" :name (n / name :op1 "Christmas"))))
            :op2 (m2 / music
                  :poss (e2 / event :wiki - :name (n2 / name :op1 "Midnight" :op2 "Mass")))
            :op3 (t4 / tender
                  :domain (f / face
                        :ARG0-of (s2 / smile-01))))
      :ARG1 (r3 / radiant
            :domain (g2 / gift
                  :ARG1-of (r4 / receive-01
                        :ARG0 (i / i))))
      :manner (s / so)
      :time (b / boy
            :mod (l2 / little)
            :domain i))
```
1307. " The men where you live , " said the little prince , " raise five thousand roses in the same garden - - and they do not find in it what they are looking for . " (lpp_1943.1307)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (a / and
            :op1 (r / raise-03
                  :ARG0 (m / man
                        :location (l2 / live-01
                              :ARG0 (y / you)))
                  :ARG1 (r2 / rose :quant 5000)
                  :location (g / garden
                        :ARG1-of (s2 / same-01)))
            :op2 (f / find-01 :polarity -
                  :ARG0 m
                  :ARG1 (t / thing
                        :ARG1-of (l3 / look-01
                              :ARG0 m))
                  :location g)))
```
1308. " They do not find it , " (lpp_1943.1308)

```
(f / find-01
  :ARG0 (t / they)
  :ARG1 (i / it)
  :polarity -)
```
1309. I replied . (lpp_1943.1309)

```
(r / reply-01
  :ARG0 (i / i))
```
1310. " And yet what they are looking for could be found in one single rose , or in a little water . " (lpp_1943.1310)

```
(c / contrast-01
      :ARG2 (p2 / possible-01
            :ARG1 (f / find-01
                  :ARG1 (t / thing
                        :ARG1-of (l2 / look-01
                              :ARG0 (t2 / they)))
                  :location (o / or
                        :op1 (r / rose
                              :ARG1-of (s / single-02))
                        :op2 (w / water
                              :quant (l3 / little))))))
```
1311. " Yes , that is true , " (lpp_1943.1311)

```
(t / true-01
      :ARG1 (t2 / that))
```
1312. I said . (lpp_1943.1312)

```
(s / say-01
      :ARG0 (i / i))
```
1313. And the little prince added : " But the eyes are blind . (lpp_1943.1313)

```
(a / and
      :op2 (a2 / add-01
            :ARG0 (p / prince
                  :mod (l / little))
            :ARG1 (c / contrast-01
                  :ARG2 (b / blind-02
                        :ARG1 (e / eye)))))
```
1314. One must look with the heart ... " (lpp_1943.1314)

```
(r / recommend-01
  :ARG1 (l / look-01
          :ARG0 (o / one)
          :instrument (h / heart)))
```
1315. I had drunk the water . (lpp_1943.1315)

```
(d / drink-01
  :ARG0 (i / i)
  :ARG1 (w / water))
```
1316. I breathed easily . (lpp_1943.1316)

```
(b / breathe-01
      :ARG0 (i / i)
      :ARG1-of (e / easy-05))
```
1317. At sunrise the sand is the color of honey . (lpp_1943.1317)

```
(r2 / resemble-01
  :ARG1 (c / color
          :poss (s / sand))
  :ARG2 (c2 / color
          :poss (h / honey))
  :time (r / rise-01
          :ARG1 (s2 / sun)))
```
1318. And that honey color was making me happy , too . (lpp_1943.1318)

```
(a / and
      :op2 (m / make-02
            :ARG0 (c / color
                  :mod (h / honey))
            :ARG1 (h2 / happy-01
                  :ARG1 (i / i))
            :mod (t / too)))
```
1319. What brought me , then , this sense of grief ? (lpp_1943.1319)

```
(b2 / bring-01
      :ARG0 (a / amr-unknown)
      :ARG1 (s / sense-01
            :ARG0 i
            :ARG1 (g / grieve-01
                  :ARG1 i)
            :mod (t / this))
      :ARG2 (i / i)
      :time (t2 / then))
```
1320. " You must keep your promise , " said the little prince , softly , as he sat down beside me once more . (lpp_1943.1320)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (o / obligate-01
            :ARG1 (y / you)
            :ARG2 (h / honor-02
                  :ARG0 y
                  :ARG1 (t / thing
                        :ARG1-of (p2 / promise-01
                              :ARG0 y))))
      :manner (s2 / soft)
      :time (s3 / sit-down-02
            :ARG1 p
            :location (b / beside
                  :op1 (i / i))
            :mod (a / again :frequency 1)))
```
1321. " What promise ? " (lpp_1943.1321)

```
(t / thing
      :ARG1-of (p2 / promise-01
            :ARG0 (i / i))
      :domain (a / amr-unknown))
```
1322. " You know - - a muzzle for my sheep ... (lpp_1943.1322)

```
(t / thing
      :ARG2-of (m2 / muzzle-01
            :ARG1 (s / sheep
                  :poss (i / i))))
```
1323. I am responsible for this flower ... " (lpp_1943.1323)

```
(r / responsible-03
      :ARG0 (i / i)
      :ARG1 (f / flower
            :mod (t / this)))
```
1324. I took my rough drafts of drawings out of my pocket . (lpp_1943.1324)

```
(t / take-01
      :ARG0 (i / i)
      :ARG1 (p2 / picture
            :ARG1-of (d3 / draft-01)
            :ARG1-of (r / rough-04)
            :ARG1-of (d4 / draw-01))
      :ARG2 (p / pocket
            :poss i))
```
1325. The little prince looked them over , and laughed as he said : " Your baobabs - - they look a little like cabbages . " (lpp_1943.1325)

```
(a / and
      :op1 (l / look-01
            :ARG0 (p / prince
                  :mod (l2 / little))
            :ARG1 (t / they))
      :op2 (l3 / laugh-01
            :ARG0 p
            :time (s / say-01
                  :ARG0 p
                  :ARG1 (l4 / look-02
                        :ARG0 (b / baobab
                              :poss (y / you))
                        :ARG1 (c / cabbage)
                        :degree (l5 / little)))))
```
1326. " Oh ! " (lpp_1943.1326)

```
(o / oh :mode expressive)
```
1327. I had been so proud of my baobabs ! (lpp_1943.1327)

```
(p / pride-01
      :ARG0 (i / i)
      :ARG1 (b / baobab
            :poss i)
      :degree (s / so))
```
1328. " Your fox - - his ears look a little like horns ; and they are too long . " (lpp_1943.1328)

```
(a2 / and
      :op1 (l4 / look-02
            :ARG0 (e / ear
                  :part-of (f / fox
                        :poss (y / you)))
            :ARG1 (h / horn)
            :degree (l / little))
      :op2 (l2 / long-03
            :ARG1 e
            :degree (t2 / too)))
```
1329. And he laughed again . (lpp_1943.1329)

```
(a / and
  :op2 (l / laugh-01
         :ARG0 (h / he)
         :mod (a2 / again)))
```
1330. " You are not fair , little prince , " (lpp_1943.1330)

```
(f / fair-01 :polarity -
      :ARG0 (p / prince
            :mod (l / little)))
```
1331. I said . (lpp_1943.1331)

```
(s / say-01
  :ARG0 (i / i))
```
1332. " I do n't know how to draw anything except boa constrictors from the outside and boa constrictors from the inside . " (lpp_1943.1332)

```
(k / know-01
      :ARG0 (i / i)
      :ARG1 (d / draw-01
            :ARG0 i
            :ARG1 (a2 / and
                  :op1 (o / outside
                        :part-of (b / boa
                              :mod (c / constrictor)))
                  :op2 (i2 / inside
                        :part-of b))))
```
1333. " Oh , that will be all right , " he said , " children understand . " (lpp_1943.1333)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (a / all-right
            :domain (t / that)
            :ARG1-of (c / cause-01
                  :ARG0 (u / understand-01
                        :ARG0 (c2 / child)))))
```
1334. So then I made a pencil sketch of a muzzle . (lpp_1943.1334)

```
(s2 / sketch-01
  :ARG0 (i / i)
  :ARG1 (m / muzzle)
  :instrument (p / pencil)
  :time (t / then))
```
1335. And as I gave it to him my heart was torn . (lpp_1943.1335)

```
(a / and
  :op2 (t / tear-01
         :ARG1 (h / heart
                 :part-of (i / i))
         :time (g / give-01
                 :ARG0 i
                 :ARG1 (i2 / it)
                 :ARG2 (h2 / he))))
```
1336. " You have plans that I do not know about , " (lpp_1943.1336)

```
(p2 / plan-01
  :ARG0 (y / you)
  :ARG1 (t / thing
          :ARG1-of (k / know-01
                     :ARG0 (i / i)
                     :polarity -)))
```
1337. I said . (lpp_1943.1337)

```
(s / say-01
  :ARG0 (i / i))
```
1338. But he did not answer me . (lpp_1943.1338)

```
(h2 / have-concession-91
  :ARG1 (a / answer-01
          :ARG0 (h / he)
          :ARG1 (i / i)
          :polarity -))
```
1339. He said to me , instead : " You know - - my descent to the earth ... (lpp_1943.1339)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (d / descend-01
            :ARG0 h
            :ARG1 (e / earth))
      :ARG2 (i / i)
      :ARG1-of (i2 / instead-of-91))
```
1340. Tomorrow will be its anniversary . " (lpp_1943.1340)

```
(a / anniversary
  :time (t / tomorrow)
  :poss (i / it))
```
1341. Then , after a silence , he went on : " I came down very near here . " (lpp_1943.1341)

```
(g / go-23
      :ARG0 (h / he)
      :ARG1 (c / come-01
            :ARG1 h
            :ARG4 (n / near-02
                  :ARG1 h
                  :ARG2 (h2 / here)
                  :degree (v / very))
            :direction (d / down))
      :time (t / then)
      :time (a / after
            :op1 (s / silent)))
```
1342. And he flushed . (lpp_1943.1342)

```
(a / and
  :op2 (f / flush-03
         :ARG1 (h / he)))
```
1343. And once again , without understanding why , I had a queer sense of sorrow . (lpp_1943.1343)

```
(a2 / and
      :op2 (s / sense-01
            :ARG0 (i / i)
            :ARG1 (s2 / sorrow-01
                  :ARG0 i)
            :mod (q / queer)
            :mod (a / again :frequency 1)
            :ARG1-of (c2 / cause-01
                  :ARG0 (a3 / amr-unknown
                        :ARG1-of (u2 / understand-01 :polarity -
                              :ARG0 i)))))
```
1344. One question , however , occurred to me : " Then it was not by chance that on the morning when I first met you - - a week ago - - you were strolling along like that , all alone , a thousand miles from any inhabited region ? (lpp_1943.1344)

```
(c / contrast-01
      :ARG2 (q / question-01
            :ARG0 (i / i)
            :ARG1 (s / stroll-01 :mode interrogative
                  :ARG0 y
                  :manner (a3 / alone
                        :degree (a4 / all)
                        :ARG1-of (r / resemble-01
                              :ARG2 (t2 / that)))
                  :direction (a6 / along)
                  :location (r3 / relative-position
                        :op1 (r2 / region
                              :ARG1-of (i3 / inhabit-01)
                              :mod (a5 / any))
                        :quant (d2 / distance-quantity :quant 1000
                              :unit (m3 / mile)))
                  :time (m / meet-03
                        :ARG0 i
                        :ARG1 (y / you)
                        :ord (o2 / ordinal-entity :value 1)
                        :time (b / before
                              :op1 (n / now)
                              :quant (t / temporal-quantity :quant 1
                                    :unit (w / week)))
                        :time (d / date-entity :dayperiod (m2 / morning)))
                  :ARG1-of (c2 / cause-01 :polarity -
                        :ARG0 (c3 / chance-02)))))
```
1345. You were on the your back to the place where you landed ? " (lpp_1943.1345)

```
(g / go-02 :mode interrogative
      :ARG1 (y2 / you)
      :ARG4 (p2 / place
            :location-of (l / land-01
                  :ARG0 (y / you)))
      :direction (b / back))
```
1346. The little prince flushed again . (lpp_1943.1346)

```
(f / flush-03
  :ARG1 (p / prince
          :mod (l / little))
  :mod (a / again))
```
1347. And I added , with some hesitancy : " Perhaps it was because of the anniversary ? " (lpp_1943.1347)

```
(a4 / and
  :op2 (a / add-01
         :ARG0 (i / i)
         :ARG1 (p2 / possible-01
                 :ARG1 (c / cause-01
                           :ARG0 (a3 / anniversary)
                           :ARG1 (i2 / it))
                 :mode interrogative)
         :manner (h / hesitate-01
                   :ARG0 i
                   :degree (s / some))))
```
1348. The little prince flushed once more . (lpp_1943.1348)

```
(f / flush-03
      :ARG1 (p / prince
            :mod (l / little))
      :mod (a / again :frequency 1))
```
1349. He never answered questions - - but when one flushes does that not mean " Yes " ? (lpp_1943.1349)

```
(c / contrast-01
      :ARG1 (a / answer-01 :polarity -
            :ARG0 (h / he)
            :ARG1 (q / question-01
                  :ARG2 h)
            :time (e / ever))
      :ARG2 (f / flush-03 :mode interrogative
            :ARG1 (o / one)
            :ARG1-of (m / mean-01
                  :ARG2 (y / yes))))
```
1350. " Ah , " (lpp_1943.1350)

```
(a / ah
  :mode expressive)
```
1351. I said to him , " I am a little frightened - - " (lpp_1943.1351)

```
(s / say-01
  :ARG0 (i / i)
  :ARG1 (f / frighten-01
          :ARG1 i
          :degree (l / little))
  :ARG2 (h / he))
```
1352. But he interrupted me . (lpp_1943.1352)

```
(c / contrast-01
  :ARG2 (i / interrupt-01
          :ARG0 (h / he)
          :ARG1 (i2 / i)))
```
1353. " Now you must work . (lpp_1943.1353)

```
(o / obligate-01
  :ARG1 (y / you)
  :ARG2 (w / work-01
          :ARG0 y)
  :time (n / now))
```
1354. You must return to your engine . (lpp_1943.1354)

```
(o2 / obligate-01
  :ARG1 (y / you)
  :ARG2 (r / return-01
          :ARG1 y
          :ARG4 (e / engine
                  :poss y)))
```
1355. I will be waiting for you here . (lpp_1943.1355)

```
(w / wait-01
      :ARG1 (i / i)
      :ARG2 (y / you)
      :location (h / here))
```
1356. Come back tomorrow evening ... " (lpp_1943.1356)

```
(c / come-01 :mode imperative
      :ARG1 (y / you)
      :direction (b / back)
      :time (d / date-entity
            :dayperiod (e2 / evening)
            :mod (t / tomorrow)))
```
1357. But I was not reassured . (lpp_1943.1357)

```
(h / have-concession-91
  :ARG1 (r / reassure-01
          :ARG1 (i / i)
          :polarity -))
```
1358. I remembered the fox . (lpp_1943.1358)

```
(r / remember-01
      :ARG0 (i / i)
      :ARG1 (f / fox))
```
1359. One runs the risk of weeping a little , if one lets himself be tamed ... (lpp_1943.1359)

```
(r2 / risk-01
      :ARG0 (o / one)
      :ARG2 (w / weep-01
            :ARG0 o
            :degree (l / little))
      :condition (l2 / let-01
            :ARG0 o
            :ARG1 (t / tame-01
                  :ARG1 o)))
```
1360. Chapter 26 . (lpp_1943.1360)

```
(c / chapter :mod 26)
```
1361. Beside the well there was the ruin of an old stone wall . (lpp_1943.1361)

```
(w / wall
      :mod (o / old)
      :consist-of (s / stone)
      :ARG1-of (r / ruin-01)
      :location (b / beside
            :op1 (w2 / well)))
```
1362. When I came back from my work , the next evening , I saw from some distance away my little price sitting on top of a wall , with his feet dangling . (lpp_1943.1362)

```
(s / see-01
      :ARG0 (i / i
            :location (r2 / relative-position
                  :quant (d2 / distant-02)))
      :ARG1 (s2 / sit-01
            :ARG1 (p2 / prince
                  :mod (l / little)
                  :poss i
                  :ARG0-of (d / dangle-01
                        :ARG1 (f / foot
                              :part-of p2)))
            :ARG2 (w / wall
                  :location (p / position
                        :op1 (o / on
                              :direction (t / top)))))
      :time (r / return-01
            :ARG1 i
            :ARG3 (w2 / work-01
                  :ARG0 i)
            :time (d3 / date-entity
                  :dayperiod (e / evening)
                  :mod (n / next))))
```
1363. And I heard him say : " Then you do n't remember . (lpp_1943.1363)

```
(a / and
      :op2 (h / hear-01
            :ARG0 (i / i)
            :ARG1 (s / say-01
                  :ARG0 (h2 / he)
                  :ARG1 (r / remember-01 :polarity -
                        :ARG0 (y / you)
                        :mod (t / then)))))
```
1364. This is not the exact spot . " (lpp_1943.1364)

```
(s2 / spot
      :domain (t / this)
      :mod (e2 / exact :polarity -))
```
1365. Another voice must have answered him , for he replied to it : " Yes , yes ! (lpp_1943.1365)

```
(o / obligate-01
      :ARG0 (v / voice
            :mod (a / another))
      :ARG1 h2
      :ARG2 (a2 / answer-01)
      :ARG0-of (c / cause-01
            :ARG1 (r / reply-01
                  :ARG0 (h2 / he)
                  :ARG2 (y / yes))))
```
1366. It is the right day , but this is not the place . " (lpp_1943.1366)

```
(c / contrast-01
      :ARG1 (d / day
            :ARG2-of (r / right-06))
      :ARG2 (p / place :polarity -
            :domain (t / this)))
```
1367. I continued my walk toward the wall . (lpp_1943.1367)

```
(c / continue-01
      :ARG0 (i / i)
      :ARG1 (w / walk-01
            :ARG0 i
            :direction (t / toward
                  :op1 (w2 / wall))))
```
1368. At no time did I see or hear anyone . (lpp_1943.1368)

```
(o / or
      :op1 (s / see-01 :polarity -
            :ARG0 (i / i)
            :ARG1 (a / anyone))
      :op2 (h / hear-01 :polarity -
            :ARG0 i
            :ARG1 a)
      :time (e / ever))
```
1369. The little prince , however , replied once again : " -- Exactly . (lpp_1943.1369)

```
(c / contrast-01
      :ARG2 (r / reply-01
            :ARG0 (p / prince
                  :mod (l / little))
            :ARG2 (e / exact)
            :mod (a / again)
            :time (o / once)))
```
1370. You will see where my track begins , in the sand . (lpp_1943.1370)

```
(s / see-01
      :ARG0 (y2 / you)
      :ARG1 (b2 / begin-01
            :ARG1 (t2 / track
                  :poss (i / i))
            :location (s3 / sand)))
```
1371. You have nothing to do but wait for me there . (lpp_1943.1371)

```
(h2 / have-03
      :ARG0 (y / you)
      :ARG1 (n / nothing
            :ARG1-of (d / do-02
                  :ARG0 y)
            :ARG1-of (c / contrast-01
                  :ARG2 (w2 / wait-01
                        :ARG1 y
                        :ARG2 (i / i)
                        :location (t2 / there)))))
```
1372. I shall be there tonight . " (lpp_1943.1372)

```
(t / there
      :location-of (i / i)
      :time (d / date-entity
            :dayperiod (n / night)
            :mod (t2 / today)))
```
1373. I was only twenty metres from the wall , and I still saw nothing . (lpp_1943.1373)

```
(a / and
      :op1 (b / be-located-at-91
            :ARG1 (i / i)
            :ARG2 (r / relative-position
                  :op1 (w / wall)
                  :quant (d / distance-quantity :quant 20
                        :unit (m / meter)
                        :mod (o / only))))
      :op2 (s / see-01
            :ARG0 i
            :ARG1 (n / nothing)
            :mod (s2 / still)))
```
1374. After a silence the little prince spoke again : " You have good poison ? (lpp_1943.1374)

```
(s / speak-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (h / have-03 :mode interrogative
            :ARG0 (y / you)
            :ARG1 (p2 / poison-01
                  :ARG1-of (g / good-02)))
      :mod (a / again)
      :time (a2 / after
            :op1 (s2 / silent)))
```
1375. You are sure that it will not make me suffer too long ? " (lpp_1943.1375)

```
(s2 / sure-02 :mode interrogative
      :ARG0 (y / you)
      :ARG1 (s / suffer-01 :polarity -
            :ARG0 (i / i)
            :ARG1 (i2 / it)
            :ARG1-of (l / long-03
                  :degree (t / too))))
```
1376. I stopped in my tracks , my heart torn asunder ; but still I did not understand . (lpp_1943.1376)

```
(c / contrast-01
      :ARG1 (a / and
            :op1 (s / stop-01
                  :ARG1 (i / i))
            :op2 (t / tear-01
                  :ARG1 (h / heart
                        :part-of i)
                  :mod (a2 / asunder)))
      :ARG2 (u / understand-01 :polarity -
            :ARG0 i
            :mod (s2 / still)))
```
1377. " Now go away , " said the little prince . (lpp_1943.1377)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little))
      :ARG1 (g / go-02 :mode imperative
            :ARG0 (y / you)
            :ARG1 (a / away)
            :time (n / now)))
```
1378. " I want to get down from the wall . " (lpp_1943.1378)

```
(w / want-01
      :ARG0 (i / i)
      :ARG1 (g / get-05
            :ARG0 i
            :ARG2 (r / relative-position
                  :op1 (w2 / wall)
                  :direction (d / down))))
```
1379. I dropped my eyes , then , to the foot of the wall - - and I leaped into the air . (lpp_1943.1379)

```
(a / and
      :op1 (d / drop-01
            :ARG0 (i / i)
            :ARG1 (e / eye
                  :part-of i)
            :ARG4 (f / foot
                  :part-of (w / wall))
            :time (t / then))
      :op2 (l / leap-03
            :ARG0 i
            :destination (a2 / air)))
```
1380. There before me , facing the little prince , was one of those yellow snakes that take just thirty seconds to bring your life to an end . (lpp_1943.1380)

```
(s3 / snake
      :ARG1-of (y / yellow-02)
      :ARG2-of (t / take-10
            :ARG0 (e / end-01
                  :ARG1 (l2 / life
                        :poss (y2 / you)))
            :ARG1 (t2 / temporal-quantity :quant 30
                  :unit (s2 / second)
                  :mod (j / just)))
      :location (b / before
            :op1 (i / i))
      :ARG0-of (f / face-01
            :ARG1 (p / prince
                  :mod (l / little))))
```
1381. Even as I was digging into my pocked to get out my revolver I made a running step back . (lpp_1943.1381)

```
(c / contrast-01
      :ARG1 (s / step-01
            :ARG1 i
            :ARG2 (b / back)
            :manner (r / run-02))
      :ARG2 (d / dig-01
            :ARG0 (i / i)
            :ARG2 (p / pocket
                  :poss i)
            :ARG3 r2
            :purpose (g / get-01
                  :ARG0 i
                  :ARG1 (r2 / revolver
                        :poss i))))
```
1382. But , at the noise I made , the snake let himself flow easily across the sand like the dying spray of a fountain , and , in no apparent hurry , disappeared , with a light metallic sound , among the stones . (lpp_1943.1382)

```
(c / contrast-01
      :ARG2 (a / and
            :op1 (l2 / let-01
                  :ARG0 (s3 / snake)
                  :ARG1 (f / flow-01
                        :ARG1 s3
                        :ARG1-of (e / easy-05)
                        :ARG1-of (r / resemble-01
                              :ARG2 (s5 / spray
                                    :ARG1-of (d2 / die-down-02)
                                    :poss (f2 / fountain)))
                        :path (a3 / across
                              :op1 (s4 / sand)))
                  :ARG1-of (c2 / cause-01
                        :ARG0 (n / noise
                              :ARG1-of (m2 / make-01
                                    :ARG0 (i / i)))))
            :op2 (d / disappear-01
                  :ARG1 s3
                  :ARG1-of (h / hurry-01 :polarity -
                        :mod (a2 / apparent))
                  :location (a4 / among
                        :op1 (s2 / stone))
                  :ARG0-of (s / sound-02
                        :ARG3 (m / metallic)
                        :ARG1-of (l / light-06)))))
```
1383. I reached the wall just in time to catch my little man in my arms ; his face was white as snow . (lpp_1943.1383)

```
(m / multi-sentence
      :snt1 (r / reach-01
            :ARG0 (i / i)
            :ARG1 (w2 / wall)
            :time (c / catch-01
                  :ARG0 i
                  :ARG1 (m2 / man
                        :mod (l / little)
                        :poss i)
                  :mod (j / just)
                  :location (a / arm
                        :part-of i)))
      :snt2 (f / face
            :ARG1-of (w / white-03
                  :degree (e / equal)
                  :compared-to (s / snow))
            :part-of m2))
```
1384. " What does this mean ? " (lpp_1943.1384)

```
(m / mean-01
      :ARG1 (t / this)
      :ARG2 (a / amr-unknown))
```
1385. I demanded . (lpp_1943.1385)

```
(d / demand-01
  :ARG0 (i / i))
```
1386. " Why are you talking with snakes ? " (lpp_1943.1386)

```
(t / talk-01
      :ARG0 (y / you)
      :ARG2 (s / snake)
      :purpose (a / amr-unknown))
```
1387. I had loosened the golden muffler that he always wore . (lpp_1943.1387)

```
(l / loosen-01
      :ARG0 (i / i)
      :ARG1 (m / muffler
            :consist-of (g / gold)
            :ARG1-of (w / wear-01
                  :ARG0 (h / he)
                  :time (a / always))))
```
1388. I had moistened his temples , and had given him some water to drink . (lpp_1943.1388)

```
(a / and
  :op1 (m / moisten-01
         :ARG0 (i / i)
         :ARG1 (t / temple
                 :poss (h / he)))
  :op2 (g / give-01
         :ARG0 i
         :ARG1 (w / water
                 :quant (s / some)
                 :purpose (d / drink-01))
         :ARG2 h))
```
1389. And now I did not dare ask him any more questions . (lpp_1943.1389)

```
(a / and
      :op2 (d / dare-01 :polarity -
            :ARG1 (i / i)
            :ARG2 (q2 / question-01
                  :ARG0 i
                  :ARG2 (h / he)
                  :mod (m / more
                        :mod (a3 / any))))
      :time (n / now))
```
1390. He looked at me very gravely , and put his arms around my neck . (lpp_1943.1390)

```
(a / and
      :op1 (l / look-01
            :ARG0 (h / he)
            :ARG1 (i / i)
            :manner (g / grave
                  :degree (v / very)))
      :op2 (p / put-01
            :ARG0 h
            :ARG1 (a2 / arm
                  :part-of h)
            :ARG2 (a3 / around
                  :op1 (n / neck
                        :part-of i))))
```
1391. I felt his heart beating like the heart of a dying bird , shot with someone 's rifle ... (lpp_1943.1391)

```
(f / feel-01
      :ARG0 (i / i)
      :ARG1 (h4 / heart
            :part-of (h2 / he)
            :ARG1-of (b / beat-01
                  :ARG1-of (r / resemble-01
                        :ARG2 (h3 / heart
                              :part-of (b2 / bird
                                    :ARG1-of (d / die-01)
                                    :ARG1-of (s / shoot-02
                                          :ARG2 (r2 / rifle
                                                :poss (s2 / someone)))))))))
```
1392. " I am glad that you have found what was the matter with your engine , " he said . (lpp_1943.1392)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (g / glad-02
            :ARG0 (f / find-01
                  :ARG0 (y / you)
                  :ARG1 (a / amr-unknown
                        :ARG0-of (c / cause-01
                              :ARG1 (h2 / have-03
                                    :ARG1 (p / problem
                                          :topic (e / engine
                                                :poss y))))))
            :ARG1 (i / i)))
```
1393. " Now you can go back home - - " (lpp_1943.1393)

```
(p / possible-01
      :ARG1 (g / go-02
            :ARG0 (y / you)
            :ARG4 (h / home)
            :direction (b / back))
      :time (n / now))
```
1394. " How do you know about that ? " (lpp_1943.1394)

```
(k / know-01
  :ARG0 (y / you)
  :ARG1 (t / that)
  :manner (a / amr-unknown))
```
1395. I was just coming to tell him that my work had been successful , beyond anything that I had dared to hope . (lpp_1943.1395)

```
(c / come-01
      :ARG1 (i / i)
      :purpose (t / tell-01
            :ARG0 i
            :ARG1 (s2 / succeed-01
                  :ARG1 (w / work-01
                        :ARG0 i)
                  :degree (b / beyond
                        :op1 (a / anything
                              :ARG1-of (h2 / hope-01
                                    :ARG0 i
                                    :ARG2-of (d / dare-01
                                          :ARG1 i)))))
            :ARG2 (h / he))
      :mod (j / just))
```
1396. He made no answer to my question , but he added : " I , too , am going back home today ... " (lpp_1943.1396)

```
(c / contrast-01
      :ARG1 (m / make-01
            :ARG0 h
            :ARG1 (a / answer-01 :polarity -
                  :ARG0 (h / he)
                  :ARG1 (q / question-01
                        :ARG0 (i / i))))
      :ARG2 (a2 / add-01
            :ARG0 h
            :ARG1 (r / return-01
                  :ARG1 h
                  :ARG4 (h2 / home)
                  :time (t / today)
                  :mod (t2 / too))))
```
1397. Then , sadly - - " It is much farther ... it is much more difficult ... " (lpp_1943.1397)

```
(s2 / say-01
      :ARG1 (a / and
            :op1 (f / far
                  :mod (m3 / much
                        :quant (m4 / more))
                  :domain (i / it))
            :op2 (d / difficult
                  :degree (m / more
                        :quant (m2 / much))
                  :domain i))
      :time (t / then)
      :manner (s / sad-02))
```
1398. I realised clearly that something extraordinary was happening . (lpp_1943.1398)

```
(r / realize-01
      :ARG0 (i / i)
      :ARG1 (e2 / event
            :mod (e / extraordinary))
      :ARG1-of (c / clear-06))
```
1399. I was holding him close in my arms as if he were a little child ; and yet it seemed to me that he was rushing headlong toward an abyss from which I could do nothing to restrain him ... (lpp_1943.1399)

```
(a / and
      :op1 (h / hold-01
            :ARG0 (i / i)
            :ARG1 (h2 / he)
            :ARG1-of (c / close-10)
            :location (a2 / arm
                  :part-of i)
            :ARG1-of (r / resemble-01
                  :ARG2 (c2 / child
                        :mod (l / little)
                        :domain h2)))
      :op2 (s / seem-01
            :ARG1 (r2 / rush-01
                  :ARG1 h2
                  :ARG2 (t / toward
                        :op1 (a3 / abyss
                              :ARG2-of (r3 / restrain-01 :polarity -
                                    :ARG0 i
                                    :ARG1 h2))
                        :mod (h3 / headlong)))
            :ARG2 i
            :mod (y / yet)))
```
1400. His look was very serious , like some one lost far away . (lpp_1943.1400)

```
(l / look-01
      :ARG0 (h / he)
      :ARG2-of (s / serious-01
            :degree (v / very))
      :ARG1-of (r / resemble-01
            :ARG2 (s2 / someone
                  :ARG1-of (l2 / lose-02
                        :direction (a / away
                              :mod (f / far))))))
```
1401. " I have your sheep . (lpp_1943.1401)

```
(h / have-03
      :ARG0 (i / i)
      :ARG1 (s / sheep
            :poss (y / you)))
```
1402. And I have the sheep 's box . (lpp_1943.1402)

```
(a / and
      :op2 (h / have-03
            :ARG0 (i / i)
            :ARG1 (b / box
                  :poss (s / sheep))))
```
1403. And I have the muzzle ... " (lpp_1943.1403)

```
(a / and
      :op2 (h / have-03
            :ARG0 (i / i)
            :ARG1 (m / muzzle)))
```
1404. And he gave me a sad smile . (lpp_1943.1404)

```
(a / and
      :op2 (g / give-01
            :ARG0 (h / he)
            :ARG1 (s / smile
                  :ARG1-of (s2 / sad-02))
            :ARG2 (i / i)))
```
1405. I waited a long time . (lpp_1943.1405)

```
(w / wait-01
      :ARG1 (i / i)
      :ARG1-of (l / long-03))
```
1406. I could see that he was reviving little by little . (lpp_1943.1406)

```
(p / possible-01
      :ARG1 (s / see-01
            :ARG0 (i / i)
            :ARG1 (r / revive-01
                  :ARG1 (h / he)
                  :manner (l / little-by-little))))
```
1407. " Dear little man , " (lpp_1943.1407)

```
(m2 / man
      :mod (l2 / little)
      :mod (d / dear))
```
1408. I said to him , " you are afraid ... " (lpp_1943.1408)

```
(s / say-01
  :ARG0 (i / i)
  :ARG1 (f / fear-01
          :ARG0 h)
  :ARG2 (h / he))
```
1409. He was afraid , there was no doubt about that . (lpp_1943.1409)

```
(f / fear-01
  :ARG0 (h / he)
  :mod (c / certain))
```
1410. But he laughed lightly . (lpp_1943.1410)

```
(c / contrast-01
      :ARG2 (l / laugh-01
            :ARG0 (h / he)
            :manner (l2 / light-06)))
```
1411. " I shall be much more afraid this evening ... " (lpp_1943.1411)

```
(f / fear-01
      :ARG0 (i / i)
      :degree (m / more
            :mod (m2 / much))
      :time (d / date-entity
            :dayperiod (e / evening)
            :mod (t / today)))
```
1412. Once again I felt myself frozen by the sense of something irreparable . (lpp_1943.1412)

```
(f / feel-01
      :ARG0 (i / i)
      :ARG1 (f2 / freeze-01
            :ARG0 (s / sense-01
                  :ARG0 i
                  :ARG1 (s2 / something
                        :ARG1-of (r / repair-01
                              :ARG1-of (p / possible-01 :polarity -))))
            :ARG1 i)
      :mod (a / again :frequency 1))
```
1413. And I knew that I could not bear the thought of never hearing that laughter any more . (lpp_1943.1413)

```
(a / and
      :op2 (k / know-01
            :ARG0 (i / i)
            :ARG1 (p / possible-01 :polarity -
                  :ARG1 (b / bear-01
                        :ARG1 (t / think-01
                              :ARG1 (h / hear-01 :polarity -
                                    :ARG1 (l / laugh-01)
                                    :time (e / ever)
                                    :mod (m / more
                                          :mod (a2 / any))))))))
```
1414. For me , it was like a spring of fresh water in the desert . (lpp_1943.1414)

```
(r / resemble-01
      :ARG1 (i / it)
      :ARG2 (s / spring
            :source-of (w / water
                  :ARG1-of (f / fresh-04))
            :location (d / desert))
      :beneficiary (i2 / i))
```
1415. " Little man , " (lpp_1943.1415)

```
(m / man
  :mod (l / little))
```
1416. I said , " I want to hear you laugh again . " (lpp_1943.1416)

```
(s / say-01
  :ARG0 i
  :ARG1 (w / want-01
          :ARG0 (i / i)
          :ARG1 (h / hear-01
                  :ARG0 i
                  :ARG1 (l / laugh-01
                          :ARG0 (y / you)
                          :mod (a / again)))))
```
1417. But he said to me : " Tonight , it will be a year ... my star , then , can be found right above the place where I came to the Earth , a year ago ... " (lpp_1943.1417)

```
(c / contrast-01
      :ARG2 (s / say-01
            :ARG0 (h / he)
            :ARG1 (p / possible-01
                  :ARG1 (f / find-01
                        :ARG1 (s2 / star
                              :poss h)
                        :location (a / above
                              :op1 (p2 / place
                                    :location (e / earth)
                                    :ARG4-of (c2 / come-01
                                          :time (b / before
                                                :op1 (n / now)
                                                :quant (t3 / temporal-quantity :quant 1
                                                      :unit (y2 / year)))))
                              :mod (r / right)))
                  :time (d / date-entity :dayperiod (n2 / night) :mod (t / today))
                  :duration (y / year)
                  :mod (t2 / then))
            :ARG2 (i / i)))
```
1418. " Little man , " (lpp_1943.1418)

```
(m / man
  :mod (l / little))
```
1419. I said , " tell me that it is only a bad dream - - this affair of the snake , and the meeting - place , and the star ... " (lpp_1943.1419)

```
(s / say-01
      :ARG0 (i / i)
      :ARG1 (t / tell-01 :mode imperative
            :ARG0 (y / you)
            :ARG1 (d / dream-01
                  :ARG0 i
                  :ARG1 (a / and
                        :op1 (a2 / affair-02
                              :ARG1 (s2 / snake)
                              :ARG2 (t2 / this))
                        :op2 (m / meet-01
                              :location (p / place))
                        :op3 (s3 / star))
                  :ARG1-of (b / bad-07)
                  :mod (o / only))
            :ARG2 i))
```
1420. But he did not answer my plea . (lpp_1943.1420)

```
(c / contrast-01
  :ARG2 (a / answer-01
          :ARG0 (h / he)
          :ARG1 (p / plea
                  :poss (i / i))
          :polarity -))
```
1421. He said to me , instead : " The thing that is important is the thing that is not seen ... " (lpp_1943.1421)

```
(s3 / say-01
      :ARG0 (h / he)
      :ARG1 (i2 / important
            :domain (t / thing
                  :ARG1-of (s2 / see-01 :polarity -)))
      :ARG2 (i3 / i)
      :ARG1-of (i / instead-of-91))
```
1422. " Yes , I know ... " (lpp_1943.1422)

```
(k / know-01
  :ARG0 (i / i))
```
1423. " It is just as it is with the flower . (lpp_1943.1423)

```
(r / resemble-01
  :ARG1 (i / it)
  :ARG2 (f / flower)
  :mod (j / just))
```
1424. If you love a flower that lives on a star , it is sweet to look at the sky at night . (lpp_1943.1424)

```
(l / look-01
      :ARG1 (s2 / sky
            :time (d / date-entity :dayperiod (n / night)))
      :ARG1-of (s / sweet-04)
      :condition (l2 / love-01
            :ARG0 (y / you)
            :ARG1 (f / flower
                  :ARG0-of (l3 / live-01
                        :location (s3 / star)))))
```
1425. All the stars are a - bloom with flowers ... " (lpp_1943.1425)

```
(b / bloom-01
      :ARG0 (f / flower)
      :location (s / star
            :mod (a / all)))
```
1426. " Yes , I know ... " (lpp_1943.1426)

```
(k / know-01
  :ARG0 (i / i))
```
1427. " It is just as it is with the water . (lpp_1943.1427)

```
(r / resemble-01
  :ARG1 (i / it)
  :ARG2 (w / water)
  :mod (j / just))
```
1428. Because of the pulley , and the rope , what you gave me to drink was like music . (lpp_1943.1428)

```
(c / cause-01
      :ARG0 (a / and
            :op1 (p / pulley)
            :op2 (r / rope))
      :ARG1 (r2 / resemble-01
            :ARG1 (t / thing
                  :ARG1-of (g / give-01
                        :ARG0 (y / you)
                        :ARG2 (i / i)
                        :purpose (d / drink-01
                              :ARG0 i)))
            :ARG2 (m / music)))
```
1429. You remember - - how good it was . " (lpp_1943.1429)

```
(r / remember-01
      :ARG0 (y / you)
      :ARG1 (g / good-02
            :ARG1 (i / it)
            :degree (s / so)))
```
1430. " Yes , I know ... " (lpp_1943.1430)

```
(k / know-01
  :ARG0 (i / i))
```
1431. " And at night you will look up at the stars . (lpp_1943.1431)

```
(a / and
      :op2 (l / look-01
            :ARG0 (y / you)
            :ARG1 (s / star)
            :direction (u / up)
            :time (d / date-entity :dayperiod (n / night))))
```
1432. Where I live everything is so small that I can not show you where my star is to be found . (lpp_1943.1432)

```
(p / possible-01
  :polarity -
  :ARG1 (s / show-01
            :ARG0 (i / i)
            :ARG1 (l / location
                    :location-of (f / find-01
                                   :ARG1 (s2 / star
                                           :poss i)))
            :ARG2 (y2 / you))
  :ARG1-of (c / cause-01
             :ARG0 (e / everything
                     :mod (s3 / small
                            :degree (s4 / so))
                     :location (l2 / live-01
                                 :ARG0 i))))
```
1433. It is better , like that . (lpp_1943.1433)

```
(r / resemble-01
      :ARG1 (i / it
            :ARG1-of (g / good-02
                  :degree (m / more)))
      :ARG2 (t / that))
```
1434. My star will just be one of the stars , for you . (lpp_1943.1434)

```
(s / star :quant 1
      :beneficiary (y / you)
      :poss (i / i)
      :ARG1-of (i2 / include-91
            :ARG2 (s2 / star)
            :mod (j / just)))
```
1435. And so you will love to watch all the stars in the heavens ... they will all be your friends . (lpp_1943.1435)

```
(a / and
      :op2 (l / love-01
            :ARG0 (y / you)
            :ARG1 (w / watch-01
                  :ARG0 y
                  :ARG1 (s / star
                        :location (h / heaven)
                        :mod (a2 / all)
                        :ARG0-of (h2 / have-rel-role-91
                              :ARG1 y
                              :ARG2 (f / friend))))))
```
1436. And , besides , I am going to make you a present ... " (lpp_1943.1436)

```
(a / and
  :op1 (m / make-01
         :ARG0 (i / i)
         :ARG1 (p / present)
         :ARG3 (y / you)))
```
1437. He laughed again . (lpp_1943.1437)

```
(l / laugh-01
  :ARG0 (h / he)
  :mod (a / again))
```
1438. " Ah , little prince , dear little prince ! (lpp_1943.1438)

```
(a / and :mode expressive
      :op2 (p2 / prince
            :mod (l2 / little)
            :mod (d / dear)))
```
1439. I love to hear that laughter ! " (lpp_1943.1439)

```
(l / love-01
      :ARG0 (i / i)
      :ARG1 (h / hear-01
            :ARG0 i
            :ARG1 (l2 / laugh-01
                  :mod (t / that))))
```
1440. " That is my present . (lpp_1943.1440)

```
(p / present-01
      :ARG0 (i / i)
      :ARG1 (t / that))
```
1441. Just that . (lpp_1943.1441)

```
(t / that
  :mod (j / just))
```
1442. It will be as it was when we drank the water ... " (lpp_1943.1442)

```
(r / resemble-01
      :ARG1 (i / it)
      :ARG2 (t / time
            :time-of (d / drink-01
                  :ARG0 (w / we)
                  :ARG1 (w2 / water))))
```
1443. " What are you trying to say ? " (lpp_1943.1443)

```
(t / try-01
  :ARG0 (y / you)
  :ARG1 (s / say-01
          :ARG0 y
          :ARG1 (a / amr-unknown)))
```
1444. " All men have the stars , " he answered , " but they are not the same things for different people . (lpp_1943.1444)

```
(a / answer-01
      :ARG0 (h / he)
      :ARG2 (c / contrast-01
            :ARG1 (h2 / have-03
                  :ARG0 (m / man
                        :mod (a2 / all))
                  :ARG1 (s / star))
            :ARG2 (t / thing
                  :ARG1-of (s2 / same-01 :polarity -
                        :ARG2 s
                        :ARG3 (p / person
                              :ARG1-of (d2 / differ-02))))))
```
1445. For some , who are travelers , the stars are guides . (lpp_1943.1445)

```
(g / guide-01
  :ARG0 (s / star)
  :ARG1 (s2 / some
          :ARG0-of (t / travel-01)))
```
1446. For others they are no more than little lights in the sky . (lpp_1943.1446)

```
(o2 / opine-01
      :ARG0 (p / person
            :mod (o / other))
      :ARG1 (l / light
            :mod (l2 / little)
            :location (s / sky)
            :mod (o3 / only)
            :domain (t / they)))
```
1447. For others , who are scholars , they are problems . (lpp_1943.1447)

```
(o / opine-01
      :ARG0 (s / scholar)
      :ARG1 (p / problem
            :domain (t / they)))
```
1448. For my businessman they were wealth . (lpp_1943.1448)

```
(o / opine-01
      :ARG0 (b / businessman
            :poss (i / i))
      :ARG1 (w / wealth
            :domain (t / they)))
```
1449. But all these stars are silent . (lpp_1943.1449)

```
(c / contrast-01
      :ARG2 (s2 / silent
            :domain (s / star
                  :mod (t / this
                        :mod (a / all)))))
```
1450. You - - you alone - - will have the stars as no one else has them - - " (lpp_1943.1450)

```
(h / have-03
      :ARG0 (y / you
            :mod (a / alone))
      :ARG1 (s / star)
      :ARG1-of (r / resemble-01 :polarity -
            :ARG2 (h2 / have-03
                  :ARG0 (a2 / anyone
                        :mod (e / else))
                  :ARG1 s)))
```
1451. " What are you trying to say ? " (lpp_1943.1451)

```
(t / try-01
      :ARG0 (y / you)
      :ARG1 (s / say-01
            :ARG0 y
            :ARG1 (a / amr-unknown)))
```
1452. " In one of the stars I shall be living . (lpp_1943.1452)

```
(l / live-01
      :ARG0 (i / i)
      :location (s / star :quant 1
            :ARG1-of (i2 / include-91
                  :ARG2 (s2 / star))))
```
1453. In one of them I shall be laughing . (lpp_1943.1453)

```
(l / laugh-01
      :ARG0 (i / i)
      :location (s / star :quant 1
            :ARG1-of (i2 / include-91
                  :ARG2 (t / they))))
```
1454. And so it will be as if all the stars were laughing , when you look at the sky at night ... you - - only you - - will have stars that can laugh ! " (lpp_1943.1454)

```
(a / and
      :op2 (r / resemble-01
            :ARG1 (i2 / it)
            :ARG2 (l2 / laugh-01
                  :ARG0 (s / star
                        :mod (a3 / all)))
            :time (l3 / look-01
                  :ARG0 (y / you
                        :mod (o2 / only))
                  :ARG1 (s2 / sky)
                  :time (d / date-entity
                        :dayperiod (n / night)
                        :time-of (h / have-03
                              :ARG0 y
                              :ARG1 (s3 / star
                                    :ARG0-of (l / laugh-01
                                          :ARG1-of (p / possible-01))))))))
```
1455. And he laughed again . (lpp_1943.1455)

```
(a / and
      :op2 (l / laugh-01
            :ARG0 (h / he)
            :mod (a2 / again)))
```
1456. " And when your sorrow is comforted ( time soothes all sorrows ) you will be content that you have known me . (lpp_1943.1456)

```
(a / and
      :op2 (c / content-01
            :ARG1 (y / you)
            :ARG2 (k / know-02
                  :ARG0 y
                  :ARG1 (i / i))
            :time (c2 / comfort-01
                  :ARG1 (s / sorrow-01
                        :ARG0 y
                        :ARG1-of (s2 / soothe-01
                              :ARG0 (t / time))
                        :mod (a2 / all)))))
```
1457. You will always be my friend . (lpp_1943.1457)

```
(h / have-rel-role-91
      :ARG0 (y / you)
      :ARG1 (i / i)
      :ARG2 (f / friend)
      :time (a / always))
```
1458. You will want to laugh with me . (lpp_1943.1458)

```
(w / want-01
      :ARG0 (y / you)
      :ARG1 (l / laugh-01
            :ARG0 y
            :accompanier (i / i)))
```
1459. And you will sometimes open your window , so , for that pleasure ... and your friends will be properly astonished to see you laughing as you look up at the sky ! (lpp_1943.1459)

```
(a / and
      :op1 (o / open-01
            :ARG0 (y / you)
            :ARG1 (w / window
                  :poss y)
            :time (s / sometimes)
            :purpose (p / pleasure
                  :mod (t / that)))
      :op2 (a2 / astonish-01
            :ARG0 (s2 / see-01
                  :ARG0 p3
                  :ARG1 (l / laugh-01
                        :ARG0 (y2 / you)
                        :time (l2 / look-01
                              :ARG1 (s3 / sky)
                              :direction (u / up))))
            :ARG1 (p3 / person
                  :ARG0-of (h / have-rel-role-91
                        :ARG1 y
                        :ARG2 (f / friend)))
            :manner (p2 / proper)))
```
1460. Then you will say to them , ' Yes , the stars always make me laugh ! ' And they will think you are crazy . (lpp_1943.1460)

```
(a / and
      :op1 (s / say-01
            :ARG0 (y / you)
            :ARG1 (a3 / and
                  :op1 (y2 / yes)
                  :op2 (m / make-02
                        :ARG0 (s3 / star)
                        :ARG1 (l2 / laugh-01
                              :ARG0 (i / i))
                        :time (a2 / always)))
            :ARG2 (t2 / they)
            :time (t / then))
      :op2 (t3 / think-01
            :ARG0 t2
            :ARG1 (c / crazy-03
                  :ARG1 y)))
```
1461. It will be a very shabby trick that I shall have played on you ... " (lpp_1943.1461)

```
(t3 / trick-01
      :ARG0 (i / i)
      :ARG1 (y / you)
      :mod (s2 / shabby
            :degree (v2 / very)))
```
1462. And he laughed again . (lpp_1943.1462)

```
(a / and
      :op2 (l / laugh-01
            :ARG0 (h / he)
            :mod (a2 / again)))
```
1463. " It will be as if , in place of the stars , I had given you a great number of little bells that knew how to laugh ... " (lpp_1943.1463)

```
(r / resemble-01
      :ARG1 (g / give-01
            :ARG0 (i / i)
            :ARG1 (b2 / bell
                  :mod (l3 / little)
                  :quant (g2 / great)
                  :ARG0-of (k / know-01
                        :ARG1 (l2 / laugh-01)))
            :ARG2 (y / you)
            :ARG1-of (i2 / instead-of-91
                  :ARG2 (g3 / give-01
                        :ARG0 i
                        :ARG1 (s2 / star)
                        :ARG2 y))))
```
1464. And he laughed again . (lpp_1943.1464)

```
(a / and
      :op2 (l / laugh-01
            :ARG0 (h / he)
            :mod (a2 / again)))
```
1465. Then he quickly became serious : " Tonight - - you know ... do not come , " said the little prince . (lpp_1943.1465)

```
(s / say-01
      :ARG0 (p / prince
            :mod (l / little)
            :ARG1-of (b / become-01
                  :ARG2 (s2 / serious-01
                        :ARG1 p)
                  :ARG1-of (q / quick-02)
                  :time (t / then)))
      :ARG1 (c / come-01 :mode imperative :polarity -
            :ARG1 (y / you)
            :time (d / date-entity :dayperiod (n / night) :mod (t2 / today))))
```
1466. " I shall not leave you , " (lpp_1943.1466)

```
(l / leave-15 :polarity -
      :ARG0 (i / i)
      :ARG1 (y / you))
```
1467. I said . (lpp_1943.1467)

```
(s / say-01
  :ARG0 (i / i))
```
1468. " I shall look as if I were suffering . (lpp_1943.1468)

```
(l / look-02
      :ARG0 (i / i)
      :ARG1 (h / have-manner-91
            :ARG2 (s2 / suffer-01)))
```
1469. I shall look a little as if I were dying . (lpp_1943.1469)

```
(l / look-02
      :ARG0 (i / i)
      :ARG1 (h / have-manner-91
            :ARG2 (d2 / die-01))
      :degree (l3 / little))
```
1470. It is like that . (lpp_1943.1470)

```
(r / resemble-01
  :ARG1 (i / it)
  :ARG2 (t / that))
```
1471. Do not come to see that . (lpp_1943.1471)

```
(c / come-01 :polarity - :mode imperative
      :ARG1 (y / you)
      :purpose (s / see-01
            :ARG0 y
            :ARG1 (t / that)))
```
1472. It is not worth the trouble ... " (lpp_1943.1472)

```
(w / worth-02 :polarity -
      :ARG1 (i / it)
      :ARG2 (t / trouble-01))
```
1473. " I shall not leave you . " (lpp_1943.1473)

```
(l / leave-15 :polarity -
      :ARG0 (i / i)
      :ARG1 (y / you))
```
1474. But he was worried . (lpp_1943.1474)

```
(c / contrast-01
      :ARG2 (w2 / worry-01
            :ARG1 (h / he)))
```
1475. " I tell you - - it is also because of the snake . (lpp_1943.1475)

```
(t / tell-01
      :ARG0 (i / i)
      :ARG1 (c / cause-01
            :ARG0 (s / snake)
            :mod (a / also))
      :ARG2 (y / you))
```
1476. He must not bite you . (lpp_1943.1476)

```
(o2 / obligate-01
      :ARG1 (b2 / bite-01 :polarity -
            :ARG0 (h2 / he)
            :ARG1 (y2 / you)))
```
1477. Snakes - - they are malicious creatures . (lpp_1943.1477)

```
(s / snake
      :mod (c / creature
            :mod (m / malicious)))
```
1478. This one might bite you just for fun ... " (lpp_1943.1478)

```
(p / possible-01
      :ARG1 (b / bite-01
            :ARG0 (o / one
                  :mod (t / this))
            :ARG1 (y / you)
            :purpose (f / fun-01
                  :mod (j / just))))
```
1479. " I shall not leave you . " (lpp_1943.1479)

```
(l / leave-15 :polarity -
      :ARG0 (i / i)
      :ARG1 (y / you))
```
1480. But a thought came to reassure him : " It is true that they have no more poison for a second bite . " (lpp_1943.1480)

```
(c / contrast-01
      :ARG2 (c2 / come-01
            :ARG1 (t / think-01
                  :ARG1 (t3 / true-01
                        :ARG1 (h2 / have-03 :polarity -
                              :ARG0 (t2 / they)
                              :ARG1 (p / poison
                                    :purpose (b / bite-01
                                          :ord (o / ordinal-entity :value 2))
                                    :quant (m / more)))
                        :purpose (r / reassure-01
                              :ARG1 (h / he))))))
```
1481. That night I did not see him set out on his way . (lpp_1943.1481)

```
(s / see-01 :polarity -
      :ARG0 (i / i)
      :ARG1 (s2 / set-out-07
            :ARG0 (h / he)
            :ARG1 (w / way
                  :poss h))
      :time (d / date-entity
            :dayperiod (n / night)
            :mod (t / that)))
```
1482. He got away from me without making a sound . (lpp_1943.1482)

```
(g / get-away-08
      :ARG0 (h / he)
      :source (i / i)
      :manner (s2 / sound-02 :polarity -
            :ARG1 h))
```
1483. When I succeeded in catching up with him he was walking along with a quick and resolute step . (lpp_1943.1483)

```
(s / succeed-01
      :ARG0 (i / i)
      :ARG1 (c / catch-up-04
            :ARG1 i
            :ARG2 (h / he))
      :time (w / walk-01
            :ARG0 h
            :ARG1-of (q / quick-02)
            :manner (r2 / resolute)))
```
1484. He said to me merely : " Ah ! (lpp_1943.1484)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (a / ah :mode expressive)
      :ARG2 (i / i)
      :manner (m / mere))
```
1485. You are there ... " (lpp_1943.1485)

```
(y / you
  :location (t / there))
```
1486. And he took me by the hand . (lpp_1943.1486)

```
(a / and
      :op2 (t / take-01
            :ARG0 (h / he)
            :ARG1 (i / i)
            :manner (h2 / hand)))
```
1487. But he was still worrying . (lpp_1943.1487)

```
(c / contrast-01
      :ARG2 (w / worry-01
            :ARG1 (h / he)
            :time (s2 / still)))
```
1488. " It was wrong of you to come . (lpp_1943.1488)

```
(c / come-01
      :ARG1 (y / you)
      :ARG1-of (w / wrong-02))
```
1489. You will suffer . (lpp_1943.1489)

```
(s / suffer-01
  :ARG0 (y / you))
```
1490. I shall look as if I were dead ; and that will not be true ... " (lpp_1943.1490)

```
(a / and
      :op1 (r / resemble-01
            :ARG1 (i / i)
            :ARG2 (i2 / i
                  :ARG1-of (d2 / die-01)))
      :op2 (t / true-01 :polarity -
            :ARG1 r))
```
1491. I said nothing . (lpp_1943.1491)

```
(s / say-01
  :ARG0 (i / i)
  :ARG1 (n / nothing))
```
1492. " You understand ... it is too far . (lpp_1943.1492)

```
(u / understand-01
      :ARG0 (y / you)
      :ARG1 (f / far
            :degree (t / too)))
```
1493. I can not carry this body with me . (lpp_1943.1493)

```
(p / possible-01 :polarity -
      :ARG1 (c / carry-01
            :ARG0 (i / i)
            :ARG1 (b / body
                  :mod (t / this))
            :ARG3 (i2 / i)))
```
1494. It is too heavy . " (lpp_1943.1494)

```
(h2 / heavy
      :degree (t2 / too))
```
1495. I said nothing . (lpp_1943.1495)

```
(s / say-01
  :ARG0 (i / i)
  :ARG1 (n / nothing))
```
1496. " But it will be like an old abandoned shell . (lpp_1943.1496)

```
(c / contrast-01
      :ARG2 (r / resemble-01
            :ARG1 (i / it)
            :ARG2 (s / shell
                  :ARG1-of (a / abandon-01)
                  :mod (o / old))))
```
1497. There is nothing sad about old shells ... " (lpp_1943.1497)

```
(s / sad-02 :polarity -
      :ARG0 (s2 / shell
            :mod (o / old)))
```
1498. I said nothing . (lpp_1943.1498)

```
(s / say-01
  :ARG0 (i / i)
  :ARG1 (n / nothing))
```
1499. He was a little discouraged . (lpp_1943.1499)

```
(d / discourage-01
  :ARG1 (h / he)
  :degree (l / little))
```
1500. But he made one more effort : " You know , it will be very nice . (lpp_1943.1500)

```
(c / contrast-01
      :ARG2 (e / effort-01
            :ARG0 (h / he)
            :ARG1 (n / nice-01
                  :ARG1 (i / it)
                  :degree (v / very))
            :mod (m2 / more :quant 1)))
```
1501. I , too , shall look at the stars . (lpp_1943.1501)

```
(l / look-01
  :ARG0 (i / i
          :mod (t / too))
  :ARG1 (s / star))
```
1502. All the stars will be wells with a rusty pulley . (lpp_1943.1502)

```
(s / star
      :domain (w / well
            :ARG0-of (h / have-03
                  :ARG1 (p / pulley
                        :mod (r / rust))))
      :mod (a / all))
```
1503. All the stars will pour out fresh water for me to drink ... " (lpp_1943.1503)

```
(p / pour-01
      :ARG0 (s / star
            :mod (a / all))
      :ARG1 (w / water
            :ARG1-of (f / fresh-04))
      :purpose (d / drink-01
            :ARG0 (i / i)
            :ARG1 w)
      :direction (o / out))
```
1504. I said nothing . (lpp_1943.1504)

```
(s / say-01
  :ARG0 (i / i)
  :ARG1 (n / nothing))
```
1505. " That will be so amusing ! (lpp_1943.1505)

```
(a / amuse-01
      :ARG0 (t / that)
      :degree (s / so))
```
1506. You will have five hundred million little bells , and I shall have five hundred million springs of fresh water ... " (lpp_1943.1506)

```
(a / and
      :op1 (h / have-03
            :ARG0 (y / you)
            :ARG1 (b / bell :quant 500000000
                  :mod (l / little)))
      :op2 (h2 / have-03
            :ARG0 (i / i)
            :ARG1 (s / spring :quant 500000000
                  :source-of (w / water
                        :ARG1-of (f / fresh-04)))))
```
1507. And he too said nothing more , because he was crying ... (lpp_1943.1507)

```
(a / and
      :op2 (s / say-01
            :ARG0 (h / he
                  :degree (t / too))
            :ARG1 (n / nothing
                  :mod (m / more))
            :ARG1-of (c / cause-01
                  :ARG0 (c2 / cry-02
                        :ARG0 h))))
```
1508. " Here it is . (lpp_1943.1508)

```
(i / it
  :location (h / here))
```
1509. Let me go on by myself . " (lpp_1943.1509)

```
(a / allow-01
      :ARG0 (y / you)
      :ARG1 (g / go-on-15
            :ARG1 (i / i)
            :mod (b / by-oneself)))
```
1510. And he sat down , because he was afraid . (lpp_1943.1510)

```
(a / and
      :op2 (s / sit-down-02
            :ARG1 (h / he)
            :ARG1-of (c / cause-01
                  :ARG0 (f / fear-01
                        :ARG0 h))))
```
1511. Then he said , again : " You know - - my flower ... (lpp_1943.1511)

```
(s / say-01
      :ARG0 (h / he)
      :ARG1 (f / flower
            :poss h)
      :time (t / then)
      :mod (a / again))
```
1512. I am responsible for her . (lpp_1943.1512)

```
(r / responsible-03
      :ARG0 (i / i)
      :ARG2 (s / she))
```
1513. And she is so weak ! (lpp_1943.1513)

```
(a / and
      :op2 (w / weak-02
            :ARG1 (s / she)
            :degree (s2 / so)))
```
1514. She is so naïve ! (lpp_1943.1514)

```
(n / naive
      :degree (s2 / so)
      :domain (s / she))
```
1515. She has four thorns , of no use at all , to protect herself against all the world ... " (lpp_1943.1515)

```
(h / have-03
      :ARG0 (s / she)
      :ARG1 (t / thorn :quant 4
            :ARG1-of (u / use-01 :polarity -))
      :purpose (p / protect-01
            :ARG0 t
            :ARG1 s
            :ARG2 (w / world
                  :mod (a / all))))
```
1516. I too sat down , because I was not able to stand up any longer . (lpp_1943.1516)

```
(s / sit-down-02
      :ARG1 (i / i
            :degree (t / too))
      :ARG1-of (c / cause-01
            :ARG0 (p / possible-01 :polarity -
                  :ARG1 (s2 / stand-up-07
                        :ARG1 i
                        :ARG1-of (l / long-03
                              :mod (a / any))))))
```
1517. " There now - - that is all ... " (lpp_1943.1517)

```
(t / that
  :mod (a / all)
  :time (n / now))
```
1518. He still hesitated a little ; then he got up . (lpp_1943.1518)

```
(m / multi-sentence
      :snt1 (h / hesitate-01
            :ARG0 (h2 / he)
            :mod (s / still)
            :degree (l / little))
      :snt2 (g / get-05
            :ARG1 h2
            :ARG2 (u / up)
            :time (t / then)))
```
1519. He took one step . (lpp_1943.1519)

```
(s / step-01
      :ARG1 (h / he))
```
1520. I could not move . (lpp_1943.1520)

```
(p / possible-01
  :ARG1 (m / move-01
            :ARG1 (i / i))
  :polarity -)
```
1521. There was nothing but a flash of yellow close to his ankle . (lpp_1943.1521)

```
(c / contrast-01
      :ARG1 (n / nothing)
      :ARG2 (f / flash
            :ARG1-of (y / yellow-02)
            :ARG1-of (c2 / close-10
                  :ARG2 (a / ankle
                        :part-of (h / he)))))
```
1522. He remained motionless for an instant . (lpp_1943.1522)

```
(r / remain-01
      :ARG1 (h / he)
      :duration (i / instant)
      :manner (m / move-01 :polarity -))
```
1523. He did not cry out . (lpp_1943.1523)

```
(c / cry-out-03
  :ARG0 (h / he)
  :polarity -)
```
1524. He fell as gently as a tree falls . (lpp_1943.1524)

```
(f / fall-01
      :ARG1 (h / he)
      :manner (g / gentle
            :degree (e / equal)
            :compared-to (f2 / fall-01
                  :ARG1 (t / tree))))
```
1525. There was not even any sound , because of the sand . (lpp_1943.1525)

```
(s / sound-02 :polarity -
      :mod (a / any
            :mod (e / even))
      :ARG1-of (c / cause-01
            :ARG0 (s2 / sand)))
```
1526. Chapter 27 . (lpp_1943.1526)

```
(c / chapter :mod 27)
```
1527. And now six years have already gone by ... (lpp_1943.1527)

```
(a / and
      :op2 (g / go-on-15
            :ARG1 (t / temporal-quantity :quant 6
                  :unit (y / year))
            :time (a2 / already))
      :time (n / now))
```
1528. I have never yet told this story . (lpp_1943.1528)

```
(t / tell-01 :polarity -
      :ARG0 (i / i)
      :ARG1 (s / story
            :mod (t2 / this))
      :time (e / ever)
      :time (y / yet))
```
1529. The companions who met me on my return were well content to see me alive . (lpp_1943.1529)

```
(c / content-01
      :ARG0 (s / see-01
            :ARG0 c2
            :ARG1 (l / live-01
                  :ARG0 (i / i)))
      :ARG1 (c2 / companion
            :ARG0-of (m / meet-03
                  :ARG1 i
                  :time (r / return-01
                        :ARG1 i)))
      :mod (w / well))
```
1530. I was sad , but I told them : " I am tired . " (lpp_1943.1530)

```
(c / contrast-01
      :ARG1 (s / sad-02
            :ARG1 i)
      :ARG2 (t / tell-01
            :ARG0 (i / i)
            :ARG1 (t3 / tire-01
                  :ARG1 i)
            :ARG2 (t2 / they)))
```
1531. Now my sorrow is comforted a little . (lpp_1943.1531)

```
(c / comfort-01
      :ARG1 (s / sorrow-01
            :ARG0 (i / i))
      :time (n / now)
      :degree (l / little))
```
1532. That is to say - - not entirely . (lpp_1943.1532)

```
(s / say-01
  :ARG1 (e / entire
          :polarity -))
```
1533. But I know that he did go back to his planet , because I did not find his body at daybreak . (lpp_1943.1533)

```
(c / contrast-01
  :ARG2 (k / know-01
          :ARG0 (i / i)
          :ARG1 (g / go-back-19
                  :ARG1 (h / he)
                  :ARG2 (p / planet
                          :poss h))
          :ARG1-of (c2 / cause-01
                     :ARG0 (f / find-01
                             :ARG0 i
                             :ARG1 (b / body
                                     :poss h)
                             :polarity -
                             :time (d / daybreak)))))
```
1534. It was not such a heavy body ... and at night I love to listen to the stars . (lpp_1943.1534)

```
(a / and
      :op1 (b / body
            :mod (h / heavy :polarity -
                  :mod (s / such)))
      :op2 (l / love-01
            :ARG0 (i / i)
            :ARG1 (l2 / listen-01
                  :ARG0 i
                  :ARG1 (s2 / star)
                  :time (d / date-entity :dayperiod (n / night)))))
```
1535. It is like five hundred million little bells ... (lpp_1943.1535)

```
(r / resemble-01
      :ARG1 (i / it)
      :ARG2 (b / bell :quant 500000000
            :mod (l / little)))
```
1536. But there is one extraordinary thing ... when I drew the muzzle for the little prince , I forgot to add the leather strap to it . (lpp_1943.1536)

```
(c / contrast-01
      :ARG2 (t / thing :quant 1
            :mod (e / extraordinary)
            :time (d / draw-01
                  :ARG0 (i / i
                        :ARG0-of (f / forget-01
                              :ARG1 (a / add-on-05
                                    :ARG0 i
                                    :ARG1 (s / strap
                                          :consist-of (l2 / leather))
                                    :ARG2 m)))
                  :ARG1 (m / muzzle)
                  :ARG2 (p / prince
                        :mod (l / little)))))
```
1537. He will never have been able to fasten it on his sheep . (lpp_1943.1537)

```
(p / possible-01 :polarity -
      :time (e / ever)
      :ARG1 (f / fasten-01
            :ARG0 (h / he)
            :ARG1 (i / it)
            :ARG2 (s / sheep
                  :poss h)))
```
1538. So now I keep wondering : what is happening on his planet ? (lpp_1943.1538)

```
(k / keep-02
      :ARG1 (w / wonder-01
            :ARG0 (i / i)
            :ARG1 (e / event
                  :mod (a / amr-unknown)
                  :location (p / planet
                        :poss (h / he))))
      :time (n / now))
```
1539. Perhaps the sheep has eaten the flower ... (lpp_1943.1539)

```
(p2 / possible-01
      :ARG1 (e / eat-01
            :ARG0 (s / sheep)
            :ARG1 (f / flower)))
```
1540. At one time I say to myself : " Surely not ! (lpp_1943.1540)

```
(s / say-01
      :ARG0 (i / i)
      :ARG1 (h / have-polarity-91
            :ARG2 -
            :ARG1-of (s2 / sure-02))
      :ARG2 i
      :time (o / one))
```
1541. The little prince shuts his flower under her glass globe every night , and he watches over his sheep very carefully ... " (lpp_1943.1541)

```
(a / and
      :op1 (s / shut-01
            :ARG0 (p / prince
                  :mod (l / little))
            :ARG1 (g / globe
                  :consist-of (g2 / glass)
                  :poss (s2 / she)
                  :op1-of (u / under
                        :location-of (f2 / flower
                              :mod (l2 / little)
                              :poss p)))
            :time (r / rate-entity-91
                  :ARG4 (n / night)))
      :op2 (w / watch-01
            :ARG0 p
            :ARG1 (s3 / sheep)
            :manner (c / careful
                  :degree (v / very))))
```
1542. Then I am happy . (lpp_1943.1542)

```
(h / happy-01
      :ARG1 (i / i)
      :time (t / then))
```
1543. And there is sweetness in the laughter of all the stars . (lpp_1943.1543)

```
(a / and
      :op2 (s / sweet-05
            :ARG1 (l / laugh-01
                  :ARG0 (s2 / star
                        :mod (a2 / all)))))
```
1544. But at another time I say to myself : " At some moment or other one is absent - minded , and that is enough ! (lpp_1943.1544)

```
(c / contrast-01
      :ARG2 (s / say-01
            :ARG0 (i / i)
            :ARG1 (a2 / and
                  :op1 (o / one
                        :mod (a3 / absent-minded)
                        :time (o2 / or
                              :op1 (m / moment
                                    :mod (s2 / some))
                              :op2 (o3 / other)))
                  :op2 (t2 / that
                        :mod (e / enough)))
            :ARG2 i
            :time (t / time
                  :mod (a / another))))
```
1545. On some one evening he forgot the glass globe , or the sheep got out , without making any noise , in the night ... " (lpp_1943.1545)

```
(o / or
      :op1 (f / forget-01
            :ARG0 (h / he)
            :ARG1 (g / globe
                  :consist-of (g2 / glass)))
      :op2 (e / escape-01
            :ARG0 (s / sheep)
            :time (d / date-entity
                  :dayperiod (n / night))
            :manner (s3 / sound-02 :polarity -
                  :ARG1 s
                  :mod (a2 / any)))
      :time (d2 / date-entity
            :dayperiod (e2 / evening)
            :mod (s2 / some)))
```
1546. And then the little bells are changed to tears ... (lpp_1943.1546)

```
(a / and
      :op2 (c / change-01
            :ARG1 (b / bell
                  :mod (l / little))
            :ARG2 (t2 / tear-03)
            :time (t / then)))
```
1547. Here , then , is a great mystery . (lpp_1943.1547)

```
(m / mystery
      :mod (g / great)
      :time (t / then)
      :location (h / here))
```
1548. For you who also love the little prince , and for me , nothing in the universe can be the same if somewhere , we do not know where , a sheep that we never saw has - - yes or no ? -- eaten a rose ... (lpp_1943.1548)

```
(p / possible-01
      :ARG1 (s / same-01
            :ARG1 (n / nothing
                  :location (u / universe))
            :ARG3 (a / and
                  :op1 (y / you
                        :ARG0-of (l / love-01
                              :ARG1 (p2 / prince
                                    :mod (l2 / little)))
                        :mod (a2 / also))
                  :op2 (i / i)))
      :condition (e / eat-01 :mode interrogative
            :ARG0 (s2 / sheep
                  :ARG1-of (s3 / see-01 :polarity -
                        :ARG0 (w2 / we)
                        :time (e2 / ever)))
            :ARG1 (r / rose)
            :location (s4 / somewhere
                  :ARG1-of (k / know-01 :polarity -
                        :ARG0 w2))))
```
1549. Look up at the sky . (lpp_1943.1549)

```
(l / look-01 :mode imperative
      :ARG0 (y / you)
      :ARG1 (s / sky)
      :direction (u / up))
```
1550. Ask yourselves : is it yes or no ? (lpp_1943.1550)

```
(a / ask-01 :mode imperative
      :ARG0 (y / you)
      :ARG1 (o / or :mode interrogative
            :op1 (y2 / yes)
            :op2 (n / no))
      :ARG2 y)
```
1551. Has the sheep eaten the flower ? (lpp_1943.1551)

```
(e / eat-01
  :ARG0 (s / sheep)
  :ARG1 (f / flower)
  :mode interrogative)
```
1552. And you will see how everything changes ... (lpp_1943.1552)

```
(a / and
      :op2 (s / see-01
            :ARG0 (y / you)
            :ARG1 (h / have-manner-91
                  :ARG2 (c / change-01
                        :ARG1 (e / everything)))))
```
1553. And no grown - up will ever understand that this is a matter of so much importance ! (lpp_1943.1553)

```
(a / and
      :op2 (u / understand-01 :polarity -
            :ARG0 (g / grown-up)
            :ARG1 (t / this
                  :ARG1-of (m / matter-01
                        :mod (i / important
                              :mod (m2 / much
                                    :degree (s / so)))))
            :time (e2 / ever)))
```
1554. This is , to me , the loveliest and saddest landscape in the world . (lpp_1943.1554)

```
(o / opine-01
      :ARG0 (i / i)
      :ARG1 (l / landscape
            :mod (l2 / lovely
                  :degree (m / most)
                  :compared-to (w / world))
            :ARG0-of (s / sad-02
                  :degree (m2 / most)
                  :compared-to w)
            :domain (t / this)))
```
1555. It is the same as that on the preceding page , but I have drawn it again to impress it on your memory . (lpp_1943.1555)

```
(c / contrast-01
      :ARG1 (s / same-01
            :ARG1 (i / it)
            :ARG2 (t / that
                  :location (p / page
                        :ARG1-of (p2 / precede-01))))
      :ARG2 (d / draw-01
            :ARG0 i
            :ARG1 i
            :mod (a / again)
            :purpose (i2 / impress-01
                  :ARG0 i
                  :ARG1 (m / memory
                        :poss (y / you)))))
```
1556. It is here that the little prince appeared on Earth , and disappeared . (lpp_1943.1556)

```
(a / and
      :op1 (a2 / appear-01
            :ARG1 (p / prince
                  :mod (l / little))
            :location (e / earth))
      :op2 (d / disappear-01
            :ARG1 p)
      :location (h / here))
```
1557. Look at it carefully so that you will be sure to recognise it in case you travel some day to the African desert . (lpp_1943.1557)

```
(l / look-01 :mode imperative
      :ARG0 (y2 / you)
      :ARG1 (i / it)
      :manner (c / careful)
      :purpose (r / recognize-02
            :ARG0 (y / you)
            :ARG1 i
            :ARG1-of (e / ensure-01)
            :condition (t / travel-01
                  :ARG0 y
                  :ARG4 (d / desert
                        :location (c2 / continent :wiki "Africa" :name (n / name :op1 "Africa")))
                  :time (d2 / day
                        :mod (s2 / some)))))
```
1558. And , if you should come upon this spot , please do not hurry on . (lpp_1943.1558)

```
(a / and
      :op2 (h / hurry-01 :polarity - :mode imperative :polite +
            :ARG0 y
            :ARG1 y
            :condition (c / come-upon-26
                  :ARG0 (y / you)
                  :ARG1 (s / spot
                        :mod (t / this)))))
```
1559. Wait for a time , exactly under the star . (lpp_1943.1559)

```
(w / wait-01 :mode imperative
      :ARG1 (y / you)
      :duration (t / time)
      :location (u / under
            :op1 (s / star)
            :manner (e / exact)))
```
1560. Then , if a little man appears who laughs , who has golden hair and who refuses to answer questions , you will know who he is . (lpp_1943.1560)

```
(k / know-01
      :ARG0 (y / you)
      :ARG1 m
      :condition (a / appear-01
            :ARG1 (m / man
                  :mod (l / little)
                  :ARG0-of (l2 / laugh-01)
                  :ARG0-of (h / have-03
                        :ARG1 (h2 / hair
                              :mod (g / golden)))
                  :ARG0-of (r / refuse-01
                        :ARG1 (a2 / answer-01
                              :ARG1 (q / question-01))))
            :time (t / then)))
```
1561. If this should happen , please comfort me . (lpp_1943.1561)

```
(c / comfort-01 :polite + :mode imperative
      :ARG0 (y / you)
      :ARG1 (i / i)
      :condition (t / this))
```
1562. Send me word that he has come back . (lpp_1943.1562)
