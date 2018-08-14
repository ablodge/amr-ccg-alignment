AMRs (Abstract Meaning Representations) for the 1562 sentences of Le Petit Prince, a 1943 novel by Antoine de Saint-Exupery
Version 1.6 - March 14, 2016

1. Chapter 1 . (lpp_1943.1)


(<font color="green">c / chapter</font>
  <font color="blue">:mod</font> 1)

2. Once when I was six years old I saw a magnificent picture in a book , called True Stories from Nature , about the primeval forest . (lpp_1943.2)


(<font color="green">s / see-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> (<font color="green">p / picture</font>
            <font color="blue">:mod</font> (<font color="green">m / magnificent</font>)
            <font color="blue">:location</font> (<font color="green">b2 / book</font> <font color="blue">:wiki</font> -
                  <font color="blue">:name</font> (<font color="green">n / name</font> <font color="blue">:op1</font> "True" <font color="blue">:op2</font> "Stories" <font color="blue">:op3</font> "from" <font color="blue">:op4</font> "Nature")
                  <font color="blue">:topic</font> (<font color="green">f / forest</font>
                        <font color="blue">:mod</font> (<font color="green">p2 / primeval</font>))))
      <font color="blue">:mod</font> (<font color="green">o / once</font>)
      <font color="blue">:time</font> (<font color="green">a / age-01</font>
            <font color="blue">:ARG1</font> i
            <font color="blue">:ARG2</font> (<font color="green">t / temporal</font>-quantity <font color="blue">:quant</font> 6
                  <font color="blue">:unit</font> (<font color="green">y / year</font>))))

3. It was a picture of a boa constrictor in the act of swallowing an animal . (lpp_1943.3)


(<font color="green">p / picture</font>
  <font color="blue">:domain</font> (<font color="green">i / it</font>)
  <font color="blue">:topic</font> (<font color="green">b2 / boa</font>
           <font color="blue">:mod</font> (<font color="green">c2 / constrictor</font>)
           <font color="blue">:ARG0-of</font> (<font color="green">s / swallow-01</font>
                      <font color="blue">:ARG1</font> (<font color="green">a / animal</font>))))

4. Here is a copy of the drawing . (lpp_1943.4)


(<font color="green">b / be</font>-located-at-91
      <font color="blue">:ARG1</font> (<font color="green">t2 / thing</font>
            <font color="blue"><font color="blue">:ARG2</font>-of</font> (<font color="green">c / copy-01</font>
                  <font color="blue">:ARG1</font> (<font color="green">p / picture</font>
                        <font color="blue">:ARG1</font>-of (<font color="green">d / draw-01</font>))))
      <font color="blue">:ARG2</font> (<font color="green">h / here</font>))

5. In the book it said : " Boa constrictors swallow their prey whole , without chewing it . (lpp_1943.5)


(<font color="green">s2 / say-01</font>
      <font color="blue">:ARG0</font> (<font color="green">b2 / book</font>)
      <font color="blue">:ARG1</font> (<font color="green">s / swallow-01</font>
            <font color="blue">:ARG0</font> (<font color="green">b / boa</font>
                  <font color="blue">:mod</font> (<font color="green">c / constrictor</font>))
            <font color="blue">:ARG1</font> (<font color="green">p / prey</font>
                  <font color="blue">:mod</font> (<font color="green">w / whole</font>)
                  <font color="blue">:poss</font> b)
            <font color="blue">:manner</font> (<font color="green">c2 / chew-01</font> <font color="blue">:polarity</font> -
                  <font color="blue">:ARG0</font> b
                  <font color="blue">:ARG1</font> p)))

6. After that they are not able to move , and they sleep through the six months that they need for digestion . " (lpp_1943.6)


(<font color="green">a / and</font>
      <font color="blue">:op1</font> (<font color="green">p / possible-01</font> <font color="blue">:polarity</font> -
            <font color="blue">:ARG1</font> (<font color="green">m / move-01</font>
                  <font color="blue">:ARG0</font> (<font color="green">t / they</font>)
                  <font color="blue">:time</font> (<font color="green">a2 / after</font>
                        <font color="blue">:op1</font> (<font color="green">t3 / that</font>))))
      <font color="blue">:op2</font> (<font color="green">s / sleep-01</font>
            <font color="blue">:ARG0</font> t
            <font color="blue">:duration</font> (<font color="green">t2 / temporal</font>-quantity <font color="blue">:quant</font> 6
                  <font color="blue">:unit</font> (<font color="green">m2 / month</font>)
                  <font color="blue">:ARG1</font>-of (<font color="green">n / need-01</font>
                        <font color="blue">:ARG0</font> t
                        <font color="blue">:purpose</font> (<font color="green">d / digest-01</font>
                              <font color="blue">:ARG0</font> t)))))

7. I pondered deeply , then , over the adventures of the jungle . (lpp_1943.7)


(<font color="green">p / ponder-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> (<font color="green">a / adventure</font>
            <font color="blue">:location</font> (<font color="green">j / jungle</font>))
      <font color="blue">:ARG1</font>-of (<font color="green">d / deep-02</font>)
      <font color="blue">:time</font> (<font color="green">t / then</font>))

8. And after some work with a colored pencil I succeeded in making my first drawing . (lpp_1943.8)


(<font color="green">a2 / and</font>
      <font color="blue">:op2</font> (<font color="green">s / succeed-01</font>
            <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
            <font color="blue">:ARG1</font> (<font color="green">m / make-01</font>
                  <font color="blue">:ARG0</font> i
                  <font color="blue">:ARG1</font> (<font color="green">p2 / picture</font>
                        <font color="blue">:ARG1</font>-of (<font color="green">d / draw-01</font>
                              <font color="blue">:ARG0</font> i
                              <font color="blue">:ord</font> (<font color="green">o / ordinal</font>-entity <font color="blue">:value</font> 1))))
            <font color="blue">:time</font> (<font color="green">a / after</font>
                  <font color="blue">:op1</font> (<font color="green">w / work-01</font>
                        <font color="blue">:ARG0</font> i
                        <font color="blue">:instrument</font> (<font color="green">p / pencil</font>
                              <font color="blue">:mod</font> (<font color="green">c / color</font>))
                        <font color="blue">:mod</font> (<font color="green">s2 / some</font>)))))

9. My Drawing Number One . (lpp_1943.9)


(<font color="green">p / picture</font> <font color="blue">:wiki</font> -
      <font color="blue">:name</font> (<font color="green">n2 / name</font> <font color="blue">:op1</font> "Drawing" <font color="blue">:op2</font> "Number" <font color="blue">:op3</font> "One")
      <font color="blue">:poss</font> (<font color="green">i / i</font>))

10. It looked like this : I showed my masterpiece to the grown - ups , and asked them whether the drawing frightened them . (lpp_1943.10)


(<font color="green">a / and</font>
      <font color="blue">:op1</font> (<font color="green">l / look-02</font>
            <font color="blue">:ARG0</font> (<font color="green">i / it</font>)
            <font color="blue">:ARG1</font> (<font color="green">t / this</font>))
      <font color="blue">:op2</font> (<font color="green">s / show-01</font>
            <font color="blue">:ARG0</font> (<font color="green">i2 / i</font>)
            <font color="blue">:ARG1</font> (<font color="green">m / masterpiece</font>
                  <font color="blue">:poss</font> i2)
            <font color="blue">:ARG2</font> (<font color="green">g / grown</font>-up))
      <font color="blue">:op3</font> (<font color="green">a2 / ask-01</font>
            <font color="blue">:ARG0</font> i2
            <font color="blue">:ARG1</font> (<font color="green">f / frighten-01</font> <font color="blue">:mode</font> interrogative
                  <font color="blue">:ARG0</font> (<font color="green">p / picture</font>
                        <font color="blue">:ARG1</font>-of (<font color="green">d / draw-01</font>))
                  <font color="blue">:ARG1</font> g)
            <font color="blue">:ARG2</font> g))

11. But they answered : " Frighten ? (lpp_1943.11)


(<font color="green">c / contrast-01</font>
  <font color="blue">:ARG2</font> (<font color="green">a / answer-01</font>
          <font color="blue">:ARG0</font> (<font color="green">t / they</font>)
          <font color="blue">:ARG2</font> (<font color="green">f / frighten-01</font>
                  <font color="blue">:mode</font> interrogative)))

12. Why should any one be frightened by a hat ? " (lpp_1943.12)


(<font color="green">f / frighten-01</font>
  <font color="blue">:ARG0</font> (<font color="green">h / hat</font>)
  <font color="blue">:ARG1</font> (<font color="green">o / one</font>
          <font color="blue">:mod</font> (<font color="green">a / any</font>))
  <font color="blue">:ARG1</font>-of (<font color="green">c / cause-01</font>
             <font color="blue">:ARG0</font> (<font color="green">a2 / amr</font>-unknown)))

13. My drawing was not a picture of a hat . (lpp_1943.13)


(<font color="green">p / picture-01</font> <font color="blue">:polarity</font> -
      <font color="blue">:ARG0</font> (<font color="green">p2 / picture</font>
            <font color="blue"><font color="blue">:ARG1</font>-of</font> (<font color="green">d / draw-01</font>
                  <font color="blue">:ARG0</font> (<font color="green">i / i</font>)))
      <font color="blue">:ARG1</font> (<font color="green">h / hat</font>))

14. It was a picture of a boa constrictor digesting an elephant . (lpp_1943.14)


(<font color="green">p / picture-01</font>
  <font color="blue">:ARG0</font> (<font color="green">i / it</font>)
  <font color="blue">:ARG1</font> (<font color="green">b2 / boa</font>
          <font color="blue">:mod</font> (<font color="green">c / constrictor</font>)
          <font color="blue">:ARG0</font>-of (<font color="green">d / digest-01</font>
                     <font color="blue">:ARG1</font> (<font color="green">e / elephant</font>))))

15. But since the grown - ups were not able to understand it , I made another drawing : I drew the inside of the boa constrictor , so that the grown - ups could see it clearly . (lpp_1943.15)


(<font color="green">c / contrast-01</font>
      <font color="blue">:ARG2</font> (<font color="green">a2 / and</font>
            <font color="blue">:op1</font> (<font color="green">d3 / draw-01</font>
                  <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
                  <font color="blue">:ARG1</font> (<font color="green">p2 / picture</font>
                        <font color="blue">:mod</font> (<font color="green">a / another</font>))
                  <font color="blue">:ARG1</font>-of (<font color="green">c3 / cause-01</font>
                        <font color="blue">:ARG0</font> (<font color="green">p3 / possible-01</font> <font color="blue">:polarity</font> -
                              <font color="blue">:ARG1</font> (<font color="green">u / understand-01</font>
                                    <font color="blue">:ARG0</font> (<font color="green">g / grown</font>-up)
                                    <font color="blue">:ARG1</font> (<font color="green">i2 / it</font>)))))
            <font color="blue">:op2</font> (<font color="green">d / draw-01</font>
                  <font color="blue">:ARG0</font> i
                  <font color="blue">:ARG1</font> (<font color="green">i3 / inside</font>
                        <font color="blue">:part-of</font> (<font color="green">b2 / boa</font>
                              <font color="blue">:mod</font> (<font color="green">c4 / constrictor</font>)))
                  <font color="blue">:purpose</font> (<font color="green">p / possible-01</font>
                        <font color="blue">:ARG1</font> (<font color="green">s / see-01</font>
                              <font color="blue">:ARG0</font> g
                              <font color="blue">:ARG1</font> (<font color="green">i4 / it</font>)
                              <font color="blue">:ARG1</font>-of (<font color="green">c2 / clear-06</font>))))))

16. They always need to have things explained . (lpp_1943.16)


(<font color="green">n / need-01</font>
      <font color="blue">:ARG0</font> (<font color="green">t / they</font>)
      <font color="blue">:ARG1</font> (<font color="green">e / explain-01</font>)
      <font color="blue">:time</font> (<font color="green">a / always</font>))

17. My Drawing Number Two looked like this : The grown - ups ' response , this time , was to advise me to lay aside my drawings of boa constrictors , whether from the inside or the outside , and devote myself instead to geography , history , arithmetic and grammar . (lpp_1943.17)


(<font color="green">a6 / and</font>
      <font color="blue">:op1</font> (<font color="green">l / look-02</font>
            <font color="blue">:ARG0</font> (<font color="green">p / picture</font> <font color="blue">:wiki</font> - <font color="blue">:name</font> (<font color="green">n / name</font> <font color="blue">:op1</font> "Drawing" <font color="blue">:op2</font> "Number" <font color="blue">:op3</font> "Two")
                  <font color="blue">:poss</font> i)
            <font color="blue">:ARG1</font> (<font color="green">t2 / this</font>))
      <font color="blue">:op2</font> (<font color="green">r / respond-01</font>
            <font color="blue">:ARG0</font> (<font color="green">g / grown</font>-up)
            <font color="blue">:ARG1</font> (<font color="green">i / i</font>)
            <font color="blue">:ARG2</font> (<font color="green">a / advise-01</font>
                  <font color="blue">:ARG0</font> g
                  <font color="blue">:ARG1</font> i
                  <font color="blue">:ARG2</font> (<font color="green">a3 / and</font>
                        <font color="blue">:op1</font> (<font color="green">l2 / lay-01</font>
                              <font color="blue">:ARG0</font> i
                              <font color="blue">:ARG1</font> (<font color="green">p2 / picture</font>
                                    <font color="blue">:ARG1</font>-of (<font color="green">d2 / draw-01</font>
                                          <font color="blue">:ARG0</font> i)
                                    <font color="blue">:topic</font> (<font color="green">b2 / boa</font>
                                          <font color="blue">:mod</font> (<font color="green">c2 / constrictor</font>)
                                          <font color="blue">:mod</font> (<font color="green">o / or</font>
                                                <font color="blue">:op1</font> (<font color="green">i2 / inside</font>)
                                                <font color="blue">:op2</font> (<font color="green">o2 / outside</font>))))
                              <font color="blue">:ARG2</font> (<font color="green">a2 / aside</font>))
                        <font color="blue">:op2</font> (<font color="green">d3 / devote-01</font>
                              <font color="blue">:ARG0</font> i
                              <font color="blue">:ARG1</font> i
                              <font color="blue">:ARG2</font> (<font color="green">a4 / and</font>
                                    <font color="blue">:op1</font> (<font color="green">g2 / geography</font>)
                                    <font color="blue">:op2</font> (<font color="green">h / history</font>)
                                    <font color="blue">:op3</font> (<font color="green">a5 / arithmetic</font>)
                                    <font color="blue">:op4</font> (<font color="green">g3 / grammar</font>))
                              <font color="blue">:ARG1</font>-of (<font color="green">i4 / instead</font>-of-91
                                    <font color="blue">:ARG2</font> d2))))
            <font color="blue">:time</font> (<font color="green">t4 / time</font>
                  <font color="blue">:mod</font> (<font color="green">t5 / this</font>))))

18. That is why , at the age of six , I gave up what might have been a magnificent career as a painter . (lpp_1943.18)


(<font color="green">c2 / cause-01</font>
      <font color="blue">:ARG0</font> (<font color="green">t2 / that</font>)
      <font color="blue">:ARG1</font> (<font color="green">g / give</font>-up-07
            <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
            <font color="blue">:ARG1</font> (<font color="green">c / career</font>
                  <font color="blue">:mod</font> (<font color="green">m / magnificent</font>)
                  <font color="blue">:topic</font> (<font color="green">p / person</font>
                        <font color="blue">:ARG0</font>-of (<font color="green">p2 / paint-02</font>)))
            <font color="blue">:time</font> (<font color="green">a / age-01</font>
                  <font color="blue">:ARG1</font> i
                  <font color="blue">:ARG2</font> (<font color="green">t / temporal</font>-quantity <font color="blue">:quant</font> 6
                        <font color="blue">:unit</font> (<font color="green">y / year</font>)))))

19. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two . (lpp_1943.19)


(<font color="green">d / dishearten-01</font>
      <font color="blue">:ARG0</font> (<font color="green">f / fail-01</font>
            <font color="blue">:ARG1</font> (<font color="green">a / and</font>
                  <font color="blue">:op1</font> (<font color="green">p / picture</font> <font color="blue">:wiki</font> -
                        <font color="blue">:name</font> (<font color="green">n / name</font> <font color="blue">:op1</font> "Drawing" <font color="blue">:op2</font> "Number" <font color="blue">:op3</font> "One"))
                  <font color="blue">:op2</font> (<font color="green">p2 / picture</font> <font color="blue">:wiki</font> -
                        <font color="blue">:name</font> (<font color="green">n2 / name</font> <font color="blue">:op1</font> "Drawing" <font color="blue">:op2</font> "Number" <font color="blue">:op3</font> "Two"))
                  <font color="blue">:poss</font> i))
      <font color="blue">:ARG1</font> (<font color="green">i / i</font>))

20. Grown - ups never understand anything by themselves , and it is tiresome for children to be always and forever explaining things to them . (lpp_1943.20)


(<font color="green">a / and</font>
      <font color="blue">:op1</font> (<font color="green">u / understand-01</font> <font color="blue">:polarity</font> -
            <font color="blue">:ARG0</font> (<font color="green">g / grown</font>-up)
            <font color="blue">:ARG1</font> (<font color="green">a3 / anything</font>)
            <font color="blue">:time</font> (<font color="green">e2 / ever</font>)
            <font color="blue">:mod</font> (<font color="green">b / by</font>-oneself))
      <font color="blue">:op2</font> (<font color="green">t / tiresome</font>
            <font color="blue">:domain</font> (<font color="green">e / explain-01</font>
                  <font color="blue">:ARG0</font> (<font color="green">c / child</font>)
                  <font color="blue">:ARG1</font> (<font color="green">t2 / thing</font>)
                  <font color="blue">:ARG2</font> g
                  <font color="blue">:time</font> (<font color="green">a4 / always</font>)
                  <font color="blue">:mod</font> (<font color="green">f / forever</font>))))

21. So then I chose another profession , and learned to pilot airplanes . (lpp_1943.21)


(<font color="green">c2 / cause-01</font>
  <font color="blue">:ARG1</font> (<font color="green">a / and</font>
          <font color="blue">:op1</font> (<font color="green">c / choose-01</font>
                 <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
                 <font color="blue">:ARG1</font> (<font color="green">p / profession</font>
                         <font color="blue">:mod</font> (<font color="green">a2 / another</font>)))
          <font color="blue">:op2</font> (<font color="green">l / learn-01</font>
                 <font color="blue">:ARG0</font> i
                 <font color="blue">:ARG1</font> (<font color="green">p2 / pilot-01</font>
                         <font color="blue">:ARG0</font> i
                         <font color="blue">:ARG1</font> (<font color="green">a3 / airplane</font>)))))

22. I have flown a little over all parts of the world ; and it is true that geography has been very useful to me . (lpp_1943.22)


(<font color="green">a / and</font>
      <font color="blue">:op1</font> (<font color="green">f / fly-01</font>
            <font color="blue">:ARG0</font> i
            <font color="blue">:location</font> (<font color="green">o / over</font>
                  <font color="blue">:op1</font> (<font color="green">p2 / part</font>
                        <font color="blue">:part-of</font> (<font color="green">w / world</font>))))
      <font color="blue">:op2</font> (<font color="green">u / useful-05</font>
            <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
            <font color="blue">:ARG1</font> (<font color="green">g / geography</font>)
            <font color="blue">:degree</font> (<font color="green">v / very</font>)))

23. At a glance I can distinguish China from Arizona . (lpp_1943.23)


(<font color="green">p / possible-01</font>
      <font color="blue">:ARG1</font> (<font color="green">d / distinguish-01</font>
            <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
            <font color="blue">:ARG1</font> (<font color="green">c / country</font> <font color="blue">:wiki</font> "China"
                  <font color="blue">:name</font> (<font color="green">n / name</font> <font color="blue">:op1</font> "China"))
            <font color="blue">:ARG2</font> (<font color="green">s / state</font> <font color="blue">:wiki</font> "Arizona"
                  <font color="blue">:name</font> (<font color="green">n2 / name</font> <font color="blue">:op1</font> "Arizona"))
            <font color="blue">:manner</font> (<font color="green">g / glance-01</font>
                  <font color="blue">:ARG0</font> i)))

24. If one gets lost in the night , such knowledge is valuable . (lpp_1943.24)


(<font color="green">v / value-02</font>
      <font color="blue">:ARG1</font> (<font color="green">k / knowledge</font>
            <font color="blue">:mod</font> (<font color="green">s / such</font>))
      <font color="blue">:condition</font> (<font color="green">g / get-03</font>
            <font color="blue">:ARG1</font> (<font color="green">o / one</font>)
            <font color="blue">:ARG2</font> (<font color="green">l / lost</font>
                  <font color="blue">:time</font> (<font color="green">d / date</font>-entity <font color="blue">:dayperiod</font> (<font color="green">n / night</font>)))))

25. In the course of this life I have had a great many encounters with a great many people who have been concerned with matters of consequence . (lpp_1943.25)


(<font color="green">e / encounter-01</font>
  <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
  <font color="blue">:ARG1</font> (<font color="green">p / person</font>
          <font color="blue">:quant</font> (<font color="green">m2 / many</font>
                   <font color="blue">:mod</font> (<font color="green">g2 / great</font>))
          <font color="blue">:ARG1</font>-of (<font color="green">c / concern-01</font>
                     <font color="blue">:ARG0</font> (<font color="green">m3 / matter</font>
                             <font color="blue">:mod</font> (<font color="green">c2 / consequence</font>))))
  <font color="blue">:quant</font> (<font color="green">m / many</font>
           <font color="blue">:mod</font> (<font color="green">g / great</font>))
  <font color="blue">:time</font> (<font color="green">c3 / course</font>
          <font color="blue">:poss</font> (<font color="green">l / life</font>
                  <font color="blue">:mod</font> (<font color="green">t / this</font>))))

26. I have lived a great deal among grown - ups . (lpp_1943.26)


(<font color="green">l / live-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:mod</font> (<font color="green">d / deal</font>
            <font color="blue">:mod</font> (<font color="green">g2 / great</font>))
      <font color="blue">:location</font> (<font color="green">a / among</font>
            <font color="blue">:op1</font> (<font color="green">g / grown</font>-up)))

27. I have seen them intimately , close at hand . (lpp_1943.27)


(<font color="green">s / see-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> (<font color="green">t / they</font>)
      <font color="blue">:ARG1</font>-of (<font color="green">c / close-10</font>
            <font color="blue">:ARG2</font> (<font color="green">a / at</font>-hand))
      <font color="blue">:ARG2</font>-of (<font color="green">i2 / intimate-02</font>
            <font color="blue">:ARG1</font> i))

28. And that has n't much improved my opinion of them . (lpp_1943.28)


(<font color="green">a / and</font>
      <font color="blue">:op2</font> (<font color="green">i / improve-01</font> <font color="blue">:polarity</font> -
            <font color="blue">:ARG0</font> (<font color="green">t / that</font>)
            <font color="blue">:ARG1</font> (<font color="green">t3 / thing</font>
                  <font color="blue">:ARG1</font>-of (<font color="green">o2 / opine-01</font>
                        <font color="blue">:ARG0</font> (<font color="green">i2 / i</font>)
                        <font color="blue">:topic</font> (<font color="green">t2 / they</font>)))
            <font color="blue">:degree</font> (<font color="green">m2 / much</font>)))

29. Whenever I met one of them who seemed to me at all clear - sighted , I tried the experiment of showing him my Drawing Number One , which I have always kept . (lpp_1943.29)


(<font color="green">t / try-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> (<font color="green">e / experiment-01</font>
            <font color="blue">:ARG1</font> (<font color="green">s / show-01</font>
                  <font color="blue">:ARG1</font> (<font color="green">p2 / picture</font> <font color="blue">:wiki</font> - <font color="blue">:name</font> (<font color="green">n / name</font> <font color="blue">:op1</font> "Drawing" <font color="blue">:op2</font> "Number" <font color="blue">:op3</font> "One"))
                  <font color="blue">:ARG2</font> p
                  <font color="blue">:ARG1</font>-of (<font color="green">k / keep-01</font>
                        <font color="blue">:ARG0</font> i
                        <font color="blue">:time</font> (<font color="green">a / always</font>))))
      <font color="blue">:time</font> (<font color="green">m / meet-02</font>
            <font color="blue">:ARG0</font> i
            <font color="blue">:ARG1</font> (<font color="green">p / person</font>
                  <font color="blue">:ARG1</font>-of (<font color="green">i2 / include-91</font>
                        <font color="blue">:ARG2</font> (<font color="green">t3 / they</font>))
                  <font color="blue">:ARG0</font>-of (<font color="green">s3 / see-01</font>
                        <font color="blue">:ARG1</font>-of (<font color="green">c / clear-08</font>)
                        <font color="blue">:ARG1</font>-of (<font color="green">s4 / seem-01</font>
                              <font color="blue">:ARG2</font> i)))
            <font color="blue">:mod</font> (<font color="green">a2 / any</font>)))

30. I would try to find out , so , if this was a person of true understanding . (lpp_1943.30)


(<font color="green">t / try-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> (<font color="green">f / find</font>-out-03
            <font color="blue">:ARG0</font> i
            <font color="blue">:ARG1</font> (<font color="green">u2 / understand-01</font> <font color="blue"><font color="blue">:mod</font>e</font> interrogative
                  <font color="blue">:ARG0</font> (<font color="green">p / person</font>
                        <font color="blue">:mod</font> (<font color="green">t2 / this</font>))
                  <font color="blue">:ARG1</font>-of (<font color="green">t3 / true-01</font>))))

31. But , whoever it was , he , or she , would always say : " That is a hat . " (lpp_1943.31)


(<font color="green">c / contrast-01</font>
  <font color="blue">:ARG2</font> (<font color="green">s / say-01</font>
          <font color="blue">:ARG0</font> (<font color="green">o / or</font>
                  <font color="blue">:op1</font> (<font color="green">h / he</font>)
                  <font color="blue">:op2</font> (<font color="green">s2 / she</font>))
          <font color="blue">:ARG1</font> (<font color="green">h2 / hat</font>
                  <font color="blue">:domain</font> (<font color="green">t / that</font>))
          <font color="blue">:time</font> (<font color="green">a / always</font>)))

32. Then I would never talk to that person about boa constrictors , or primeval forests , or stars . (lpp_1943.32)


(<font color="green">t / talk-01</font>
  <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
  <font color="blue">:ARG1</font> (<font color="green">o / or</font>
          <font color="blue">:op1</font> (<font color="green">b / boa</font>
                 <font color="blue">:mod</font> (<font color="green">c2 / constrictor</font>))
          <font color="blue">:op2</font> (<font color="green">f / forest</font>
                 <font color="blue">:mod</font> (<font color="green">p2 / primeval</font>))
          <font color="blue">:op3</font> (<font color="green">s / star</font>))
  <font color="blue">:ARG2</font> (<font color="green">p / person</font>
          <font color="blue">:mod</font> (<font color="green">t2 / that</font>))
  <font color="blue">:time</font> (<font color="green">e / ever</font>)
  <font color="blue">:polarity</font> -)

33. I would bring myself down to his level . (lpp_1943.33)


(<font color="green">b / bring-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> i
      <font color="blue">:ARG2</font> (<font color="green">l / level</font>
            <font color="blue">:poss</font> (<font color="green">h / he</font>))
      <font color="blue">:ARG3</font> (<font color="green">d / down</font>))

34. I would talk to him about bridge , and golf , and politics , and neckties . (lpp_1943.34)


(<font color="green">t / talk-01</font>
  <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
  <font color="blue">:ARG1</font> (<font color="green">a / and</font>
          <font color="blue">:op1</font> (<font color="green">b / bridge</font>)
          <font color="blue">:op2</font> (<font color="green">g / golf</font>)
          <font color="blue">:op3</font> (<font color="green">p / politics</font>)
          <font color="blue">:op4</font> (<font color="green">n2 / necktie</font>))
  <font color="blue">:ARG2</font> (<font color="green">h / he</font>))

35. And the grown - up would be greatly pleased to have met such a sensible man . (lpp_1943.35)


(<font color="green">a / and</font>
      <font color="blue">:op2</font> (<font color="green">p / please-01</font>
            <font color="blue">:ARG0</font> (<font color="green">m / meet-02</font>
                  <font color="blue">:ARG0</font> g
                  <font color="blue">:ARG1</font> (<font color="green">m2 / man</font>
                        <font color="blue">:ARG2-of</font> (<font color="green">s / sense-02</font>
                              <font color="blue">:degree</font> (<font color="green">s2 / such</font>))))
            <font color="blue">:ARG1</font> (<font color="green">g / grown</font>-up)
            <font color="blue">:degree</font> (<font color="green">g2 / great</font>)))

36. Chapter 2 . (lpp_1943.36)


(<font color="green">c / chapter</font>
  <font color="blue">:mod</font> 2)

37. So I lived my life alone , without anyone that I could really talk to , until I had an accident with my plane in the Desert of Sahara , six years ago . (lpp_1943.37)


(<font color="green">c / cause-01</font>
      <font color="blue">:ARG1</font> (<font color="green">l / live-01</font>
            <font color="blue">:ARG0</font> (<font color="green">i / i</font>
                  <font color="blue">:ARG0</font>-of (<font color="green">t3 / talk-01</font> <font color="blue">:polarity</font> -
                        <font color="blue">:ARG2</font> (<font color="green">a5 / anyone</font>)
                        <font color="blue">:ARG1</font>-of (<font color="green">r / real-04</font>)))
            <font color="blue">:ARG1</font> (<font color="green">l2 / life</font>
                  <font color="blue">:poss</font> i)
            <font color="blue">:manner</font> (<font color="green">a / alone</font>)
            <font color="blue">:duration</font> (<font color="green">u / until</font>
                  <font color="blue">:op1</font> (<font color="green">h / have-06</font>
                        <font color="blue">:ARG0</font> i
                        <font color="blue">:ARG1</font> (<font color="green">a3 / accident</font>
                              <font color="blue">:mod</font> (<font color="green">p / plane</font>))
                        <font color="blue">:location</font> (<font color="green">d / desert</font> <font color="blue">:wiki</font> "Sahara" <font color="blue">:name</font> (<font color="green">n / name</font> <font color="blue">:op1</font> "Desert" <font color="blue">:op2</font> "of" <font color="blue">:op3</font> "Sahara"))
                        <font color="blue">:time</font> (<font color="green">b / before</font>
                              <font color="blue">:op1</font> (<font color="green">n2 / now</font>)
                              <font color="blue">:quant</font> (<font color="green">t2 / temporal</font>-quantity <font color="blue">:quant</font> 6
                                    <font color="blue">:unit</font> (<font color="green">y / year</font>)))))))

38. Something was broken in my engine . (lpp_1943.38)


(<font color="green">b / break-01</font>
      <font color="blue">:ARG1</font> (<font color="green">s / something</font>
            <font color="blue">:location</font> (<font color="green">e / engine</font>
                  <font color="blue">:poss</font> (<font color="green">i / i</font>))))

39. And as I had with me neither a mechanic nor any passengers , I set myself to attempt the difficult repairs all alone . (lpp_1943.39)


(<font color="green">a / and</font>
  <font color="blue">:op2</font> (<font color="green">c / cause-01</font>
         <font color="blue">:ARG0</font> (<font color="green">h / have-03</font>
                 <font color="blue">:ARG0</font> i
                 <font color="blue">:ARG1</font> (<font color="green">o / or</font>
                         <font color="blue">:op1</font> (<font color="green">m / mechanic</font>)
                         <font color="blue">:op2</font> (<font color="green">p / passenger</font>))
                 <font color="blue">:accompanier</font> (<font color="green">i / i</font>)
                 <font color="blue">:polarity</font> -)
         <font color="blue">:ARG1</font> (<font color="green">a2 / attempt-01</font>
                 <font color="blue">:ARG0</font> i
                 <font color="blue">:ARG1</font> (<font color="green">r / repair-01</font>
                         <font color="blue">:mod</font> (<font color="green">d / difficult</font>))
                 <font color="blue">:mod</font> (<font color="green">a3 / alone</font>
                        <font color="blue">:degree</font> (<font color="green">a4 / all</font>)))))

40. It was a question of life or death for me : I had scarcely enough drinking water to last a week . (lpp_1943.40)


(<font color="green">q / question-01</font>
      <font color="blue">:ARG0</font> i
      <font color="blue">:ARG1</font> (<font color="green">o / or</font>
            <font color="blue">:op1</font> (<font color="green">l / live-01</font>)
            <font color="blue">:op2</font> (<font color="green">d / die-01</font>))
      <font color="blue">:ARG1</font>-of (<font color="green">c / cause-01</font>
            <font color="blue">:ARG0</font> (<font color="green">h / have-03</font>
                  <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
                  <font color="blue">:ARG1</font> (<font color="green">w / water</font>
                        <font color="blue">:purpose</font> (<font color="green">d2 / drink-01</font>
                              <font color="blue">:ARG0</font> i)
                        <font color="blue">:quant</font> (<font color="green">e / enough</font>
                              <font color="blue">:mod</font> (<font color="green">s / scarce</font>))
                        <font color="blue">:ARG1</font>-of (<font color="green">l2 / last-03</font>
                              <font color="blue">:ARG2</font> (<font color="green">t / temporal</font>-quantity <font color="blue">:quant</font> 1
                                    <font color="blue">:unit</font> (<font color="green">w2 / week</font>))
                              <font color="blue">:ARG3</font> i)))))

41. The first night , then , I went to sleep on the sand , a thousand miles from any human habitation . (lpp_1943.41)


(<font color="green">s / sleep-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:location</font> (<font color="green">s2 / sand</font>)
      <font color="blue">:time</font> (<font color="green">d2 / date</font>-entity
            <font color="blue">:dayperiod</font> (<font color="green">n / night</font>)
            <font color="blue">:ord</font> (<font color="green">o / ordinal</font>-entity <font color="blue">:value</font> 1))
      <font color="blue">:location</font> (<font color="green">r / relative</font>-position
            <font color="blue">:op1</font> (<font color="green">p / place</font>
                  <font color="blue">:ARG1-of</font> (<font color="green">i2 / inhabit-01</font>
                        <font color="blue">:ARG0</font> (<font color="green">h / human</font>))
                  <font color="blue">:mod</font> (<font color="green">a2 / any</font>))
            <font color="blue">:quant</font> (<font color="green">d / distance</font>-quantity <font color="blue">:quant</font> 1000
                  <font color="blue">:unit</font> (<font color="green">m / mile</font>))
            <font color="blue">:direction</font> (<font color="green">a3 / away</font>)))

42. I was more isolated than a shipwrecked sailor on a raft in the middle of the ocean . (lpp_1943.42)


(<font color="green">i / isolate-01</font>
      <font color="blue">:ARG1</font> (<font color="green">i2 / i</font>)
      <font color="blue">:degree</font> (<font color="green">m / more</font>)
      <font color="blue">:compared-to</font> (<font color="green">p / person</font>
            <font color="blue">:ARG0-of</font> (<font color="green">s / sail-01</font>)
            <font color="blue">:ARG1</font>-of (<font color="green">s2 / shipwreck-01</font>)
            <font color="blue">:location</font> (<font color="green">r / raft</font>
                  <font color="blue">:location</font> (<font color="green">o / ocean</font>
                        <font color="blue">:part</font> (<font color="green">m2 / middle</font>)))))

43. Thus you can imagine my amazement , at sunrise , when I was awakened by an odd little voice . (lpp_1943.43)


(<font color="green">c / cause-01</font>
      <font color="blue">:ARG1</font> (<font color="green">p / possible-01</font>
            <font color="blue">:ARG1</font> (<font color="green">i2 / imagine-01</font>
                  <font color="blue">:ARG0</font> (<font color="green">y / you</font>)
                  <font color="blue">:ARG1</font> (<font color="green">a / amaze-01</font>
                        <font color="blue">:ARG1</font> (<font color="green">i / i</font>)
                        <font color="blue">:time</font> (<font color="green">s / sunrise</font>
                              <font color="blue">:time</font>-of (<font color="green">w / wake-01</font>
                                    <font color="blue">:ARG0</font> (<font color="green">v / voice</font>
                                          <font color="blue">:mod</font> (<font color="green">o / odd</font>)
                                          <font color="blue">:mod</font> (<font color="green">l / little</font>))
                                    <font color="blue">:ARG1</font> i))))))

44. It said : " If you please -- draw me a sheep ! " (lpp_1943.44)


(<font color="green">s / say-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / it</font>)
      <font color="blue">:ARG1</font> (<font color="green">d / draw-01</font> <font color="blue">:mode</font> imperative <font color="blue">:polite</font> +
            <font color="blue">:ARG0</font> (<font color="green">y2 / you</font>)
            <font color="blue">:ARG1</font> (<font color="green">s2 / sheep</font>)
            <font color="blue">:ARG2</font> (<font color="green">i2 / i</font>)))

45. " What ! " (lpp_1943.45)


(<font color="green">s / string</font>-entity <font color="blue">:value</font> "what")

46. " Draw me a sheep ! " (lpp_1943.46)


(<font color="green">d / draw-01</font>
  <font color="blue">:ARG0</font> (<font color="green">y / you</font>)
  <font color="blue">:ARG1</font> (<font color="green">s / sheep</font>)
  <font color="blue">:ARG2</font> (<font color="green">i / i</font>)
  <font color="blue">:mode</font> imperative)

47. I jumped to my feet , completely thunderstruck . (lpp_1943.47)


(<font color="green">j / jump-03</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>
            <font color="blue">:mod</font> (<font color="green">t / thunderstruck</font>
                  <font color="blue">:ARG1-of</font> (<font color="green">c / complete-02</font>)))
      <font color="blue">:destination</font> (<font color="green">f / foot</font>
            <font color="blue">:part-of</font> i))

48. I blinked my eyes hard . (lpp_1943.48)


(<font color="green">b / blink-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> (<font color="green">e / eye</font>
            <font color="blue">:part-of</font> i)
      <font color="blue">:ARG1</font>-of (<font color="green">h / hard-04</font>))

49. I looked carefully all around me . (lpp_1943.49)


(<font color="green">l / look-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:direction</font> (<font color="green">a / around</font>
            <font color="blue">:op1</font> i
            <font color="blue">:mod</font> (<font color="green">a2 / all</font>))
      <font color="blue">:manner</font> (<font color="green">c / careful</font>))

50. And I saw a most extraordinary small person , who stood there examining me with great seriousness . (lpp_1943.50)


(<font color="green">a / and</font>
      <font color="blue">:op2</font> (<font color="green">s / see-01</font>
            <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
            <font color="blue">:ARG1</font> (<font color="green">p / person</font>
                  <font color="blue">:mod</font> (<font color="green">s2 / small</font>)
                  <font color="blue">:mod</font> (<font color="green">e / extraordinary</font>
                        <font color="blue">:degree</font> (<font color="green">m / most</font>))
                  <font color="blue">:ARG1</font>-of (<font color="green">s3 / stand-01</font>
                        <font color="blue">:ARG2</font> (<font color="green">t / there</font>))
                  <font color="blue">:ARG0</font>-of (<font color="green">e2 / examine-01</font>
                        <font color="blue">:ARG1</font> i
                        <font color="blue">:ARG2</font>-of (<font color="green">s4 / serious-01</font>
                              <font color="blue">:degree</font> (<font color="green">g / great</font>))))))

51. Here you may see the best portrait that , later , I was able to make of him . (lpp_1943.51)


(<font color="green">p / possible-01</font>
      <font color="blue">:ARG1</font> (<font color="green">s / see-01</font>
            <font color="blue">:ARG0</font> (<font color="green">y / you</font>)
            <font color="blue">:ARG1</font> (<font color="green">p2 / portrait</font>
                  <font color="blue">:ARG1</font>-of (<font color="green">g / good-02</font>
                        <font color="blue">:degree</font> (<font color="green">m / most</font>))
                  <font color="blue">:ARG1</font>-of (<font color="green">m2 / make-01</font>
                        <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
                        <font color="blue">:ARG1</font>-of (<font color="green">p3 / possible-01</font>)
                        <font color="blue">:time</font> (<font color="green">l / late</font>
                              <font color="blue">:degree</font> (<font color="green">m3 / more</font>)))
                  <font color="blue">:topic</font> (<font color="green">h / he</font>))
            <font color="blue">:location</font> (<font color="green">h2 / here</font>)))

52. But my drawing is certainly very much less charming than its model . (lpp_1943.52)


(<font color="green">c3 / contrast-01</font>
      <font color="blue">:ARG2</font> (<font color="green">c / charm-01</font>
            <font color="blue">:ARG0</font> (<font color="green">p / picture</font>
                  <font color="blue">:ARG1-of</font> (<font color="green">d / draw-01</font>
                        <font color="blue">:ARG0</font> (<font color="green">i / i</font>)))
            <font color="blue">:quant</font> (<font color="green">l / less</font>
                  <font color="blue">:degree</font> (<font color="green">m / much</font>
                        <font color="blue">:degree</font> (<font color="green">v / very</font>)))
            <font color="blue">:mod</font> (<font color="green">c2 / certain</font>)
            <font color="blue">:compared-to</font> (<font color="green">m2 / model</font>
                  <font color="blue">:poss</font> p)))

53. That , however , is not my fault . (lpp_1943.53)


(<font color="green">c / contrast-01</font>
  <font color="blue">:ARG2</font> (<font color="green">f / fault-01</font>
          <font color="blue">:ARG1</font> (<font color="green">i / i</font>)
          <font color="blue">:ARG2</font> (<font color="green">t / that</font>)
          <font color="blue">:polarity</font> -))

54. The grown - ups discouraged me in my painter 's career when I was six years old , and I never learned to draw anything , except boas from the outside and boas from the inside . (lpp_1943.54)


(<font color="green">d / discourage-01</font>
      <font color="blue">:ARG0</font> (<font color="green">g / grown</font>-up)
      <font color="blue">:ARG1</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG2</font> (<font color="green">c / career</font>
            <font color="blue">:topic</font> (<font color="green">p / person</font>
                  <font color="blue">:ARG0</font>-of (<font color="green">p2 / paint-02</font>))
            <font color="blue">:poss</font> i)
      <font color="blue">:ARG0</font>-of (<font color="green">c2 / cause-01</font>
            <font color="blue">:ARG1</font> (<font color="green">l / learn-01</font> <font color="blue">:polarity</font> -
                  <font color="blue">:ARG0</font> i
                  <font color="blue">:ARG1</font> (<font color="green">d2 / draw-01</font>
                        <font color="blue">:ARG0</font> i
                        <font color="blue">:ARG1</font> (<font color="green">a2 / anything</font>))
                  <font color="blue">:time</font> (<font color="green">e / ever</font>)
                  <font color="blue">:ARG2</font>-of (<font color="green">e2 / except-01</font>
                        <font color="blue">:ARG1</font> (<font color="green">a3 / and</font>
                              <font color="blue">:op1</font> (<font color="green">b / boa</font>
                                    <font color="blue">:direction</font> (<font color="green">f / from</font>
                                          <font color="blue">:op1</font> (<font color="green">o / outside</font>)))
                              <font color="blue">:op2</font> (<font color="green">b2 / boa</font>
                                    <font color="blue">:direction</font> (<font color="green">f2 / from</font>
                                          <font color="blue">:op1</font> (<font color="green">i2 / inside</font>)))))))
      <font color="blue">:time</font> (<font color="green">a / age-01</font>
            <font color="blue">:ARG1</font> i
            <font color="blue">:ARG2</font> (<font color="green">t2 / temporal</font>-quantity <font color="blue">:quant</font> 6
                  <font color="blue">:unit</font> (<font color="green">y / year</font>))))

55. Now I stared at this sudden apparition with my eyes fairly starting out of my head in astonishment . (lpp_1943.55)


(<font color="green">s / stare-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> (<font color="green">t / thing</font>
            <font color="blue">:ARG1</font>-of (<font color="green">a / appear-01</font>
                  <font color="blue">:manner</font> (<font color="green">s2 / sudden</font>))
            <font color="blue">:mod</font> (<font color="green">t2 / this</font>))
      <font color="blue">:time</font> (<font color="green">n / now</font>)
      <font color="blue">:manner</font> (<font color="green">s3 / start-03</font>
            <font color="blue">:ARG0</font> (<font color="green">e / eye</font>
                  <font color="blue">:part-of</font> i)
            <font color="blue">:ARG1</font>-of (<font color="green">c / cause-01</font>
                  <font color="blue">:ARG0</font> (<font color="green">a2 / astonish-01</font>
                        <font color="blue">:ARG1</font> i))
            <font color="blue">:degree</font> (<font color="green">f / fair</font>)
            <font color="blue">:manner</font> (<font color="green">o / out-06</font>
                  <font color="blue">:ARG1</font> e
                  <font color="blue">:ARG2</font> (<font color="green">h / head</font>
                        <font color="blue">:part-of</font> i))))

56. Remember , I had crashed in the desert a thousand miles from any inhabited region . (lpp_1943.56)


(<font color="green">r / remember-01</font>
  <font color="blue">:ARG0</font> (<font color="green">y / you</font>)
  <font color="blue">:ARG1</font> (<font color="green">c / crash-01</font>
          <font color="blue">:ARG1</font> (<font color="green">i / i</font>)
          <font color="blue">:location</font> (<font color="green">d / desert</font>)
          <font color="blue">:location</font> (<font color="green">r3 / relative</font>-position
                      <font color="blue">:op1</font> (<font color="green">r2 / region</font>
                             <font color="blue">:ARG1</font>-of (<font color="green">i2 / inhabit-01</font>)
                             <font color="blue">:mod</font> (<font color="green">a2 / any</font>))
                      <font color="blue">:quant</font> (<font color="green">d2 / distance</font>-quantity
                               <font color="blue">:unit</font> (<font color="green">m / mile</font>)
                               <font color="blue">:quant</font> 1000)
                      <font color="blue">:direction</font> (<font color="green">a / away</font>)))
  <font color="blue">:mod</font>e imperative)

57. And yet my little man seemed neither to be straying uncertainly among the sands , nor to be fainting from fatigue or hunger or thirst or fear . (lpp_1943.57)


(<font color="green">c3 / contrast-01</font>
  <font color="blue">:ARG2</font> (<font color="green">s / seem-01</font>
          <font color="blue">:ARG1</font> (<font color="green">a / and</font>
                  <font color="blue">:op1</font> (<font color="green">s2 / stray-01</font>
                         <font color="blue">:ARG0</font> (<font color="green">m / man</font>
                                 <font color="blue">:mod</font> (<font color="green">l / little</font>)
                                 <font color="blue">:poss</font> (<font color="green">i / i</font>))
                         <font color="blue">:ARG1</font> (<font color="green">a3 / among</font>
                                 <font color="blue">:op1</font> (<font color="green">s3 / sand</font>))
                         <font color="blue">:manner</font> (<font color="green">c / certain</font>
                                   <font color="blue">:polarity</font> -)
                         <font color="blue">:polarity</font> -)
                  <font color="blue">:op2</font> (<font color="green">f / faint-01</font>
                         <font color="blue">:ARG0</font> m
                         <font color="blue">:ARG1</font>-of (<font color="green">c2 / cause-01</font>
                                    <font color="blue">:ARG0</font> (<font color="green">o / or</font>
                                            <font color="blue">:op1</font> (<font color="green">f2 / fatigue-01</font>)
                                            <font color="blue">:op2</font> (<font color="green">h / hunger-01</font>)
                                            <font color="blue">:op3</font> (<font color="green">t / thirst-01</font>)
                                            <font color="blue">:op4</font> (<font color="green">f3 / fear-01</font>)))
                         <font color="blue">:polarity</font> -))))

58. Nothing about him gave any suggestion of a child lost in the middle of the desert , a thousand miles from any human habitation . (lpp_1943.58)


(<font color="green">s / suggest-01</font>
  <font color="blue">:ARG0</font> (<font color="green">n / nothing</font>
          <font color="blue">:topic</font> (<font color="green">h / he</font>))
  <font color="blue">:ARG1</font> (<font color="green">c / child</font>
          <font color="blue">:ARG1</font>-of (<font color="green">l / lose-02</font>
                     <font color="blue">:location</font> (<font color="green">d / desert</font>
                                 <font color="blue">:part</font> (<font color="green">m / middle</font>))
                     <font color="blue">:location</font> (<font color="green">r / relative</font>-position
                                 <font color="blue">:op1</font> (<font color="green">t / thing</font>
                                        <font color="blue">:ARG1</font>-of (<font color="green">i / inhabit-01</font>
                                                   <font color="blue">:ARG0</font> (<font color="green">h2 / human</font>))
                                        <font color="blue">:mod</font> (<font color="green">a3 / any</font>))
                                 <font color="blue">:quant</font> (<font color="green">d2 / distance</font>-quantity
                                          <font color="blue">:unit</font> (<font color="green">m2 / mile</font>)
                                          <font color="blue">:quant</font> 1000)
                                 <font color="blue">:direction</font> (<font color="green">a2 / away</font>)))))

59. When at last I was able to speak , I said to him : " But -- what are you doing here ? " (lpp_1943.59)


(<font color="green">s / say-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> (<font color="green">c / contrast-01</font>
            <font color="blue">:ARG2</font> (<font color="green">b2 / be</font>-located-at-91 <font color="blue">:mode</font> interrogative
                  <font color="blue">:ARG1</font> (<font color="green">y2 / you</font>)
                  <font color="blue">:ARG2</font> (<font color="green">h2 / here</font>)
                  <font color="blue">:ARG1</font>-of (<font color="green">c2 / cause-01</font>
                        <font color="blue">:ARG0</font> (<font color="green">a / amr</font>-unknown))))
      <font color="blue">:ARG2</font> (<font color="green">h / he</font>)
      <font color="blue">:time</font> (<font color="green">p / possible-01</font>
            <font color="blue">:ARG1</font> (<font color="green">s2 / speak-01</font>
                  <font color="blue">:ARG0</font> i
                  <font color="blue">:time</font> (<font color="green">a2 / at</font>-last))))

60. And in answer he repeated , very slowly , as if he were speaking of a matter of great consequence : " If you please -- draw me a sheep ... " (lpp_1943.60)


(<font color="green">a / and</font>
      <font color="blue">:op2</font> (<font color="green">r / repeat-01</font>
            <font color="blue">:ARG0</font> (<font color="green">h / he</font>)
            <font color="blue">:ARG1</font> (<font color="green">d / draw-01</font> <font color="blue"><font color="blue">:mod</font>e</font> imperative <font color="blue">:polite</font> +
                  <font color="blue">:ARG0</font> (<font color="green">y2 / you</font>)
                  <font color="blue">:ARG1</font> (<font color="green">s3 / sheep</font>)
                  <font color="blue">:ARG2</font> (<font color="green">i / i</font>))
            <font color="blue">:purpose</font> (<font color="green">a2 / answer-01</font>
                  <font color="blue">:ARG0</font> h)
            <font color="blue">:ARG1</font>-of (<font color="green">s / slow-05</font>
                  <font color="blue">:degree</font> (<font color="green">v / very</font>))
            <font color="blue">:conj-as-if</font> (<font color="green">s2 / speak-01</font>
                  <font color="blue">:ARG0</font> h
                  <font color="blue">:ARG1</font> (<font color="green">m / matter</font>
                        <font color="blue">:mod</font> (<font color="green">c / consequence</font>
                              <font color="blue">:mod</font> (<font color="green">g / great</font>))))))

61. When a mystery is too overpowering , one dare not disobey . (lpp_1943.61)


(<font color="green">d / dare-01</font>
  <font color="blue">:ARG0</font> (<font color="green">o / one</font>)
  <font color="blue">:ARG2</font> (<font color="green">d2 / disobey-01</font>
          <font color="blue">:ARG0</font> o)
  <font color="blue">:polarity</font> -
  <font color="blue">:time</font> (<font color="green">o2 / overpower-01</font>
          <font color="blue">:ARG0</font> (<font color="green">m / mystery</font>)
          <font color="blue">:degree</font> (<font color="green">t2 / too</font>)))

62. Absurd as it might seem to me , a thousand miles from any human habitation and in danger of death , I took out of my pocket a sheet of paper and my fountain - pen . (lpp_1943.62)


(<font color="green">t / take-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>
            <font color="blue">:location</font> (<font color="green">r / relative</font>-position
                  <font color="blue">:op1</font> (<font color="green">p5 / place</font>
                        <font color="blue">:mod</font> (<font color="green">a3 / any</font>)
                        <font color="blue"><font color="blue">:ARG1</font>-of</font> (<font color="green">i2 / inhabit-01</font>
                              <font color="blue">:ARG0</font> (<font color="green">h / human</font>)))
                  <font color="blue">:quant</font> (<font color="green">d / distance</font>-quantity <font color="blue">:quant</font> 1000
                        <font color="blue">:unit</font> (<font color="green">m / mile</font>))
                  <font color="blue">:direction</font> (<font color="green">a2 / away</font>))
            <font color="blue"><font color="blue">:ARG1</font>-of</font> (<font color="green">e / endanger-01</font>
                  <font color="blue">:ARG0</font> (<font color="green">d2 / die-01</font>
                        <font color="blue">:ARG1</font> i)))
      <font color="blue">:ARG1</font> (<font color="green">a / and</font>
            <font color="blue">:op1</font> (<font color="green">p / paper</font>
                  <font color="blue">:quant</font> (<font color="green">s / sheet</font> <font color="blue">:quant</font> 1))
            <font color="blue">:op2</font> (<font color="green">p2 / pen</font>
                  <font color="blue">:mod</font> (<font color="green">f / fountain</font>)
                  <font color="blue">:poss</font> i))
      <font color="blue">:ARG2</font> (<font color="green">p3 / pocket</font>
            <font color="blue">:poss</font> i)
      <font color="blue">:concession</font> (<font color="green">p4 / possible-01</font>
            <font color="blue">:ARG1</font> (<font color="green">s2 / seem-01</font>
                  <font color="blue">:ARG1</font> (<font color="green">a4 / absurd</font>)
                  <font color="blue">:ARG2</font> i)))

63. But then I remembered how my studies had been concentrated on geography , history , arithmetic , and grammar , and I told the little chap ( a little crossly , too ) that I did not know how to draw . (lpp_1943.63)


(<font color="green">c4 / contrast-01</font>
      <font color="blue">:ARG2</font> (<font color="green">a / and</font>
            <font color="blue">:op1</font> (<font color="green">r / remember-01</font>
                  <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
                  <font color="blue">:ARG1</font> (<font color="green">c / concentrate-01</font>
                        <font color="blue">:ARG1</font> (<font color="green">a2 / and</font>
                              <font color="blue">:op1</font> (<font color="green">g / geography</font>)
                              <font color="blue">:op2</font> (<font color="green">h / history</font>)
                              <font color="blue">:op3</font> (<font color="green">a3 / arithmetic</font>)
                              <font color="blue">:op4</font> (<font color="green">g2 / grammar</font>))
                        <font color="blue">:ARG2</font> (<font color="green">s / study-01</font>
                              <font color="blue">:ARG0</font> i))
                  <font color="blue">:time</font> (<font color="green">t / then</font>))
            <font color="blue">:op2</font> (<font color="green">t2 / tell-01</font>
                  <font color="blue">:ARG0</font> i
                  <font color="blue">:ARG1</font> (<font color="green">k / know-03</font> <font color="blue">:polarity</font> -
                        <font color="blue">:ARG0</font> i
                        <font color="blue">:ARG1</font> (<font color="green">d / draw-01</font>
                              <font color="blue">:ARG0</font> i))
                  <font color="blue">:ARG2</font> (<font color="green">c2 / chap</font>
                        <font color="blue">:mod</font> (<font color="green">l / little</font>))
                  <font color="blue">:manner</font> (<font color="green">c3 / cross</font>
                        <font color="blue">:mod</font> (<font color="green">l2 / little</font>)
                        <font color="blue">:mod</font> (<font color="green">a4 / also</font>)))))

64. He answered me : " That does n't matter . (lpp_1943.64)


(<font color="green">a / answer-01</font>
  <font color="blue">:ARG0</font> (<font color="green">h / he</font>)
  <font color="blue">:ARG1</font> (<font color="green">i / i</font>)
  <font color="blue">:ARG2</font> (<font color="green">m2 / matter-01</font>
          <font color="blue">:ARG1</font> (<font color="green">t / that</font>)
          <font color="blue">:polarity</font> -))

65. Draw me a sheep ... " (lpp_1943.65)


(<font color="green">d / draw-01</font>
  <font color="blue">:ARG0</font> (<font color="green">y / you</font>)
  <font color="blue">:ARG1</font> (<font color="green">s / sheep</font>)
  <font color="blue">:ARG2</font> (<font color="green">i / i</font>)
  <font color="blue">:mode</font> imperative)

66. But I had never drawn a sheep . (lpp_1943.66)


(<font color="green">c / contrast-01</font>
  <font color="blue">:ARG2</font> (<font color="green">d / draw-01</font>
          <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
          <font color="blue">:ARG1</font> (<font color="green">s / sheep</font>)
          <font color="blue">:time</font> (<font color="green">e / ever</font>)
          <font color="blue">:polarity</font> -))

67. So I drew for him one of the two pictures I had drawn so often . (lpp_1943.67)


(<font color="green">c / cause-01</font>
  <font color="blue">:ARG1</font> (<font color="green">d / draw-01</font>
          <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
          <font color="blue">:ARG1</font> (<font color="green">p / picture</font>
                  <font color="blue">:quant</font> 1
                  <font color="blue">:ARG1</font>-of (<font color="green">i2 / include-91</font>
                             <font color="blue">:ARG2</font> (<font color="green">p2 / picture</font>
                                     <font color="blue">:quant</font> 2
                                     <font color="blue">:ARG1</font>-of (<font color="green">d2 / draw-01</font>
                                                <font color="blue">:ARG0</font> i
                                                <font color="blue">:time</font> (<font color="green">o / often</font>
                                                        <font color="blue">:degree</font> (<font color="green">s / so</font>))))))
          <font color="blue">:ARG2</font> (<font color="green">h / he</font>)))

68. It was that of the boa constrictor from the outside . (lpp_1943.68)


(<font color="green">b / boa</font>
      <font color="blue">:mod</font> (<font color="green">c2 / constrictor</font>)
      <font color="blue">:direction</font> (<font color="green">f / from</font>
            <font color="blue">:op1</font> (<font color="green">o / outside</font>)))

69. And I was astounded to hear the little fellow greet it with , " No , no , no ! (lpp_1943.69)


(<font color="green">a / and</font>
  <font color="blue">:op2</font> (<font color="green">a2 / astound-01</font>
         <font color="blue">:ARG0</font> (<font color="green">h / hear-01</font>
                 <font color="blue">:ARG0</font> i
                 <font color="blue">:ARG1</font> (<font color="green">g / greet-01</font>
                         <font color="blue">:ARG0</font> f
                         <font color="blue">:ARG1</font> (<font color="green">i2 / it</font>)
                         <font color="blue">:ARG3</font> (<font color="green">a3 / and</font>
                                 <font color="blue">:op1</font> (<font color="green">n / no</font>)
                                 <font color="blue">:op2</font> (<font color="green">n2 / no</font>)
                                 <font color="blue">:op3</font> (<font color="green">n3 / no</font>)))
                 <font color="blue">:ARG2</font> (<font color="green">f / fellow</font>
                         <font color="blue">:mod</font> (<font color="green">l / little</font>)))
         <font color="blue">:ARG1</font> (<font color="green">i / i</font>)))

70. I do not want an elephant inside a boa constrictor . (lpp_1943.70)


(<font color="green">w / want-01</font>
  <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
  <font color="blue">:ARG1</font> (<font color="green">e / elephant</font>
          <font color="blue">:location</font> (<font color="green">i2 / inside</font>
                      <font color="blue">:op1</font> (<font color="green">b2 / boa</font>
                             <font color="blue">:mod</font> (<font color="green">c2 / constrictor</font>))))
  <font color="blue">:polarity</font> -)

71. A boa constrictor is a very dangerous creature , and an elephant is very cumbersome . (lpp_1943.71)


(<font color="green">a / and</font>
  <font color="blue">:op1</font> (<font color="green">c2 / creature</font>
         <font color="blue">:mod</font> (<font color="green">d2 / dangerous</font>)
         <font color="blue">:domain</font> (<font color="green">b / boa</font>
                   <font color="blue">:mod</font> (<font color="green">c / constrictor</font>)))
  <font color="blue">:op2</font> (<font color="green">c3 / cumbersome</font>
         <font color="blue">:degree</font> (<font color="green">v2 / very</font>)
         <font color="blue">:domain</font> (<font color="green">e / elephant</font>)))

72. Where I live , everything is very small . (lpp_1943.72)


(<font color="green">s / small</font>
  <font color="blue">:degree</font> (<font color="green">v / very</font>)
  <font color="blue">:domain</font> (<font color="green">e / everything</font>)
  <font color="blue">:location</font> (<font color="green">l2 / live-01</font>
              <font color="blue">:ARG0</font> (<font color="green">i / i</font>)))

73. What I need is a sheep . (lpp_1943.73)


(<font color="green">n / need-01</font>
  <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
  <font color="blue">:ARG1</font> (<font color="green">s / sheep</font>))

74. Draw me a sheep . " (lpp_1943.74)


(<font color="green">d / draw-01</font>
  <font color="blue">:ARG0</font> (<font color="green">y / you</font>)
  <font color="blue">:ARG1</font> (<font color="green">s / sheep</font>)
  <font color="blue">:ARG2</font> (<font color="green">i / i</font>)
  <font color="blue">:mode</font> imperative)

75. So then I made a drawing . (lpp_1943.75)


(<font color="green">c / cause-01</font>
  <font color="blue">:ARG1</font> (<font color="green">d / draw-01</font>
          <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
          <font color="blue">:time</font> (<font color="green">t2 / then</font>)))

76. He looked at it carefully , then he said : " No . (lpp_1943.76)


(<font color="green">a / and</font>
  <font color="blue">:op1</font> (<font color="green">l / look-01</font>
         <font color="blue">:ARG0</font> (<font color="green">h / he</font>)
         <font color="blue">:ARG1</font> (<font color="green">i / it</font>)
         <font color="blue">:manner</font> (<font color="green">c / careful</font>))
  <font color="blue">:op2</font> (<font color="green">s / say-01</font>
         <font color="blue">:ARG0</font> h
         <font color="blue">:ARG1</font> (<font color="green">n / no</font>)
         <font color="blue">:time</font> (<font color="green">t / then</font>)))

77. This sheep is already very sickly . (lpp_1943.77)


(<font color="green">s2 / sick-05</font>
      <font color="blue">:ARG1</font> (<font color="green">s / sheep</font>
            <font color="blue">:mod</font> (<font color="green">t / this</font>))
      <font color="blue">:degree</font> (<font color="green">v / very</font>)
      <font color="blue">:time</font> (<font color="green">a / already</font>))

78. Make me another . " (lpp_1943.78)


(<font color="green">m / make-01</font>
  <font color="blue">:ARG0</font> (<font color="green">y / you</font>)
  <font color="blue">:ARG1</font> (<font color="green">a / another</font>)
  <font color="blue">:ARG3</font> (<font color="green">i / i</font>)
  <font color="blue">:mode</font> imperative)

79. So I made another drawing . (lpp_1943.79)


(<font color="green">c / cause-01</font>
      <font color="blue">:ARG1</font> (<font color="green">m / make-01</font>
            <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
            <font color="blue">:ARG1</font> (<font color="green">p / picture</font>
                  <font color="blue">:ARG1</font>-of (<font color="green">d / draw-01</font>
                        <font color="blue">:ARG0</font> i)
                  <font color="blue">:mod</font> (<font color="green">a / another</font>))))

80. My friend smiled gently and indulgently . (lpp_1943.80)


(<font color="green">s / smile-01</font>
      <font color="blue">:ARG0</font> (<font color="green">p / person</font>
            <font color="blue">:ARG0</font>-of (<font color="green">h / have</font>-rel-role-91
                  <font color="blue">:ARG1</font> (<font color="green">i / i</font>)
                  <font color="blue">:ARG2</font> (<font color="green">f / friend</font>)))
      <font color="blue">:manner</font> (<font color="green">g / gentle</font>)
      <font color="blue">:manner</font> (<font color="green">i2 / indulgent</font>))

81. " You see yourself , " he said , " that this is not a sheep . (lpp_1943.81)


(<font color="green">s / say-01</font>
  <font color="blue">:ARG0</font> (<font color="green">h / he</font>)
  <font color="blue">:ARG1</font> (<font color="green">s2 / see-01</font>
          <font color="blue">:ARG0</font> (<font color="green">y / you</font>)
          <font color="blue">:ARG1</font> (<font color="green">s4 / sheep</font>
                  <font color="blue">:domain</font> (<font color="green">t2 / this</font>)
                  <font color="blue">:polarity</font> -)))

82. This is a ram . (lpp_1943.82)


(<font color="green">r2 / ram</font>
  <font color="blue">:domain</font> (<font color="green">t2 / this</font>))

83. It has horns . " (lpp_1943.83)


(<font color="green">h / have-03</font>
      <font color="blue">:ARG0</font> (<font color="green">i / it</font>)
      <font color="blue">:ARG1</font> (<font color="green">h2 / horn</font>))

84. So then I did my drawing over once more . (lpp_1943.84)


(<font color="green">c / cause-01</font>
      <font color="blue">:ARG1</font> (<font color="green">d / do-02</font>
            <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
            <font color="blue">:ARG1</font> (<font color="green">p / picture</font>
                  <font color="blue">:ARG1</font>-of (<font color="green">d2 / draw-01</font>
                        <font color="blue">:ARG0</font> i))
            <font color="blue">:mod</font> (<font color="green">o / over</font>)
            <font color="blue">:mod</font> (<font color="green">a / again</font> <font color="blue">:frequency</font> 1)
            <font color="blue">:time</font> (<font color="green">t2 / then</font>)))

85. But it was rejected too , just like the others . (lpp_1943.85)


(<font color="green">c / contrast-01</font>
      <font color="blue">:ARG1</font> (<font color="green">r / reject-01</font>
            <font color="blue">:ARG1</font> (<font color="green">i / it</font>)
            <font color="blue">:ARG1</font>-of (<font color="green">r2 / resemble-01</font>
                  <font color="blue">:ARG2</font> (<font color="green">o / other</font>))
            <font color="blue">:mod</font> (<font color="green">t / too</font>)))

86. " This one is too old . (lpp_1943.86)


(<font color="green">o2 / old</font>
  <font color="blue">:degree</font> (<font color="green">t2 / too</font>)
  <font color="blue">:domain</font> (<font color="green">o / one</font>
            <font color="blue">:mod</font> (<font color="green">t / this</font>)))

87. I want a sheep that will live a long time . " (lpp_1943.87)


(<font color="green">w / want-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> (<font color="green">s / sheep</font>
            <font color="blue">:ARG0</font>-of (<font color="green">l / live-01</font>
                  <font color="blue">:ARG1</font>-of (<font color="green">l2 / long-03</font>))))

88. By this time my patience was exhausted , because I was in a hurry to start taking my engine apart . (lpp_1943.88)


(<font color="green">e / exhaust-01</font>
      <font color="blue">:ARG1</font> (<font color="green">p / patient-01</font>
            <font color="blue">:ARG1</font> (<font color="green">i / i</font>))
      <font color="blue">:ARG1</font>-of (<font color="green">c / cause-01</font>
            <font color="blue">:ARG0</font> (<font color="green">h / hurry-01</font>
                  <font color="blue">:ARG1</font> i
                  <font color="blue">:ARG2</font> (<font color="green">s / start-01</font>
                        <font color="blue">:ARG0</font> i
                        <font color="blue">:ARG1</font> (<font color="green">d / disassemble-01</font>
                              <font color="blue">:ARG0</font> i
                              <font color="blue">:ARG1</font> (<font color="green">e2 / engine</font>
                                    <font color="blue">:poss</font> i)))))
      <font color="blue">:time</font> (<font color="green">b / by</font>
            <font color="blue">:op1</font> (<font color="green">t / time</font>
                  <font color="blue">:mod</font> (<font color="green">t2 / this</font>))))

89. So I tossed off this drawing . (lpp_1943.89)


(<font color="green">c / cause-01</font>
      <font color="blue">:ARG1</font> (<font color="green">t / toss</font>-out-02
            <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
            <font color="blue">:ARG1</font> (<font color="green">p / picture</font>
                  <font color="blue">:ARG1</font>-of (<font color="green">d / draw-01</font>
                        <font color="blue">:ARG0</font> i)
                  <font color="blue">:mod</font> (<font color="green">t3 / this</font>))
            <font color="blue">:direction</font> (<font color="green">o / off</font>)))

90. And I threw out an explanation with it . (lpp_1943.90)


(<font color="green">a / and</font>
  <font color="blue">:op2</font> (<font color="green">e / explain-01</font>
         <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
         <font color="blue">:ARG1</font> (<font color="green">i3 / it</font>)))

91. " This is only his box . (lpp_1943.91)


(<font color="green">b / box</font>
  <font color="blue">:poss</font> (<font color="green">h / he</font>)
  <font color="blue">:domain</font> (<font color="green">t / this</font>)
  <font color="blue">:mod</font> (<font color="green">o / only</font>))

92. The sheep you asked for is inside . " (lpp_1943.92)


(<font color="green">b / be</font>-located-at-91
      <font color="blue">:ARG1</font> (<font color="green">s2 / sheep</font>
            <font color="blue">:ARG1</font>-of (<font color="green">a / ask-01</font>
                  <font color="blue">:ARG0</font> (<font color="green">y / you</font>)))
      <font color="blue">:ARG2</font> (<font color="green">i2 / inside</font>))

93. I was very surprised to see a light break over the face of my young judge : " That is exactly the way I wanted it ! (lpp_1943.93)


(<font color="green">a / and</font>
      <font color="blue">:op1</font> (<font color="green">s / surprise-01</font>
            <font color="blue">:ARG0</font> (<font color="green">s2 / see-01</font>
                  <font color="blue">:ARG0</font> i
                  <font color="blue">:ARG1</font> (<font color="green">b / break-13</font>
                        <font color="blue">:ARG1</font> (<font color="green">l / light</font>)
                        <font color="blue">:location</font> (<font color="green">o / over</font>
                              <font color="blue">:op1</font> (<font color="green">f / face</font>
                                    <font color="blue">:part-of</font> (<font color="green">p / person</font>
                                          <font color="blue">:ARG0</font>-of (<font color="green">j / judge-01</font>)
                                          <font color="blue">:poss</font> i
                                          <font color="blue">:mod</font> (<font color="green">y / young</font>))))))
            <font color="blue">:ARG1</font> (<font color="green">i / i</font>)
            <font color="blue">:degree</font> (<font color="green">v / very</font>))
      <font color="blue">:op2</font> (<font color="green">s3 / say-01</font>
            <font color="blue">:ARG1</font> (<font color="green">w / way</font>
                  <font color="blue">:mod</font> (<font color="green">e / exact</font>)
                  <font color="blue">:domain</font> (<font color="green">w2 / want-01</font>
                        <font color="blue">:ARG0</font> p
                        <font color="blue">:ARG1</font> (<font color="green">i2 / it</font>)))))

94. Do you think that this sheep will have to have a great deal of grass ? " (lpp_1943.94)


(<font color="green">t / think-01</font>
  <font color="blue">:ARG0</font> (<font color="green">y / you</font>)
  <font color="blue">:ARG1</font> (<font color="green">o / obligate-01</font>
          <font color="blue">:ARG2</font> (<font color="green">h / have-03</font>
                  <font color="blue">:ARG0</font> (<font color="green">s / sheep</font>
                          <font color="blue">:mod</font> (<font color="green">t2 / this</font>))
                  <font color="blue">:ARG1</font> (<font color="green">g / grass</font>
                          <font color="blue">:quant</font> (<font color="green">d / deal</font>
                                   <font color="blue">:mod</font> (<font color="green">g2 / great</font>)))))
  <font color="blue">:mod</font>e interrogative)

95. " Why ? " (lpp_1943.95)


(<font color="green">c / cause-01</font>
      <font color="blue">:ARG0</font> (<font color="green">a / amr</font>-unknown))

96. " Because where I live everything is very small ... " (lpp_1943.96)


(<font color="green">c / cause-01</font>
  <font color="blue">:ARG0</font> (<font color="green">s / small</font>
          <font color="blue">:degree</font> (<font color="green">v / very</font>)
          <font color="blue">:domain</font> (<font color="green">e / everything</font>
                    <font color="blue">:location</font> (<font color="green">l / live-01</font>
                                <font color="blue">:ARG0</font> (<font color="green">i / i</font>)))))

97. " There will surely be enough grass for him , " (lpp_1943.97)


(<font color="green">b / benefit-01</font>
      <font color="blue">:ARG0</font> (<font color="green">g3 / grass</font>
            <font color="blue">:mod</font> (<font color="green">e3 / enough</font>
                  <font color="blue"><font color="blue">:ARG1</font>-of</font> (<font color="green">s / sure-02</font>)))
      <font color="blue">:ARG1</font> (<font color="green">h2 / he</font>))

98. I said . (lpp_1943.98)


(<font color="green">s / say-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>))

99. " It is a very small sheep that I have given you . " (lpp_1943.99)


(<font color="green">g / give-01</font>
      <font color="blue">:ARG0</font> (<font color="green">i / i</font>)
      <font color="blue">:ARG1</font> (<font color="green">s / sheep</font>
            <font color="blue">:mod</font> (<font color="green">s2 / small</font>
                  <font color="blue">:degree</font> (<font color="green">v / very</font>)))
      <font color="blue">:ARG2</font> (<font color="green">y / you</font>))

100. He bent his head over the drawing : " Not so small that -- Look ! (lpp_1943.100)


(<font color="green">a / and</font>
      <font color="blue">:op2</font> (<font color="green">b / bend-01</font>
            <font color="blue">:ARG1</font> (<font color="green">h2 / head</font>
                  <font color="blue">:location</font> (<font color="green">o / over</font>
                        <font color="blue">:op1</font> (<font color="green">p / picture</font>
                              <font color="blue">:ARG1</font>-of (<font color="green">d / draw-01</font>)))
                  <font color="blue">:part-of</font> h3))
      <font color="blue">:op2</font> (<font color="green">s / say-01</font>
            <font color="blue">:ARG0</font> (<font color="green">h3 / he</font>)
            <font color="blue">:ARG1</font> (<font color="green">l / look-01</font> <font color="blue">:mode</font> imperative
                  <font color="blue">:ARG0</font> (<font color="green">y / you</font>)
                  <font color="blue">:ARG1</font> (<font color="green">s2 / small</font> <font color="blue">:polarity</font> -
                        <font color="blue">:degree</font> (<font color="green">s3 / so</font>)
                        <font color="blue">:domain</font> (<font color="green">t2 / that</font>)))))

