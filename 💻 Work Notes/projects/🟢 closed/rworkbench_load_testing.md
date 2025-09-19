tags:: #project/doing, [[anthony-di-leo]], [[geoffrey-williams]]

- ## OBJECTIVE
	- To test the POSIT servers for migration to data analysis etc
		- DONE Planned testing day is on Thursday 26th June
		  SCHEDULED: <2025-06-26 Thu>
		- DONE Create code for each thing you need to test #next\\\\
			- Need to test
				- Phillip
					- Developing apps/pipelines
					- Running pipelines -> create synthetic pipeline to test
					- Building/Training ML models -> use the [[epath_lung_monitor/v151]] pipeline
					- Running/deployed apps/pipelines -> Have a shiny app that can be deployed as well
					- Test out a 1000x1000 matrix transpose (script can increase until a limit that we set is reached)
					  collapsed:: true
						- tests memory allocation, cpui and caching behaviours mand tests single threaded performance
						- ```
						  benchmark_matrix_test <- function(
						    start_size = 1000,
						    step = 1000,
						    max_time = 5,       # seconds
						    max_iterations = 100
						  ) {
						    library(pryr)  # for memory usage
						    results <- data.frame(
						      size = integer(),
						      time_sec = numeric(),
						      mem_mb = numeric(),
						      stringsAsFactors = FALSE
						    )
						  
						    for (i in 0:max_iterations) {
						      size <- start_size + i * step
						      cat(sprintf("Testing %dx%d matrix...\n", size, size))
						      
						      m <- matrix(runif(size * size), nrow = size)
						      
						      start <- Sys.time()
						      mt <- t(m)
						      end <- Sys.time()
						      
						      elapsed <- as.numeric(difftime(end, start, units = "secs"))
						      mem_used <- mem_used() / (1024^2)  # MB
						      
						      results <- rbind(results, data.frame(
						        size = size,
						        time_sec = elapsed,
						        mem_mb = mem_used
						      ))
						      
						      cat(sprintf("Time: %.3f sec, Memory used: %.1f MB\n", elapsed, mem_used))
						      
						      if (elapsed > max_time) {
						        cat("⛔️ Time threshold exceeded. Stopping benchmark.\n")
						        break
						      }
						      
						      rm(m, mt)
						      gc()
						    }
						  
						    return(results)
						  }
						  
						  # Run the test
						  results <- benchmark_matrix_test()
						  print(results)
						  
						  ```
						- Read and write performance of large files
					- Multicore pipeline to test as well
				- Peter
					- Testing MCMC models
- Test [[epath_lung_monitor/v151]]
	- DONE pipeline w single core - worked fine 6h45m vs local 5h45m
- ## NOTES
	- see links below