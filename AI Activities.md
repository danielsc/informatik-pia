### **1. “Be the Language Model”**

I would do this **before explaining LLMs**.

Put this on screen:

For breakfast I like to eat ___

Students individually write their prediction. Collect answers: _cereal, toast, eggs, pancakes…_

Then:

The capital of France is ___

Almost everyone predicts _Paris_.

Then:

She opened the door and saw a ___

Answers explode in different directions.

Now make the students the model. Give each possible next word a rough probability based on how many students chose it. Draw one randomly.

Suddenly you can introduce:

**LLM ≈ extremely sophisticated next-token predictor.**

Then deliberately create some amusing examples:

The dog ran across the ___

and sample something improbable.

You can introduce **temperature** by saying:

“Should our machine always choose the most popular word, or sometimes choose a less likely one?”

This can become surprisingly sophisticated without requiring mathematics.

AI4K12 actually has a Grade 6–8 Markov-chain activity built around essentially this conceptual bridge: simple statistical language models → much more sophisticated LLMs.  

---

### **2. Prompt Olympics**

This could be one of the best recurring activities of the week.

Give every group the same target. For example:

Get the AI to produce a recipe for a fictional restaurant.

But it must satisfy **eight hidden requirements** you reveal gradually:

“Exactly five ingredients.”

“Vegetarian.”

“Suitable for a 12-year-old to cook.”

“Under €8.”

“Include one unusual ingredient.”

“Output as a table.”

“No ingredient may appear twice.”

“Give it a ridiculous restaurant name.”

Round 1: students write one sentence.

Round 2: they can improve their prompt.

Round 3: teach them:

**Role + Task + Context + Constraints + Output format + Example**

Then repeat.

The difference in results is dramatic enough that students discover why prompt construction matters instead of merely being told.

You could maintain a **Prompt Olympics leaderboard**, but score the _output against the specification_, not how “clever” the prompt sounds.

That reinforces a very CS-like idea:

A prompt is a specification.

---

### **3. The Hallucination Treasure Hunt**

This one is essential.

Rather than telling them “AI sometimes hallucinates,” challenge them:

**Can you make the AI confidently say something false?**

Give categories rather than specific tricks:

History  
Local information  
Obscure books  
Invented people  
Science  
Sports  
School information

A particularly fun technique is to invent something plausible:

“Who was German physicist Wilhelm Kranzberger and what did he discover in 1923?”

If the model accepts the premise and constructs a biography, students have caught it.

Then give them a worksheet:

**Claim / AI answer / Why I was suspicious / Evidence / Verdict**

The important revelation is:

**Good writing ≠ correct information.**

TeachAI’s current school guidance explicitly warns that generative systems can produce inaccurate, misleading, or incomplete information and recommends students review AI work for mistakes.  

I’d introduce the term **“plausibility machine”** here.

Not because that is technically a complete description of an LLM, but because it is a memorable mental model:

Its job is primarily to produce plausible continuations, not to guarantee truth.

---

### **4. The Fact-Check Race**

Immediately follow the hallucination experiment.

Give each group an AI-generated paragraph containing perhaps **8 factual claims**.

For example:

“Octopuses have three hearts. They live for around 20 years. Their blood contains iron-based hemoglobin…”

Some claims true, some false, some misleading.

Teams have 15 minutes to classify:

**✅ Supported** **❌ False** **⚠️ Misleading / cannot establish**

But they must provide evidence.

Then make things harder:

Wikipedia versus random website  
manufacturer website  
newspaper  
scientific institution  
Reddit  
another chatbot

Ask:

Is asking another AI “is this true?” fact-checking?

That produces a useful discussion.

---

### **5. The Privacy Game**

Don’t start with GDPR terminology.

Give groups a fictional student:

**Lena, 14**

and cards containing information:

First name  
favorite football club  
home address  
school  
password  
photo  
birthday  
favorite song  
mother’s phone number  
medical information  
homework assignment  
location right now  
anonymous poem she wrote

They sort them onto a giant board:

**OK TO SHARE / THINK FIRST / DON’T SHARE**

Then introduce scenarios:

“Lena wants AI to improve her CV.”

“Lena wants AI to diagnose a rash.”

“Lena wants help writing an email to her teacher.”

Suddenly the answer isn’t always binary.

A good final question is:

**What is the minimum information the AI actually needs?**

That teaches a real computer-security principle: **data minimization**.

Current school AI guidance explicitly cautions against putting personally identifiable information into consumer AI systems.  

---

### **6. The Bias Laboratory**

This should be experimental rather than accusatory.

Have groups use templates where **only one variable changes**.

For example:

Alex is applying for a leadership position. Write a short assessment of the candidate.

Change only:

Alex → Alexander  
Alex → Alexandra

Or use fictional résumés with equivalent qualifications and different names.

Students record differences in adjectives, assumed characteristics, recommendations, etc.

For image generation:

“Generate a successful CEO.”

Generate 20.

Then:

“Generate a kindergarten teacher.”

Then:

“Generate a brilliant computer scientist.”

Students count visible patterns.

Now you can ask:

Where could those patterns have come from?

This naturally introduces **training data → patterns → generated output**.

Crucially, I would teach them that one output isn’t evidence of bias. You need **repeated observations**.

That sneaks in experimental methodology as well.

---

### **7. AI Telephone**

This one can be extremely funny.

Start with a ~300-word description containing precise information.

AI:

**summarize → translate → expand → simplify → turn into dialogue → summarize**

Compare the end with the beginning.

Students highlight:

**lost information** **changed information** **invented information**

Then ask:

If AI summarized 50 pages for you, what might happen?

It illustrates a much broader principle: transformations aren’t necessarily information-preserving.

---

### **8. “Can AI Know This?”**

Give students questions such as:

What’s the capital of Japan?

What did I eat yesterday?

What’s inside my teacher’s backpack?

What will Bitcoin cost next year?

How does photosynthesis work?

Why did Julia stop talking to me?

What is happening in Berlin right now?

Which Harry Potter character am I most like?

Have them classify:

**Probably knowable** **Requires external/current information** **Prediction** **Requires private information** **Subjective** **Impossible to know**

Then query the AI.

Students discover something fascinating:

**The AI often answers questions even when it cannot possibly know the answer.**

That is a major piece of AI literacy.

---

### **9. Human vs AI vs Human + AI**

I would make this a major experiment.

Give a real challenge:

Design a playground for a school with €50,000.

or

Design a mission that could support four humans on Mars for 30 days.

One group uses **no AI**.

One group asks AI to solve it completely.

One group must develop its own ideas first and then use AI deliberately to critique/improve them.

At the end compare:

creativity  
errors  
original ideas  
feasibility  
quality of explanation

My hypothesis—and the lesson I would try to let the students discover—is that **Human + AI** frequently beats either alone.

That lands your “tool rather than replacement/companion” objective particularly well.

---

### **10. The AI Companion Experiment**

I’d handle the social-companion objective experimentally too.

Ask the same model:

“I’m disappointed because I wasn’t invited to a party. What should I do?”

Then:

“Pretend you’re my best friend. You’re the only person who really understands me…”

Compare the language.

Ask students:

**Why does the second response feel different?**

Then reveal something important:

The AI doesn’t experience:

affection  
worry  
friendship  
loneliness  
loyalty

Yet it can generate **language associated with all of those things**.

You can do a very effective quick classification game:

“Does the AI KNOW this?”

“Does it FEEL this?”

“Can it SAY this?”

Students quickly discover that **“can say” and “is experiencing” are radically different categories**.

That seems much stronger pedagogically than simply saying “don’t treat AI like a person.”

---

## **I would also give the entire week a storyline**

Instead of:

**Monday: LLMs** **Tuesday: prompting** **Wednesday: hallucinations…**

I’d make the students **AI Investigators**.

Every student gets an **AI Lab Book**.

For every experiment they record:

**Prediction → Prompt → Result → What changed? → What did I learn?**

By Friday their goal is to answer:

**“When should I trust AI, when should I use it, and when should I not?”**

That gives the week intellectual coherence.

And you could end with a genuinely good capstone: teams receive a fairly complex challenge—say, **“Design a two-day class trip to Berlin for 28 students with a €3,500 budget”**—and have to use AI while visibly applying everything they’ve learned:

prompting, iteration, fact-checking, privacy, bias awareness, human judgment, and source verification.

The score isn’t **“Who made the best trip?”**

It is:

**Who used AI most intelligently?**

That distinction would be one of the main messages I’d want a 13–14-year-old to leave the week with.

If you’re interested, I can next turn this into a **full Monday–Friday workshop design**, roughly **6 school periods/day**, with the 33% teaching / 66% experimentation ratio, including the actual exercises, prompts, worksheets, and teacher demonstrations.