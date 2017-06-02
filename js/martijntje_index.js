window.onload = function() {

  queue()
  .defer(d3.csv, 'bachelor.csv')
  .defer(d3.csv, 'master.csv')
  .await(begin_magic);

  function begin_magic(error, bachelor, master) {
  	if (error) throw error;

  	
    drawChord(bachelor, master);
  }
};
