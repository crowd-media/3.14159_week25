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
            form player 1
        </div>
        
        <div class="form_agent_2"> 
            form player 2 <br/>
            khbfv<br/>
            sfjnv<br/>
            fv
        </div>
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
      grid-template-columns: 1fr 1fr;
      display: flex;
      flex-direction: row;
      justify-content: space-evenly;
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
    padding: 10px;
            box-sizing: border-box;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .form_agent_2{
      grid-row: 3;
      grid-column: 2;
            box-shadow: 6px 6px 10px rgba(34, 34, 34, 0.2), -6px -6px 10px #fff;
    padding: 10px;
    box-sizing: border-box;
    border-radius: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  
  </style>
  