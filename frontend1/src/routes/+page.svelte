<script>
	import Button from "./Button.svelte";
</script>

<main>
    <h1>El Debate</h1>
    
    <div class="header"> 
        <div class=botton_prompt>
            <Button />
        </div>
        <div class=botton_conversation>
            <Button />
        </div>
    </div>
    
    <div class="forms"> 
        <div class="form_agent_1"> 
            <br/>
            <br/>
            form agent 1<br/>
            <br/>
            <br/>
        </div>
        
        <div class="form_agent_2"> 
            <br/>
            <br/>
            form agent 2<br/>
            <br/>
            <br/>
        </div>
    </div> 
    
    <div class="topic">
        Add your topic:
    </div>

    <div class="generate-promps">
        Generate Prompts!
    </div>



</main>
    
    
    
<style>
    main {
      font-family: sans-serif;
      text-align: center;
      margin: 40px auto;
    }
    .header {
      text-align: center;
              box-shadow: 6px 6px 10px rgba(34, 34, 34, 0.2), -6px -6px 10px #fff;
      padding: 10px;
              box-sizing: border-box;
      border-radius: 20px;
      display: flex;
      flex-direction: row;
      justify-content: space-evenly;
  }
  .topic{
      box-shadow: 6px 6px 10px rgba(34, 34, 34, 0.2), -6px -6px 10px #fff;
      padding: 10px;
      box-sizing: border-box;
      border-radius: 20px;
      margin: 20px auto;
  }
  .generate-promps{
      background-color: rgb(255, 159, 103);
      box-shadow: 6px 6px 10px rgba(34, 34, 34, 0.2), -6px -6px 10px #fff;
      padding: 10px;
      box-sizing: border-box;
      border-radius: 20px;
      margin: 30px auto;
  }

  .forms{
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 20px;
  }
  .form_agent_1{
    grid-row: 3;
    grid-column: 1;
    box-shadow: 6px 6px 10px rgba(34, 34, 34, 0.2), -6px -6px 10px #fff;
    border-radius: 20px;
    padding: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .form_agent_2{
    grid-row: 3;
    grid-column: 2;
    box-shadow: 6px 6px 10px rgba(34, 34, 34, 0.2), -6px -6px 10px #fff;
    padding: 10px;
    border-radius: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  </style>
  