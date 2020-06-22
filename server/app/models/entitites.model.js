 
module.exports = {
	getEntitites(){
		const db = new Neo4J.GraphDatabase(neo4jUrl);
		db.cypher({
			query: `MATCH (e:ENTS)-[CONTAINED_IN]->(n:NEWSITEMS)
					WITH e, COUNT(CONTAINED_IN) as relations
					RETURN e, n
					`
		}, function (error, ents) {
			if(error){
		    	reject(error);
			}else{
				resolve(ents)
			}
		});
	}
}