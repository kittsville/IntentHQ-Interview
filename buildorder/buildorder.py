import sets

def getBuildOrder(projects, dependencies = []):
    dependencyMap = {}
    dependencyFreeProjects = sets.Set(projects)

    for project in projects:
        dependencyMap[project] = []

    for (dependency, project) in dependencies:
        dependencyMap[dependency].append(project)
        dependencyFreeProjects.discard(project)

    buildOrder = []

    for project in dependencyFreeProjects:
        buildOrder.append(project)

        for dependentProject in dependencyMap[project]:
            buildOrder.append(dependentProject)

    return buildOrder
