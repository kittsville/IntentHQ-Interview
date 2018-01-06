import sets

class DependencyError(Exception):
    pass

def getBuildOrder(projects, dependencies = []):
    dependencyMap   = {}
    dependencyCount = {}
    dependencyFreeProjects = sets.Set(projects)

    for project in projects:
        dependencyMap[project]   = []
        dependencyCount[project] = 0

    for (dependency, project) in dependencies:
        dependencyMap[dependency].append(project)
        dependencyCount[project] += 1
        dependencyFreeProjects.discard(project)

    if len(dependencyFreeProjects) == 0:
        raise DependencyError("Unresolvable Project Dependencies")

    buildOrder = []

    for project in dependencyFreeProjects:
        buildOrder.append(project)

        for dependentProject in dependencyMap[project]:
            dependencyCount[dependentProject] -= 1

            if dependencyCount[dependentProject] == 0:
                buildOrder.append(dependentProject)

    return buildOrder
