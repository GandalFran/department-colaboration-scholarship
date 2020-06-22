 
const neo4j = require('neo4j');
const config = require('../config/db.config');


module.exports = {
	getEntitites(){
		return new Promise(function(resolve,reject){
			const db = new neo4j.GraphDatabase(config.neo4jUrl);
			db.cypher({
				query:`
					MATCH (e:ENTS)-[CONTAINED_IN]->(n:NEWSITEMS)
					WITH e, n
					MATCH (child:ENTS)-[CONTAINED_IN]->(n)
					WHERE e<>child
					WITH e, COLLECT({newsLink:n.url, name:child.name, type:child.type}) as children
					RETURN e.name as name, e.type as type, children
					`
			}, function (error, ents) {
				if(error){
			    	reject(error);
				}else{
					resolve(ents)
				}
			});
		});
	}
}